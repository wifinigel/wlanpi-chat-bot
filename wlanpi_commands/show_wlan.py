from .command import Command
import subprocess
import re

from utils.os_cmds import IFCONFIG_CMD, IWCONFIG_CMD
class ShowWlan(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_wlan"
    

    def field_extractor(self, field_name, pattern, cmd_output_text):

        re_result = re.search(pattern, cmd_output_text)

        if not re_result is None:
            field_value = re_result.group(1)
            return field_value
        else:
            return None
    
    def channel_lookup(self, freq):

        channels = {
            '2.412': 1, '2.417': 2, '2.422': 3,  '2.427': 4,
            '2.432': 5, '2.437': 6, '2.442': 7,  '2.447': 8,
            '2.452': 9, '2.457': 10,'2.462': 11, '2.467': 12,
            '2.472': 13,'2.484': 14,'5.18': 36, '5.2':  40,
            '5.22': 44, '5.24':  48,'5.26': 52,'5.28':  56,
            '5.3':  60, '5.32': 64,'5.5': 100,'5.52': 104,
            '5.54': 108,'5.56': 112,'5.58': 116,'5.6': 120,
            '5.62': 124,'5.64': 128, '5.66': 132, '5.68': 136,
            '5.7': 140, '5.72': 144, '5.745': 149,'5.765': 153,
            '5.785': 157,'5.805': 161, '5.825': 165
        }

        return channels.get(freq, 'unknown')
    

    def run(self, args_list):
        '''
        Create page to summarise WLAN interface info
        '''

        ifconfig_file = IFCONFIG_CMD
        iwconfig_file = IWCONFIG_CMD

        try:
            ifconfig_info = subprocess.check_output('{} -s'.format(ifconfig_file), shell=True).decode()
        except Exception as ex:
            return "Err: ifconfig error: {}".format(ex)

        # Extract interface info
        interface_re = re.findall(
            r'^(wlan\d)  ', ifconfig_info, re.DOTALL | re.MULTILINE)
        if not interface_re:
            return "Err: command failed: ifconfig match error."
        else:
            for interface_name in interface_re:

                interface_info = []
                ssid = False
                freq = False
                channel = False
                mode = False

                # use iwconfig to find further info for each wlan interface
                try:
                    cmd = "{} {}".format(iwconfig_file, interface_name)
                    iwconfig_info = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True).decode()
                except subprocess.CalledProcessError:
                    return "Err: iwconfig cmd failed"

                # Extract SSID
                pattern = r'ESSID\:\"(.*?)\"'
                field_name = "ssid"
                extraction = self.field_extractor(field_name, pattern, iwconfig_info)
                if extraction:
                    ssid = extraction

                # Extract Frequency
                pattern = r'Frequency[\:|\=](\d+\.\d+) '
                field_name = "freq"
                extraction = self.field_extractor(field_name, pattern, iwconfig_info)
                if extraction:
                    freq = extraction

                # lookup channel number from freq
                if freq:
                    channel = self.channel_lookup(str(freq))
                
                # Extract Mode
                pattern = r'Mode\:(.*?) '
                field_name = "mode"
                extraction = self.field_extractor(
                    field_name, pattern, iwconfig_info)
                if extraction:
                    mode = extraction

                # construct our page data - start with name
                interface_info.append("Interface: " + interface_name)

                # SSID
                if 'ssid':
                    interface_info.append("SSID: {}".format(ssid))
                else:
                    interface_info.append("SSID: N/A")

                # Mode
                if 'mode':
                    interface_info.append( "Mode: {}".format(mode))
                else:
                    interface_info.append("Mode: N/A")

                # Channel
                if 'channel':
                    interface_info.append("Ch: {}".format(channel))
                else:
                    interface_info.append("Ch: unknown")

        return self._render(interface_info)


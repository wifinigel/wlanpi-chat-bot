from wlanpi_commands.command import Command
from utils.constants import SPOOL_DIR_FILES

import os

class ExecWirelessCapture(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "exec_wireless_capture"

        # defaults
        self.channel = False
        self.channel_width = 'HT20'
        self.interface = 'wlan0'
        self.duration = 20

        self.valid_channels = [1,2,3,4,5,6,7,8,9,10,11,12,13,36,40,44,48,
            52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,
            149,153,157,161,165]
        self.valid_widths = ['20', '40+', '40-', '80']
        self.width = { '20': "HT20", '40+': "HT40+", '40-': "HT40-", '80': "80MHz" }
        
        
        self.max_duration = 60
    
    def help_message(self):
        """
        Return the help page for this command
        """
        short_msg = """Performs a wireless
capture, uploads the
capture file."""
        long_msg = """Perform a wireless capture and uploads the resulting file (note that the file upload limit is 20Mb)       

Args:
 [1] Channel [mandatory] (1-13, 36-165)
 [2] Ch width [optional] (20*, 40+, 40-, 80)
 [3] Interface [optional] (wlan0*)
 [4] Capture duration [optional] (20* (secs))

 (* = default value)

 Example: ex wi 36 40+ wlan0 10
"""

        return self._render_help(short_msg, long_msg)
    
    def run(self, args_list):   
        
        # trigger capture
        cmd_string = "/opt/wlanpi-chat-bot/scripts/wireless_capture.sh"

        # check args
        if len(args_list) > 0:
            if int(args_list[0]) not in self.valid_channels:
                return("Invalid channel number supplied.")
            else:
                self.channel = args_list[0]
        else:
            return("Capture failed, no channel number supplied.\n(See 'help exec wireless capture')")
        
        if len(args_list) > 1:
            if args_list[1] not in self.valid_widths:
                return("Invalid channel width supplied.")
            else:
                self.channel_width = self.width[ args_list[1] ]
        
        if len(args_list) > 2:
            self.interface = args_list[2]
        
        if len(args_list) > 3:
            self.duration = args_list[3]

            # enforce hard limit
            if int(self.duration) > self.max_duration:
                self.duration = self.max_duration
        
        progress_msg = "Starting wireless capture...(ch = {}, width = {}, i/f = {}, duration = {} secs)".format(
            self.channel, self.channel_width, self.interface, self.duration)
        
        cmd_string = cmd_string + " {} {} {} {}".format(self.channel, self.channel_width, self.interface, self.duration)

        if self.run_ext_cmd(progress_msg, cmd_string):
            self.telegram_object.send_msg("Capture completed.", self.telegram_object.chat_id)
        else:
            return("Capture failed.")

        filename = '/tmp/wlandump.pcap'

        # if file size < 50Mb, send to spooler
        if os.stat(filename).st_size < 50e6:
            # copy capture file to files spooler dir
            os.system("cp {} {}".format(filename, SPOOL_DIR_FILES))
            return("Capture file sent to file spooler...please wait.")
        else:
            return("Capture file is too large to send over Telegram (> 50Mb)")
        

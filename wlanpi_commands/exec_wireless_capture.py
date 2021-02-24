from .command import Command
import os

class ExecWirelessCapture(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "exec_wireless_capture"
    
    def run(self, args_list):   
        progress_msg = "starting wireless capture..."
        #self.telegram_object.send_msg(progress_msg, self.telegram_object.chat_id)

        # trigger capture
        cmd_string = "/opt/wlanpi-chat-bot/scripts/wireless_capture.sh"
        
        if self.run_ext_cmd(progress_msg,cmd_string):
            self.telegram_object.send_msg("Capture completed.", self.telegram_object.chat_id)
        else:
            return("Capture failed.")

        filename = '/tmp/wlandump.pcap'

        try:
            with open(filename, 'rb') as document:
                doc = document.read()
        except IOError:
            return("Capture file access issue - please check path and name.")

        if self.telegram_object.send_file(doc, self.telegram_object.chat_id, "PCAP File"):
            return("Capture file sent OK")
        else:
            return("Capture file transfer failed")

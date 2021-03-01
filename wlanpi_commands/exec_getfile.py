import os

from wlanpi_commands.command import Command

class ExecGetfile(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.telegram_object = telegram_object
        self.command_name = "exec_getfile"
       
    def run(self, args_list):      

        progress_msg = "Getting file..."
        self.telegram_object.send_msg(progress_msg, self.telegram_object.chat_id)

        filename = ''
        if len(args_list) > 0:
            filename = args_list[0]
        else:
             return"Please supply filename. Failed"

        if self.telegram_object.send_file(filename, self.telegram_object.chat_id):
            return("File sent OK")
        else:
            return("File transfer failed")


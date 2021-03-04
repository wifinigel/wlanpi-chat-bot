import os

from wlanpi_commands.command import Command

class ExecGetfile(Command):
    
    def __init__(self, telegram_object, conf_obj):
        # extend Command base class
        super().__init__(telegram_object, conf_obj)

        self.telegram_object = telegram_object
        self.command_name = "exec_getfile"
    
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Uploads a file from the supplied OS path (note that the file upload limit is 50Mb)       

Args:
 [1] Filename [mandatory] (e.g. /etc/hosts)

 Example: exec getfile /etc/hosts
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
       
    def run(self, args_list):      

        progress_msg = "Getting file..."
        self.telegram_object.send_msg(progress_msg, self.telegram_object.chat_id)

        filename = ''
        if len(args_list) > 0:

            if args_list[0] == "?":
                return self._render(self.help_message())
            
            filename = args_list[0]
        else:
             return"Please supply filename. Failed"

        if self.telegram_object.send_file(filename, self.telegram_object.chat_id):
            return("File sent OK")
        else:
            return("File transfer failed")


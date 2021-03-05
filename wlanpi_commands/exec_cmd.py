import os

from wlanpi_commands.command import Command

class ExecCmd(Command):
    
    def __init__(self, telegram_object, conf_obj):
        # extend Command base class
        super().__init__(telegram_object, conf_obj)

        self.telegram_object = telegram_object
        self.command_name = "exec_cmd"
    
    
    def help_message(self):
        """
        Run an OS command
        """
        long_msg = """Runs an OS level command passsed as an arg

** Caveat: if you execute a command that never returns, bot will be locked up and require process restart.

Args:
 [1] OS_level command [mandatory] (e.g. ls -l /tmp)

 Example: exec cmd ls -l /tmp
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
       
    def run(self, args_list):      

        cmd_string = ''

        if len(args_list) > 0:

            if args_list[0] == "?":
                return self._render(self.help_message())
            
            cmd_string = " ".join(args_list)
        else:
            return self._render("Unable to command, no command passed (syntax : exec os &lt;cli command&gt;)")

        progress_msg = "Executing command..."
        return self._render(self.run_ext_cmd(progress_msg,cmd_string))


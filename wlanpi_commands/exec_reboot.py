from .command import Command
import os

class ExecReboot(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "exec_reboot"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Performs probe reboot (with 1 minute delay).       

Args: None

 Example: exec reboot
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
    
    def run(self, args_list):

        if len(args_list) > 0:
            if args_list[0] == "?":
                    return self._render(self.help_message())
            else:
                return self._render("Unknown argument.")

        os.system('shutdown -r')
        return self._render("Attempting reboot in 1 minute...")
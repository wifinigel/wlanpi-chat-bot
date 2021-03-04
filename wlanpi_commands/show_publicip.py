from .command import Command

class ShowPublicip(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_publicip"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Displays public IP that the probe is behind.       

Args: None

 Example: show publicip
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
       
    def run(self, args_list):
        
        # check if help rquired
        if len(args_list) > 0:
            if args_list[0] == "?":
                    return self._render(self.help_message())
            else:
                return self._render("Unknown argument.")

        progress_msg = "Getting Public IP..."
        cmd_string = "/usr/share/fpms/BakeBit/Software/Python/scripts/networkinfo/publicip.sh"
        return self._render(self.run_ext_cmd(progress_msg,cmd_string))

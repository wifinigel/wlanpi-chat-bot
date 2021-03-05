from .command import Command

class ShowMode(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_mode"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Displays current running mode of the probe (e.g. classic, wiperf, etc...).       

Args: None

 Example: show mode
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
    
    def run(self, args_list):

        # check if help rquired if we have unexpected args
        if len(args_list) > 0:
            return self.check_if_help_required(args_list)
        
        STATUS_FILE="/etc/wlanpi-state"
        status = "WLAN Pi mode: {}".format(self._read_file( STATUS_FILE)[0])
        return self._render(status.strip())


from .command import Command

class ShowCDP(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_cdp"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Displays CDP info detected by the probe.       

Args: None

 Example: show cdp
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
    
    def run(self, args_list):

        # check if help rquired if we have unexpected args
        if len(args_list) > 0:
            return self.check_if_help_required(args_list)
        
        # read in CDP data is available
        cdp_data = self._read_file('/tmp/cdpneigh.txt')

        if not cdp_data:
            cdp_data = "No CDP data found"

        return self._render(cdp_data)
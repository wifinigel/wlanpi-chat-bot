from .command import Command

class ShowUptime(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_uptime"
       
    def run(self, args_list):      

        # check if help rquired if we have unexpected args
        if len(args_list) > 0:
            return self.check_if_help_required(args_list)

        progress_msg = "Getting uptime..."
        cmd_string = "/usr/bin/uptime"
        return self._render(self.run_ext_cmd(progress_msg,cmd_string))

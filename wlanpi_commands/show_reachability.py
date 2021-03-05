from .command import Command
import os
import subprocess

class ShowReachability(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_reachability"
    
    def run(self, args_list):      

        # check if help rquired if we have unexpected args
        if len(args_list) > 0:
            return self.check_if_help_required(args_list)

        progress_msg = "Getting reachability info..."
        cmd_string = "/usr/share/fpms/BakeBit/Software/Python/scripts/networkinfo/reachability.sh"
        return self._render(self.run_ext_cmd(progress_msg,cmd_string))
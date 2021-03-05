from .command import Command
from utils.node_data_snapshot import DataSnapshot
import os

class ShowStatus(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_status"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        short_msg = "Shows unit status\ninc uptime\n&interface addrs"
        long_msg = """Show unit status, including hostname, uptime, current status and interface IP addresses        

Args: None"""

        return self._render_help(short_msg, long_msg)
    
    def run(self, args_list):

        # check if help rquired if we have unexpected args
        if len(args_list) > 0:
            return self.check_if_help_required(args_list)

        # remove snapshot file & re-init snapshot
        snapshot = DataSnapshot()
        os.remove(snapshot.local_file)
        status_update = snapshot.node_status()

        return self._render(status_update)
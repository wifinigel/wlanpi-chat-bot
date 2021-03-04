from .command import Command
import os
import subprocess

from utils.os_cmds import PING_CMD

class ExecPing(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "exec_ping"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Performs a ping test and reports result.       

Args:
 [1] Target ip [mandatory] (e.g. 192.168.0.99)

  (* = default value)

 Example: exec ping 192.168.0.99 udp
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
    
    def run(self, args_list):

        target_ip = ''

        if len(args_list) > 0:

            if args_list[0] == "?":
                return self._render(self.help_message())
            
            target_ip = args_list[0]
        else:
            return self._render("Unable to run test, no IP address passed (syntax : exec ping &lt;ip_address&gt;)")

        progress_msg = "Runing ping test..."
        cmd_string = "{} -c 10 -W 1 -i 0.2 {} 2>&1".format(PING_CMD, target_ip) 
        return self._render(self.run_ext_cmd(progress_msg,cmd_string))

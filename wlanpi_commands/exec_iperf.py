from .command import Command
import os
import subprocess

from utils.os_cmds import IPERF_CMD

class ExecIperf(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "exec_iperf"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Performs iperf2 test and reports result.       

Args:
 [1] Target ip [mandatory] (e.g. 192.168.0.99)
 [2] Test protocol [optional] (e.g. tcp* or udp)

  (* = default value)

 Example: exec iperf 192.168.0.99 udp
"""
        short_msg = long_msg
        return self._render_help(short_msg, long_msg)
        
    def run(self, args_list):      

        target_ip = ''
        proto = "tcp"

        # pull off the first arg, which is IP address
        if len(args_list) > 0:

            if args_list[0] == "?":
                return self._render(self.help_message())
            
            target_ip = args_list[0]
        
        if len(args_list) > 1:
            proto = args_list[1]
        
        proto_switch = "" # blank = tcp
        if proto == "udp": proto_switch = "-u"

        if target_ip:
            progress_msg = "Runing iperf test ({})...".format(proto)
            cmd_string = "{} -i 1 {} -c {} 2>&1".format(IPERF_CMD, proto_switch, target_ip)
            return self._render(self.run_ext_cmd(progress_msg,cmd_string))
        else:
            return self._render("Unable to run test, no IP address passed (syntax : exec iperf &lt;ip_address&gt; [ udp | tcp ])")
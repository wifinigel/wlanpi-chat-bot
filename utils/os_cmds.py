"""
Centralised file for all OS commands used by chatbot
"""

import pathlib
import shutil

def _find_cmd(cmd):
    """
    This function checks if an OS command is available.

    Returns: filename (if exists/found) or False if not found
    """
    path = pathlib.Path(cmd)

    if not path.is_file():
        # as we can't find it, lets hunt through the path
        command_name = cmd.split('/')[-1]
        found_cmd = shutil.which(command_name)

        if not found_cmd:     
            return False
        else:
            # re-write cmd path
            return found_cmd
    
    return cmd

# define mandatory OS commands (attempt to find in path if not in hardcoded path)
OS_CORE_CMDS = {
    'DHCLIENT_CMD': _find_cmd('/sbin/dhclient'),
    'IFCONFIG_CMD': _find_cmd('/sbin/ifconfig'),
    'IF_DOWN_CMD': _find_cmd('/sbin/ifdown'),
    'IF_UP_CMD': _find_cmd('/sbin/ifup'),
    'IP_CMD': _find_cmd('/sbin/ip'),
    'IWCONFIG_CMD': _find_cmd('/sbin/iwconfig'),
    'IW_CMD': _find_cmd('/sbin/iw'),
    'NC_CMD': _find_cmd('/bin/nc'),
    'PING_CMD': _find_cmd('/bin/ping'),
    'REBOOT_CMD': _find_cmd('/sbin/reboot'),
    'ROUTE_CMD': _find_cmd('/sbin/route'),
    'TIMEDATECTL_CMD': _find_cmd('/usr/bin/timedatectl'),
    'CURL_CMD': _find_cmd('/usr/bin/curl'),
    'IPERF_CMD': _find_cmd('/usr/bin/iperf'),
    'IPERF3_CMD': _find_cmd('/usr/bin/iperf3'),
}

# define optional OS commands (attempt to find in path if not in hardcoded path)
OS_OPT_CMDS = {}

# define exportable vars
DHCLIENT_CMD = OS_CORE_CMDS['DHCLIENT_CMD']
IFCONFIG_CMD = OS_CORE_CMDS['IFCONFIG_CMD']
IF_DOWN_CMD = OS_CORE_CMDS['IF_DOWN_CMD']
IF_UP_CMD = OS_CORE_CMDS['IF_UP_CMD']
IP_CMD = OS_CORE_CMDS['IP_CMD']
IWCONFIG_CMD = OS_CORE_CMDS['IWCONFIG_CMD']
IW_CMD = OS_CORE_CMDS['IW_CMD']
NC_CMD = OS_CORE_CMDS['NC_CMD']
PING_CMD = OS_CORE_CMDS['PING_CMD']
REBOOT_CMD = OS_CORE_CMDS['REBOOT_CMD']
ROUTE_CMD = OS_CORE_CMDS['ROUTE_CMD']
TIMEDATECTL_CMD = OS_CORE_CMDS['TIMEDATECTL_CMD']
CURL_CMD = OS_CORE_CMDS['CURL_CMD']
IPERF_CMD = OS_CORE_CMDS['IPERF_CMD']
IPERF3_CMD = OS_CORE_CMDS['IPERF3_CMD']

def check_os_cmds(file_logger):
    """
    This function checks if all expected OS commands are avaiable.
    """

    # emit warning msg for missing optional commands
    file_logger.info("Checking optional OS commands are available.")
    
    for cmd_name in OS_OPT_CMDS.keys():

        if not OS_OPT_CMDS[cmd_name]:     
            file_logger.warning("Unable to find optional OS command: {} (Some functionality may not be available)".format(cmd_name))
    
    # return failure for missing core command
    file_logger.info("Checking required OS commands are available.")

    for cmd_name in OS_CORE_CMDS.keys():

        if not OS_CORE_CMDS[cmd_name]:     
            file_logger.error("Unable to find required OS command: {}".format(cmd_name))
            return False
    
    file_logger.info("Required OS commands checked OK.")
    return True


from .command import Command
import psutil

class ShowInterfaces(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_interfaces"
    
    def help_message(self):
        """
        Return the help page for this command
        """
        long_msg = """Displays a summary of probe interfaces.       

Args: None

 Example: show interfaces
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
        
        """
        Info: 

        {'eth0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1000, mtu=1500),
        'lo': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=65536),
        'usb0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),
        'wlan0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=2312)}
        
        psutil.net_if_stats()
        
        {'eth0': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.0.25', netmask='255.255.255.0', broadcast='192.168.0.255', ptp=None),
          snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::1:1bff:fe4e:35e8%eth0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
          snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='02:01:1b:4e:35:e8', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)],
        'lo': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None),
        snicaddr(family=<AddressFamily.AF_INET6: 10>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),
        snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:00:00:00:00', netmask=None, broadcast=None, ptp=None)],
        'usb0': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.42.1', netmask='255.255.255.224', broadcast='169.254.42.31', ptp=None),
          snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='76:bb:3e:ba:1d:5f', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)],
        'wlan0': [snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::220d:b0ff:fe32:37df%wlan0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
           snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='20:0d:b0:32:37:df', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)]}
        
        psutil.net_if_addrs()
        """

        interface_stats = psutil.net_if_stats()
        interface_addresses= psutil.net_if_addrs()
        interface_list = []

        for if_name in  interface_stats.keys():

          ip_addr = " [No IP addr] "
          if interface_addresses[if_name][0].family == 2:
            ip_addr = interface_addresses[if_name][0].address
          
          if_status = interface_stats[if_name].isup
          
          if_up_down = "Down"
          if if_status == True:
            if_up_down = "Up"
          
          if_summary = "{} {} ({})".format(if_name, ip_addr, if_up_down)
          interface_list.append(if_summary)

        net_info = "Interface list: \n\n" + "\n".join(interface_list)
        
        return self._render(net_info)


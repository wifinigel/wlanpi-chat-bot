from .command import Command
import psutil

class ShowInterfaces(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_interfaces"
    
    def run(self, args_list):
        
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

        
        return self._render(net_info)


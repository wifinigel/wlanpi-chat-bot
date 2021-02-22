from .command import Command
import os

class ShowVersion(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_ver"
    
    def run(self, args_list):
        
        WLANPI_IMAGE_FILE = '/etc/wlanpi-release'

        version_string = "No version info found"
        
        if os.path.isfile(WLANPI_IMAGE_FILE):
            with open(WLANPI_IMAGE_FILE, 'r') as f:
                lines = f.readlines()
            
            # pull out the version number
            for line in lines:
                (name, value) = line.split("=")
                if name=="VERSION":
                    version = value.strip()
                    version_string = "WLAN Pi " + version[1:-1]
                    break           

        return self._render(version_string)
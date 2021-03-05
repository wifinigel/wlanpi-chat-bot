from .command import Command

class ShowTime(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "show_time"
    
    def run(self, args_list):

        # check if help rquired if we have unexpected args
        if len(args_list) > 0:
            return self.check_if_help_required(args_list)
        
        import time
        return self._render(time.ctime())


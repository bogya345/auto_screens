
import threading

class myThread (threading.Thread):
    def __init__(self, thread_name, func, name, time_limit=-1, period=-1, *args):
        # threading.Thread.__init__(self)
        super(myThread, self).__init__()
        self.thread_name = thread_name
        self.func = func
        self.name = name
        self.time_limit = time_limit
        self.period = period
        self.args = args

        self._stop_event = threading.Event()
        
    def run(self):
        print("Starting " + self.name)
        ## random_part(name, time_limit)
        ## press_part(name)
        ## period_part(name, period)
        ## delete_equals_pics(name, period)
        if (self.thread_name == 'random_part'):
            self.func(self.name, self.time_limit)
            pass
        elif (self.thread_name == 'press_part'):
            self.func(self.name)
            pass
        elif (self.thread_name == 'period_part'):
            self.func(self.name, self.period)
            pass
        elif (self.thread_name == 'delete_equals_pics'):
            self.func(self.name, self.period)
            pass
        print("Exiting " + self.thread_name)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

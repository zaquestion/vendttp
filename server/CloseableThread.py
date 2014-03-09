import threading
class CloseableThread(threading.Thread):
    running = false
    
    def __init__(self, group = None, target = None, name = None, args=(), kwargs={}):
        threading.Thread.__init__(self, group = group, target = target, name = name, args=args, kwargs=kwargs)

    def start():
        Running = true
        threading.Thead.start()

    def stop(onStop=None):
        Running = false
        if (onStop):
            onStop()

import time
import threading

def timeString():
    time_string = time.strftime('%H:%M:%S')
    threading.Timer(1, timeString).start()
    return time_string
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from maincode import *

class  MyHandler(FileSystemEventHandler):
    def on_modified(self,  event):
        print(f'event type: {event.event_type} path : {event.src_path}')
        #if str(event.src_path) == r"\\DESKTOP-DVDGK9R\Users\tordv\OneDrive\Documents\Assetto Corsa\out\race_out.json":
        if str(event.src_path) == r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\watchedfiles\testfile.json":
            print_out(event.src_path)
    def on_created(self,  event):
        print(f'event type: {event.event_type} path : {event.src_path}')
    def on_deleted(self,  event):
        print(f'event type: {event.event_type} path : {event.src_path}')

if __name__ ==  "__main__":
    event_handler = MyHandler()
    observer = Observer()
    #observer.schedule(event_handler,  path=r'\\DESKTOP-DVDGK9R\Users\tordv\OneDrive\Documents\Assetto Corsa\out',  recursive=False)
    observer.schedule(event_handler,  path=r'C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\watchedfiles',  recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join

#Source:
#https://dev.to/stokry/monitor-files-for-changes-with-python-1npj
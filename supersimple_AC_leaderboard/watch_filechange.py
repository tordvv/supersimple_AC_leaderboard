import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from maincode import *

# Run commands based on what happens in the watched directory
# The comented code lines are the actual lines to be used, the code lines under them are used for testing
class  MyHandler(FileSystemEventHandler):
    def on_modified(self,  event):
        print(f'event type: {event.event_type} path : {event.src_path}')
        #if str(event.src_path) == r"...\Documents\Assetto Corsa\out\race_out.json":
        if str(event.src_path) == r"watchedfiles\testfile.json":
            print_out(event.src_path)
    def on_created(self,  event):
        print(f'event type: {event.event_type} path : {event.src_path}')
    def on_deleted(self,  event):
        print(f'event type: {event.event_type} path : {event.src_path}')

if __name__ ==  "__main__":
    event_handler = MyHandler()
    observer = Observer()
    # Using testfile.json to test the whole function. 
    # When using the testfile, the function runs 2 times for some reason,
    # but this does not happen with the actual Assetto Corsa file in my case
    observer.schedule(event_handler,  path=r'watchedfiles',  recursive=False)
    #observer.schedule(event_handler,  path=r'...\Documents\Assetto Corsa\out',  recursive=False)
    observer.start()
    
    # Stop the program with Keyboard interrupt, 
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join

# Edited from source:
# https://dev.to/stokry/monitor-files-for-changes-with-python-1npj
# By Tord Vikestad
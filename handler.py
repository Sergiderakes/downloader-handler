import os
import csv
import functions
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

dire = "D:/Descargas"

files = []

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print("1")
        dicc = functions.lector()
        functions.create_folders(dire)
        for file_n in os.listdir(dire):
            path = dire + "/" + file_n
            
            for key, value in dicc.items():
                for extension in value:
                    if extension in file_n:
                        dest = dire + "/" + key + "/" + file_n
                        os.rename(path, dest)

event_handler = MyHandler()
FileSystemEventHandler.__init__(event_handler)
observer = Observer()
observer.schedule(event_handler, path="D:/Descargas", recursive=True)
observer.start()

try:
    while True:
        print("E")
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop
observer.join()
print("Fin")
import os
import csv
import functions
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

dire = "D:/Descargas"

dicc = functions.lector()

files = []

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("1")
        for file_n in os.listdir(dire):
            path = dire + "/" + file_n
            
            for key, value in dicc:
                for extension in value:
                    if extension in file_n:
                        dest = dire + "/" + key + "/" + file_n
                        os.rename(path, dest)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path="D:/Descargas", recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
        print("E")
except KeyboardInterrupt:
    observer.stop
observer.join()
print("Fin")
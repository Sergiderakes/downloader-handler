import os
import csv
import functions
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

dire = "D:\\Descargas"

dicc = functions.lector()

files = []

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print("1")
        for file_n in os.listdir(dire):
            path = dire + "\\" + file_n
            
            for key, value in dicc:
                for extension in value:
                    if extension in file_n:
                        dest = dire + "\\" + key + "\\" + file_n
                        os.rename(path, dest)
event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, dire, recursive=True)

while True:
    time.sleep(5)
    print("e")
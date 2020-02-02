import os
import csv
import functions
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

dire = "D:/Descargas"

files = []

def check_name_in_folder(name, folder):
    if name in os.listdir(folder):
        splits = name.split(".")
        temp = splits[-2]
        splits2 = temp.split("_")
        temp2 = splits2[-1]
        try:
            splits2[-1] = str(int(temp2) + 1)
        except:
            splits2[-1] = splits2[-1] + "_1"
        
        temp = "_".join(splits2)
        splits[-2] = temp
        name = ".".join(splits)
        name = check_name_in_folder(name, folder)
        return name
    else:
        return name

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        dicc = functions.lector()
        functions.create_folders(dire)
        for file_n in os.listdir(dire):
            path = dire + "/" + file_n
            
            for key, value in dicc.items():
                for extension in value:
                    if extension in file_n.lower():
                        fold = dire + "/" + key
                        file_n = check_name_in_folder(file_n, fold)
                        dest = fold + "/" + file_n
                        os.rename(path, dest)
                        break

event_handler = MyHandler()
FileSystemEventHandler.__init__(event_handler)
observer = Observer()
observer.schedule(event_handler, dire, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop
observer.join()
print("Fin")
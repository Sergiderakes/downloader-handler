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
        dicc = functions.lector()
        functions.create_folders(dire)
        for file_n in os.listdir(dire):
            path = dire + "/" + file_n
            
            for key, value in dicc.items():
                for extension in value:
                    if extension in file_n:
                        fold = dire + "/" + key
                        # if file_n in os.listdir(fold): #Trying to not have the same name
                        #     temp = file_n.split(".")
                        #     n_temp = temp[0].split("_")
                        #     n = n_temp[1]

                        #     try:
                        #         m = int(n) + 1
                        #         temp[0] = n_temp[0] + "_" + str(m) + "."
                        #     except:
                        #         temp[0] = temp[0] + "_1."

                        #     e = "".join(temp)
                        #     file_n = e
                        dest = fold + "/" + file_n
                        os.rename(path, dest)

event_handler = MyHandler()
FileSystemEventHandler.__init__(event_handler)
observer = Observer()
observer.schedule(event_handler, path="D:/Descargas", recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop
observer.join()
print("Fin")
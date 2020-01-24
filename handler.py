import os
import csv
import functions

dire = "D:\\Descargas\\"

dicc = functions.lector()

dirs = [dire + k for k in dicc.keys()]
print(dirs)

# files = []

# for r, _, f in os.walk(dire): # r == path of file, f == files
#     for item in f:
#         if ".exe" in item:
#             files.append(os.path.join(r, item))

# print(files)
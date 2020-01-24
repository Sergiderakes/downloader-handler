import os
import csv

def lector():
    dicc = {}
    with open(os.path.join(os.path.dirname(__file__), "data.csv"), "r") as f:
        lineas = csv.reader(f)
        for linea in lineas:
            key = linea[0]
            dicc[key] = []
            for elem in linea[1:]:
                dicc[key].append(elem)
            
    return dicc

def check_extension(extension):
    dicc = lector()
    res = (False, None)
    for key in dicc:
        if extension in dicc[key]:
            res = (True, key)
            break

    return res

def genera_string(dicc):
    strn = ""
    for key in dicc:
        strn += key + ","
        for ext in dicc[key]:
            if not ext == dicc[key][-1]:
                strn += ext + ","
            else:
                strn += ext + "\n"
    return strn

def add_extension(extension, folder):
    dicc = lector()
    res, fold_ext = check_extension(extension)
    if not res:
        if folder in dicc:
            dicc[folder].append(extension)
            strn = genera_string(dicc)
            with open(os.path.join(os.path.dirname(__file__), "data.csv"), "w") as f:
                f.write(strn)
                print("La extensión " + extension + " añadida a " + folder + " correctamente")
        
        else:
            with open(os.path.join(os.path.dirname(__file__), "data.csv"), "a") as f:
                f.write(folder + "," + extension + "\n")
                print("La extensión " + extension + " añadida a " + folder + " correctamente")
    else:
        print("La extensión " + extension + " ya existe en " + fold_ext)

def delete_extension(extension):
    res, folder = check_extension(extension)
    if res:
        dicc = lector()
        dicc[folder].remove(extension)
        if dicc[folder] == []:
            dicc.pop(folder)
        strn = genera_string(dicc)
        with open(os.path.join(os.path.dirname(__file__), "data.csv"), "w") as f:
            f.write(strn)
            print("La extensión " + extension + " borrada de " + folder + " correctamente")
    else:
        print("La extensión " + extension + " no existe")
    
def move_extension(extension, folder):
    res, folder2 = check_extension(extension)
    if res:
        if not folder == folder2:
            delete_extension(extension)
            add_extension(extension, folder)
        else:
            print("La extensión " + extension + " ya se encuentra en la carpeta " + folder)

    else:
        print("La extensión " + extension + " no existe")
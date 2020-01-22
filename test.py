import functions

def test_add_function():
    print("Añadir una extensión a una carpeta que no existe: ")
    print("Salida esperada: La extensión .jpg añadida a imagenes correctamente")
    print("Salida obtenida: ", end = "")
    functions.add_extension("imagenes", ".jpg")

def test_add_function2():
    print("Añadir una extensión a una carpeta que existe: ")
    print("Salida esperada: La extensión .png añadida a imagenes correctamente")
    print("Salida obtenida: ", end = "")
    functions.add_extension("imagenes", ".png")

def test_add_function_error():
    print("Añadir una extensión que ya existe a una carpeta que existe: ")
    print("Salida esperada: La extensión .jpg ya existe en imagenes")
    print("Salida obtenida: ", end = "")
    functions.add_extension("imagenes", ".jpg")

def test_add_function_error2():
    print("Añadir una extensión que ya existe a una carpeta que no existe: ")
    print("Salida esperada: La extensión .jpg ya existe en imagenes")
    print("Salida obtenida: ", end = "")
    functions.add_extension("imagens", ".jpg")

def test_delete_function():
    print("Borrar una extensión: ")
    print("Salida esperada: La extensión .jpg borrada de imagenes correctamente")
    print("Salida obtenida: ", end = "")
    functions.delete_extension(".jpg")

def test_delete_function2():
    print("Borrar la última extensión de una carpeta (borra también la carpeta): ")
    print("Salida esperada: La extensión .png borrada de imagenes correctamente")
    print("Salida obtenida: ", end = "")
    functions.delete_extension(".png")

def test_delete_function_error():
    print("Borrar una extensión: ")
    print("Salida esperada: La extensión .jpg no existe")
    print("Salida obtenida: ", end = "")
    functions.delete_extension(".jpg")

# Hay que borrar los datos del csv antes de ejecutar las pruebas
# You must delete all the data from the csv before executing the test

print("### PRUEBAS ###")
print("----------------TEST 1: ")
test_add_function()
print("----------------TEST 2: ")
test_add_function2()
print("----------------TEST 3: ")
test_add_function_error()
print("----------------TEST 4: ")
test_add_function_error2()
print("----------------TEST 5: ")
test_delete_function()
print("----------------TEST 6: ")
test_delete_function2()
print("----------------TEST 7: ")
test_delete_function_error()
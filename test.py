import functions

def test_add_function():
    print("Añadir una extensión a una carpeta que no existe: ")
    print("Salida esperada: La extensión .jpg añadida a imagenes correctamente")
    print("Salida obtenida: ", end = "")
    functions.add_extension(".jpg", "imagenes")

def test_add_function2():
    print("Añadir una extensión a una carpeta que existe: ")
    print("Salida esperada: La extensión .png añadida a imagenes correctamente")
    print("Salida obtenida: ", end = "")
    functions.add_extension(".png", "imagenes")

def test_add_function_error():
    print("Añadir una extensión que ya existe a una carpeta que existe: ")
    print("Salida esperada: La extensión .jpg ya existe en imagenes")
    print("Salida obtenida: ", end = "")
    functions.add_extension(".jpg", "imagenes")

def test_add_function_error2():
    print("Añadir una extensión que ya existe a una carpeta que no existe: ")
    print("Salida esperada: La extensión .jpg ya existe en imagenes")
    print("Salida obtenida: ", end = "")
    functions.add_extension(".jpg", "imagens")

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

def test_move_extension():
    print("Mover extension: ")
    print("Salida esperada: La extensión .txt añadida a textos\nLa extensión .txt borrada de textos correctamente\nLa extensión .txt añadida a texts correctamente")
    print("Salida obtenida: ", end = "")
    functions.add_extension(".txt", "textos")
    functions.move_extension(".txt", "texts")

def test_move_extension_error():
    print("Mover extension: ")
    print("Salida esperada: La extensión .txt ya se encuentra en la carpeta texts\nLa extensión .txt borrada de texts correctamente")
    print("Salida obtenida: ", end = "")
    functions.move_extension(".txt", "texts")
    functions.delete_extension(".txt")

def test_move_extension_error2():
    print("Mover extension: ")
    print("Salida esperada: La extensión .txt no existe")
    print("Salida obtenida: ", end = "")
    functions.move_extension(".txt", "textos")

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
print("----------------TEST 8: ")
test_move_extension()
print("----------------TEST 9: ")
test_move_extension_error()
print("----------------TEST 10: ")
test_move_extension_error2()
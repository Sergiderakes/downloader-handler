import functions

functions.add_extension(".exe", "exe")
functions.add_extension(".msi", "exe")
functions.add_extension(".jpg", "imagenes")
functions.add_extension(".png", "imagenes")
functions.add_extension(".pdf", "documentos")
functions.add_extension(".zip", "comprimidos")
functions.add_extension(".rar", "comprimidos")
functions.add_extension(".7z", "comprimidos")
functions.add_extension(".docx", "documentos")
functions.add_extension(".pptx", "presentaciones")

e = "hola__1.txy"
temp = e.split(".")
n_temp = temp[0].split("_")
n = n_temp[1]

try:
    m = int(n) + 1
    temp[0] = n_temp[0] + "_" + str(m) + "."
except:
    temp[0] = temp[0] + "_1."

e = "".join(temp)
print(e)
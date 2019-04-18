import pickle

class Ubicacion(object):
    def __init__(self, nombre):
        self.nombre = nombre

lugar = Ubicacion('infierno')

# print(lugar.nombre)

serializado = pickle.dumps(lugar)

nombre_archivo = 'serializado'

with open(nombre_archivo, 'w') as archivo_serializado:
    archivo_serializado.write(serializado)

nombre_archivo = 'serializado.corrupto' # indisponibiliza el sistema

with open(nombre_archivo) as archivo_serializado:
    datos_serializados = archivo_serializado.read()

deserializado = pickle.loads(datos_serializados)

print(deserializado.nombre)
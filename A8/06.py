import yaml

class Ubicacion(object):
    def __init__(self, nombre):
        self.nombre = nombre

lugar = Ubicacion('infierno')

# print(lugar.nombre)

serializado = yaml.dump(lugar)

nombre_archivo = 'serializado.yaml'

with open(nombre_archivo, 'w') as archivo_serializado:
    archivo_serializado.write(serializado)

# nombre_archivo = 'serializado.corrupto' # indisponibiliza el sistema
nombre_archivo = 'serializado.malevolo.yaml' # hace ca__r el sistema

with open(nombre_archivo) as archivo_serializado:
    datos_serializados = archivo_serializado.read()

try:
    deserializado = yaml.load(datos_serializados)
    assert(isinstance(deserializado, Ubicacion))
    print(deserializado.nombre)
except:
    print('error durante la deserializacion')
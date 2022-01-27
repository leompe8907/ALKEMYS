import requests
import csv
import pathlib
import time
import os
import pandas as pd


urlDire = input("pagina ")
nombre = input("nombre")
fecha = time.strftime("%d-%m-%y")
nombreArchivo = nombre+"-"+fecha+'.csv'
# print(nombreArchivo)
## descargar una url y guardarla en el disco 
url = urlDire
file = requests.get(url)
lineas = file.text.splitlines()
leer = csv.reader(lineas)
leer = open(nombreArchivo,'wb')
leer.write(file.content)
leer.close()

# ## buscar archivo csv en carpeta en el disco 
ruta = pathlib.Path('.')
for i in ruta.glob('*.csv'):
    print(i)
    
### cambiar nombre de archivo si se repite
archivos = ruta/nombreArchivo
if archivos.exists()>1:
    name1 = str(nombreArchivo)
    archivo =ruta/name1
    name = input("nombre nuevo")
    name = str(name+'-'+fecha+'.csv')
    newname = ruta/name
    os.rename(archivos,newname)
else:
    print(i)


### modificar archivo csv con pandas


# sql =["cod_localidad",
#       "id_provincia",
#       "id_departamento",
#       "categoria",
#       "provincia",
#       "localidad",
#       "nombre",
#       "domicilio",
#       "código_postal",
#       "numero_de_telefono",
#       "mail",
#       "web"]

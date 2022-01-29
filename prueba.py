import requests
import csv
import pathlib
import time
import os
import pandas
import pandas as pd
import psycopg2

#### funcion para los links ####
def ul(link, nombre):
    url = (f"{link}")
    file = requests.get(url)
    lineas = file.text.splitlines()
    leer = csv.reader(lineas)
    leer = open(nombre,'wb')
    leer.write(file.content)
    leer.close()
    return(leer)

##Variables##
contador=0

### descargar csv y nombrar archivos ###
print("BIENVENIDOS AL PROGRAMA PARA CREAR Y ANALIZAR BASES DE DATOS APARTIR DE ARCHIVOS CSV")

archivoCsv = int(input("CUANTOS ARCHIVOS CSV VA A DESCARGAR: "))
    
if archivoCsv > 0:
    while contador < archivoCsv:
        Url = input(" por favor introduzca el link de donde se va a descargar el archivo csv: ")
        name = input (" por favor indique el nombre del archivo a guardar: ")
        fecha = time.strftime("%d-%m-%y")
        nombreArchivo = name+"-"+fecha+'.csv'
        ruta = pathlib.Path('.')
        archivos = ruta/nombreArchivo
        if archivos.exists():
            nuevoNombreArchivo =input("por favor elija otro nombre debido a que este ya existe: ")
            nombre = nuevoNombreArchivo +"-"+fecha+'.csv'
            nombreArchivo = ruta/nombre
            os.rename(archivos,nombreArchivo)
        ul(Url,nombreArchivo)
        contador+=1
    else:
        print("GRACIAS POR USAR EL PROGRAMA")


### lectura de archivos ###

    ruta = pathlib.Path('.')
    for files in ruta.glob('*.csv'):
        read =pd.read_csv(files,sep=',')
        print(read)
        
### crear tabla en postgres ###
    connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="root",
    database="postgres",
    port="5432"
)
    connection.autocommit = True

    def crearTabla():
        cursor = connection.cursor()
        query = "CREATE TABLE alkemy(cod_localidad varchar(60),id_provincia varchar(60),id_departamento varchar(60),categoria varchar(60),provincia varchar(60),localidad varchar(60),nombre varchar(60),domicilio varchar(60),código_postal varchar(60),numero_de_telefono varchar(60),mail varchar(60),web varchar(60))"
        try:
            cursor.execute(query)
        except:
            print("ya esta")
        cursor.close

    crearTabla()   
        
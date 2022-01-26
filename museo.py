import requests
import sqlite3
import csv


# descargar una url y guardarla en el disco 
urlMuseo = (r"https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv")
file_museo = requests.get(urlMuseo)
open("museo.csv","wb").write(file_museo.content)

#leer el archivo csv
fileName = "museo.csv"
f = open(fileName,"r",errors="ignore")
next(f,None)
read = csv.reader(f, delimiter = ',')


#crear base de datos
conexion = sqlite3.connect("museo.sql")
consulta = conexion.cursor()
sql ="""CREATE TABLE IF NOT EXISTS alkemy(cod_localidad int,id_provincia int,id_departamento int,categoria txt,provincia txt,localidad txt,nombre txt,domicilio txt,código_postal int,numero_de_telefono int, mail txt, web txt)"""
if(consulta.execute(sql)):
    print("tabla creada con éxito")
else:
    print("se produjo un error")

#ingresar info a la bd
for row in read:
    consulta.execute("INSERT INTO alkemy VALUES(?,?,?,?,?,?,?,?,?,?,?,?)" , (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],))
    
    
consulta.close()
conexion.commit()
conexion.close()
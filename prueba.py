import requests

#### funcion para los links ####
def ul(link):
    url = (f"{link}")
    file = requests.get(url)
    archivo = open(f"{nombreArchivo}.csv","wb").write(file.content)
    return(archivo)

##Variables##
contador=0
   
print("BIENVENIDOS AL PROGRAMA PARA CREAR Y ANALIZAR BASES DE DATOS APARTIR DE ARCHIVOS CSV")
archivoCsv = int(input("CUANTOS ARCHIVOS CSV VA A DESCARGAR: "))
if archivoCsv > 0:
    while contador < archivoCsv:
        Url = input(" por favor introduzca el link de donde se va a descargar el archivo csv: ")
        nombreArchivo = input (" por favor indique el nombre del archivo a guardar: ")
        print(ul(Url))
        contador+=1
else:
    print("GRACIAS POR USAR EL PROGRAMA")
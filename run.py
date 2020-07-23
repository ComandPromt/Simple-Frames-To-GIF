import imageio

import os

import os.path

carpeta="/home/username/"

lista_de_archivos = os.listdir(carpeta)

separador="/";

if "\\" in carpeta:
	separador="\\";

ruta = os.path.join(carpeta,"output") 

if not(os.path.exists(ruta)): 

	os.mkdir(ruta) 

imagenes=[]

for file in lista_de_archivos:
	
    if file[-4:]==".jpg" or file[-4:]==".png" or file[-4:]==".gif":
        imagenes.append(file)

imagenes=sorted(imagenes)

longitud=len(imagenes)

longitud=longitud-1

with imageio.get_writer(carpeta+"output"+separador+"loop.gif", mode='I') as writer:
	
	for i in range(0, longitud):
		image = imageio.imread(os.path.join(carpeta, imagenes[i]))
		writer.append_data(image)
        
	for i in range(longitud, 0, -1):
		image = imageio.imread(os.path.join(carpeta, imagenes[i]))
		writer.append_data(image)

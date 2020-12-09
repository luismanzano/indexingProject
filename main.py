import math 
import random 
from Pelicula import Pelicula
from Registro import Registro

inventario = []
indice = []

def eliminarPelicula():
    print("Ingrese la pelicula que desea eliminar")
    codigo = input()
    codigo = int(codigo)
    r = len(indice) - 1
    pelicula = binarySearch(indice, 0, r, codigo)
    print("CODIGO: " + str(pelicula.codigo))
    print("TITULO: " + pelicula.titulo)
    print("ALQUILER: " + pelicula.alquiler)
    print("SOCIO: " + pelicula.socio)
    print("EXISTE: " + str(pelicula.existe))
    print("////////////////////////////")
    pelicula.existe = False
    print("CODIGO: " + str(pelicula.codigo))
    print("TITULO: " + pelicula.titulo)
    print("ALQUILER: " + pelicula.alquiler)
    print("SOCIO: " + pelicula.socio)
    print("EXISTE: " + str(pelicula.existe))

    

def retornarPelicula(index):
    pelicula = inventario[index]
    print("CODIGO: " + str(pelicula.codigo))
    print("TITULO: " + pelicula.titulo)
    print("ALQUILER: " + pelicula.alquiler)
    print("SOCIO: " + pelicula.socio)
    return pelicula

#BUSQUEDA BINARIA
def binarySearch (arr, l, r, codigo): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid].codigo == codigo: 
            print("Encontrado")
            print(arr[mid].codigo)
            return retornarPelicula(arr[mid].indice)
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid].codigo > codigo: 
            print("buscando abajo")
            return binarySearch(arr, l, mid-1, codigo) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            print("buscando arriba")
            return binarySearch(arr, mid + 1, r, codigo) 
  
    else: 
        # Element is not present in the array 
        return "El elemento no existe"
  


def buscarPelicula():
    print("ingrese el codigo de la pelicula que desea buscar")
    codigo = input()
    codigo = int(codigo)
    r = len(indice) - 1
    binarySearch(indice, 0, r, codigo)
    print("Volviendo a la interfaz")


#FUNCION QUE ORDENA EL INDICE 
def ordenarIndice():
    if len(indice) == 0:
        return
    
    else:
        n = len(indice) 
  
        # Traverse through all array elements 
        for i in range(n): 
  
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
  
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if indice[j].codigo > indice[j+1].codigo : 
                    indice[j], indice[j+1] = indice[j+1], indice[j] 

    for x in indice:
        print("----------------------")
        print("CODIGO " + str(x.codigo))
        print("INDICE " + str(x.indice))
        

#FIN DEL ORDENAR DEL INDICE

#FUNCION QUE ANADE LA PELICULA
def anadirPelicula():
    print("CODIGO")
    codigo = input()
    codigo = int(codigo)
    print("TITULO")
    titulo = input()
    print("COSTO ALQUILER")
    alquiler = input()
    print("SOCIO")
    socio = input()

    pelicula = Pelicula(codigo, titulo, alquiler, socio)
    inventario.append(pelicula)

    registro = Registro(len(inventario)-1, pelicula.codigo, True)
    indice.append(registro)

    index = len(inventario)
    print("LEN DEL INVENTARIO " + str(index))

    ordenarIndice()
#FIN DEL ANADIR PELICULAS 

def guardarDisco():
    file= open("peliculas.txt","w+")
    
    for pelicula in inventario:
        file.write(str(pelicula.codigo))
        file.write("\n")
        file.write(pelicula.titulo)
        file.write("\n")
        file.write(pelicula.socio)
        file.write("\n")
        file.write(pelicula.alquiler)
        file.write("\n")
        file.write("////////////////")

starter = True


while starter == True:
    print("Bienvenido a Peliculas Doble LL")
    print("\n 1 - AÑADIR PELICULA")
    print("\n 2 - BUSCAR PELICULA POR INDICE")
    print("\n 3 - BUSCAR PELICULA POR NOMBRE")
    print("\n 4 - GUARDAR AL DISCO")
    print("\n 9 - SALIR DEL PROGRAMA")
    option = input()
    print(option)



    if option == '1':
        anadirPelicula()

    elif option =='2':
        buscarPelicula()

    elif option =='3':
        eliminarPelicula()

    elif option =='4':
        guardarDisco()

    elif option =='5':
        eliminarPelicula()
        


    elif option == '9':
        print("Adios!")
        starter = False



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


def alquilarPelicula():
    print("Ingrese el indice de la pelicula que desea agregar")
    codigo = input()
    codigo = int(codigo)
    r = len(indice) - 1
    pelicula = binarySearch(indice, 0, r, codigo)
    if pelicula.alquilada == True:
        print("Esta pelicula ya esta alquilada")

    else:
        print("Ingrese su numero de socio")
        socio = input()
        socio = int(socio)
        pelicula.socio = socio
        print("CODIGO: " + str(pelicula.codigo))
        print("TITULO: " + pelicula.titulo)
        print("ALQUILER: " + pelicula.alquiler)
        print("SOCIO: " + pelicula.socio)
        print("EXISTE: " + str(pelicula.existe))


def devolverPelicula():
    print("Ingrese el indice de la pelicula que desea devolver")
    codigo = input()
    codigo = int(codigo)
    r = len(indice) - 1
    pelicula = binarySearch(indice, 0, r, codigo)
    
    if pelicula.alquilada == False:
        print("Esta pelicula esta en stock, no se puede devolver si no la tiene jejejeje")

    else:
        pelicula.alquilada = False
        pelicula.socio = 00000
        print("CODIGO: " + str(pelicula.codigo))
        print("TITULO: " + pelicula.titulo)
        print("ALQUILER: " + pelicula.alquiler)
        print("SOCIO: " + pelicula.socio)
        print("EXISTE: " + str(pelicula.existe))

    

def retornarPelicula(index):
    pelicula = inventario[index]
    if pelicula.existe == False:
        print("La pelicula no se encuentra disponible (eliminada logicamente)")
    else:
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
    file = open("peliculas.txt","w+")
    
    for pelicula in inventario:
        file.write(str("codigo\n"))
        file.write(str(pelicula.codigo))
        file.write("\n")
        file.write("titulo\n")
        file.write(str(pelicula.titulo))
        file.write("\n")
        file.write("socio\n")
        file.write(str(pelicula.socio))
        file.write("\n")
        file.write("alquiler\n")
        file.write(str(pelicula.alquiler))
        file.write("\n")
        file.write("////////////////\n")
    file.close()

def leerDisco():
    peliculas = len(inventario)

    file = open("peliculas.txt", "r")
    data = []
    codigo = ""
    titulo = ""
    alquiler = ""
    socio = ""
    existe = ""
    alquilada = ""
    
    for x in file:
        data.append(x)

    for i in range(len(data)):
        if data[i] == "codigo\n":
            codigo = data[i+1]
            codigo = codigo[:-1]

        elif data[i] == "titulo\n":
            titulo = data[i+1]
            titulo = titulo[:-1]

        elif data[i] == "alquiler\n":
            alquiler = data[i+1]

        elif data[i] == "socio\n":
            socio = data[i+1]
            socio = socio[:-1]

        elif data[i] == "existe\n":
            existe = data[i+1]

        elif data[i] == "alquilada\n":
            alquilada = data[i+1]

        elif data[i] == "////////////////\n":
            pelicula = Pelicula(codigo, titulo, alquiler, socio)
            inventario.append(pelicula)

            registro = Registro(len(inventario)-1, pelicula.codigo, True)
            indice.append(registro)

            index = len(inventario)
            print("LEN DEL INVENTARIO " + str(index))

            ordenarIndice()
        else:
            continue


    

starter = True


while starter == True:
    print("Bienvenido a Peliculas Doble LL")
    print("\n 1 - AÑADIR PELICULA")
    print("\n 2 - BUSCAR PELICULA POR INDICE")
    print("\n 3 - BUSCAR PELICULA POR NOMBRE")
    print("\n 4 - GUARDAR AL DISCO")
    print("\n 5 - ELIMINAR PELICULA (logicamente)")
    print("\n 6 - ALQUILAR PELICULA")
    print("\n 7 - DEVOLVER PELICULA")
    print("\n 8 - CARGAR DEL DISCO")
    print("\n 9 - BUSCAR POR PALABRA")
    print("\n 10 - SALIR DEL PROGRAMA")
    print("\n 11 - LISTAR LAS PELICULAS")
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
    
    elif option =='6':
        alquilarPelicula()

    elif option =='7':
        devolverPelicula()

    elif option =='8':
        leerDisco()

    elif option =='9':
        pass

    elif option == '10':
        print("Adios!")
        starter = False

    elif option =='11':
        for pelicula in inventario:
            print(pelicula.titulo)
            print(pelicula.codigo)
            print(pelicula.alquilada)
            print(pelicula.socio)
            print(pelicula.existe)



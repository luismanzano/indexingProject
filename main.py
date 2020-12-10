import math 
import random 
from Pelicula import Pelicula
from Registro import Registro
from Palabra import Palabra

inventario = []
indice = []
diccionario = []
indicePalabras = []

def eliminarPelicula():
    print("Ingrese la pelicula que desea eliminar")
    codigo = input()
    codigo = int(codigo)
    r = len(indice) - 1
    pelicula = binarySearch(indice, 0, r, codigo)
    print("////////////////////////////")
    pelicula.existe = False
    print("La pelicula: " + pelicula.titulo + " se ha eliminado logicamente")


def alquilarPelicula():
    print("Ingrese el indice de la pelicula que desea alquilar")
    codigo = input()
    codigo = int(codigo)
    r = len(indice) - 1
    pelicula = binarySearch(indice, 0, r, codigo)
    if pelicula.alquilada == True:
        print("Esta pelicula ya esta alquilada")

    else:
        pelicula.alquilada = True
        print("Ingrese su numero de socio")
        socio = input()
        socio = int(socio)
        pelicula.socio = socio
        print("CODIGO: " + str(pelicula.codigo))
        print("TITULO: " + pelicula.titulo)
        print("ALQUILER: " + str(pelicula.alquiler))
        print("SOCIO: " + str(pelicula.socio))
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
        print("ALQUILER: " + str(pelicula.alquiler))
        print("SOCIO: " + str(pelicula.socio))
        print("EXISTE: " + str(pelicula.existe))

    

def retornarPelicula(index):
    pelicula = inventario[index]
    if pelicula.existe == False:
        print("La pelicula no se encuentra disponible (eliminada logicamente)")
    else:
        print("-------------------------")
        print("LA PELICULA SELECCIONADA ES:")
        print("CODIGO: " + str(pelicula.codigo))
        print("TITULO: " + pelicula.titulo)
        print("ALQUILER: " + str(pelicula.alquiler))
        print("ALQUILADA: " + str(pelicula.alquilada))
    return pelicula

#BUSQUEDA BINARIA
def binarySearch (arr, l, r, codigo): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid].codigo == codigo: 
            print("Encontrado")
            #print(arr[mid].codigo)
            return retornarPelicula(arr[mid].indice)
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid].codigo > codigo: 
            #print("buscando abajo")
            return binarySearch(arr, l, mid-1, codigo) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            #print("buscando arriba")
            return binarySearch(arr, mid + 1, r, codigo) 
  
    else: 
        # Element is not present in the array 
        return "El elemento no existe"


def retornarPalabra(index, option):
    palabra = diccionario[index]

    if option == True:
        for codigo in palabra.codigos:
            #print("BUSCANDO LA PELICULA POR PALABRA")
            r = len(indice) - 1
            binarySearch(indice, 0, r, codigo)
            #print("Volviendo a la interfaz")
    else:
        diccionario[index].codigos.append(option)



def binarySearchPalabra (arr, l, r, codigo, option): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid].codigo == codigo: 
            #print("Encontrado...")
            #print(arr[mid].codigo)
            return retornarPalabra(arr[mid].indice, option)
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid].codigo > codigo: 
            return binarySearchPalabra(arr, l, mid-1, codigo, option) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearchPalabra(arr, mid + 1, r, codigo, option) 
  
    else: 
        # Element is not present in the array 
        print("La palabra que busca no existe")
        return False

  


def buscarPelicula():
    print("ingrese el codigo de la pelicula que desea buscar")
    codigo = input()
    codigo = int(codigo)
    r = len(indice) - 1
    binarySearch(indice, 0, r, codigo)
    #print("EEREQUERO")


#FUNCION QUE ORDENA EL INDICE 
def ordenarIndice(indice):
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

    # for x in indice:
    #     print("----------------------")
    #     print("CODIGO " + str(x.codigo))
    #     print("INDICE " + str(x.indice))
        

#FIN DEL ORDENAR DEL INDICE

#METODO PARA EL INDICE DE LAS PALABRAS 
def codigoPalabra(textos, codigoPelicula):
    texto = textos + " "
    text2 = [char for char in texto]
    # for cha in text2:
    #     print("cha "+cha)
    text = ""
    for cha in text2:
        if cha == " ":
            # print("CHA2 "+cha)
            # print("la palabra "+text)
            valores = [ord(caracter) for caracter in text]
            total = 0
            for i in range(len(valores)):
                total += (valores[i]*(i+1))
            #VEMOS SI LA PALABRA YA EXISTE
            r = len(indicePalabras) - 1    
            codicional = binarySearchPalabra(indicePalabras, 0, r, total, codigoPelicula)
            if codicional == False:
                palabra = Palabra(text, total, codigoPelicula)
                diccionario.append(palabra)
                registro = Registro(len(diccionario)-1, palabra.valor, True)
                indicePalabras.append(registro)
                ordenarIndice(indicePalabras)
                text = ""
 
        else:
            text += cha
    # for element in diccionario:
    #     print("palabra " + element.texto)
    #     print("valor " + str(element.valor))
    #     print("-------------------------")

    # print("//////////////////////////")    
    ordenarIndice(indicePalabras)
    # for element in indicePalabras:
    #     print("palabraIndice " + str(element.indice))
    #     print("palabraValor " + str(element.codigo))
#FIN DEL METODO DEL INDICE DE LAS PALABRAS
    


#FUNCION QUE ANADE LA PELICULA
def anadirPelicula():

    while True:
        try:
            print("CODIGO")
            codigo = input()
            if len(codigo)-1 > 4:
                raise Exception("Sorry, no numbers below zero")
            else:
                codigo = int(codigo)
                break
        except:
            print("Solo se aceptan hasta 5 digitos en el codigo")

    while True:
        try:
            print("TITULO")
            titulo = input()
            if len(titulo)-1 > 29:
                raise Exception("Sorry, no numbers below zero")
            else:
                break
        except:
            print("Solo se aceptan hasta 30 caracteres en el titulo")


    while True:
        try:
            print("COSTO DEL ALQUILER")
            alquiler = input()
            if len(alquiler)-1 > 7:
                raise Exception("Sorry, no numbers below zero")
            else:
                alquiler = int(alquiler)
                break
        except:
            print("Solo se aceptan hasta 8 digitos en el costo del alquiler")



    while True:
        try:
            print("SOCIO")
            socio = input()
            if len(socio)-1 > 7:
                raise Exception("Sorry, no numbers below zero")
            else:
                socio = int(socio)
                break
        except:
            print("Solo se aceptan hasta 8 digitos en el numero de socio")


    pelicula = Pelicula(codigo, titulo, alquiler, socio)
    codigoPalabra(pelicula.titulo, pelicula.codigo)
    inventario.append(pelicula)

    registro = Registro(len(inventario)-1, pelicula.codigo, True)
    indice.append(registro)

    index = len(inventario)
    print("LEN DEL INVENTARIO " + str(index))

    ordenarIndice(indice)
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

def addPelicula(codigo, titulo, alquiler, socio, existe, alquilada):
    pelicula = Pelicula(codigo,titulo, alquiler, socio)
    pelicula.alquilada = alquilada
    inventario.append(pelicula)
    registro = Registro(len(inventario)-1, pelicula.codigo, True)
    indice.append(registro)
    ordenarIndice(indice)


def reindexar():
    print("Reindexando.......")
    #Eliminamos del arreglo inventario (que seria la db con todos los datos)
    for i in range(len(inventario)-1):
        if inventario[i].existe == False:
            inventario.pop(i)
        else:
            continue
    global indice 
    indice = []

    for i in range(len(inventario)):
        pelicula = inventario[i]
        registro = Registro(i, pelicula.codigo, True)
        indice.append(registro)
    ordenarIndice(indice)



    



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
            codigo = int(codigo)

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
            
            codigoPalabra(pelicula.titulo, pelicula.codigo)

            index = len(inventario)
            # print("LEN DEL INVENTARIO " + str(index))

            ordenarIndice(indice)
        else:
            continue


def buscarNombre(palabra, option):
    valores = [ord(caracter) for caracter in palabra]
    total = 0
    for i in range(len(valores)):
        total += (valores[i]*(i+1))
    r = len(indicePalabras) - 1
    binarySearchPalabra(indicePalabras, 0, r, total, option)
    print("Volviendo a la interfaz")

    

    

starter = True


if __name__ == "__main__":
    leerDisco()
    print("\n\n\n\n\n\n\n\n")
    print("Bienvenido a Peliculas Doble LL\n")
    while starter == True:
        print("\nIngresa la opcion que desea ejecutar")
        print("\n 1 - AÑADIR PELICULA   2 - BUSCAR PELICULA POR INDICE   3 - BUSCAR PELICULA POR NOMBRE")
        print("\n 4 - GUARDAR AL DISCO   5 - ELIMINAR PELICULA (logicamente)   6 - ALQUILAR PELICULA")
        print("\n 7 - DEVOLVER PELICULA   8 - CARGAR DEL DISCO   9 - REINDEXAR")
        print("\n 10 - SALIR DEL PROGRAMA   11 - LISTAR LAS PELICULAS\n")
        option = input()
        # print(option)



        if option == '1':
            anadirPelicula()

        elif option =='2':
            buscarPelicula()

        elif option =='3':
            print("Ingrese la palabra que desea buscar")
            nombre = input()
            buscarNombre(nombre, True)

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
            reindexar()

        elif option == '10':
            #GUARDANDO AUTOMATICAMENTE EN DISCO
            reindexar()
            guardarDisco()
            print("Su nuevos datos han sido guardados al disco")
            print("Adios!")
            starter = False

        elif option =='11':
            for pelicula in inventario:
                print(pelicula.titulo)
                print(pelicula.codigo)
                print(pelicula.alquilada)
                print(pelicula.socio)
                print(pelicula.existe)

            for x in indice:
                print("----------------------")
                print("CODIGO " + str(x.codigo))
                print("INDICE " + str(x.indice))

            print("FINNNNNNNNNNNNNNN")



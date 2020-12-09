import math 
import random 
from Pelicula import Pelicula
from Registro import Registro
from Palabra import Palabra

diccionario = []
indicePalabras = []

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

    for x in indice:
        print("----------------------")
        print("CODIGO " + str(x.codigo))
        print("INDICE " + str(x.indice))
        

def codigoPalabra(textos):
    texto = textos + " "
    text2 = [char for char in texto]
    for cha in text2:
        print("cha "+cha)
    text = ""
    for cha in text2:
        if cha == " ":
            print("CHA2 "+cha)
            print("la palabra "+text)
            valores = [ord(caracter) for caracter in text]
            total = 0
            for i in range(len(valores)):
                total += (valores[i]*(i+1))
            palabra = Palabra(text, total)
            diccionario.append(palabra)
            registro = Registro(len(diccionario)-1, palabra.valor, True)
            indicePalabras.append(registro)
            ordenarIndice(indicePalabras)
            text = ""
        else:
            text += cha
    for element in diccionario:
        print("palabra " + element.texto)
        print("valor " + str(element.valor))
        print("-------------------------")

    print("//////////////////////////")    
    
    for element in indicePalabras:
        print("palabraIndice " + str(element.indice))
        print("palabraValor " + str(element.codigo))


texto = input()
codigoPalabra(texto)

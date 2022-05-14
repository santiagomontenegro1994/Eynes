from asyncio.windows_events import NULL
from itertools import count
from pickle import TRUE
import random
import numpy as np


matriz= 2 * np.random.random([5,5]) #Creo la matriz de 5 x 5 con numero aleatoreos(lo multiplico x 100 por que por defecto genera numeros entre 0 y 1)
matriz= matriz.astype(int) #convierto el contenido de la matriz en numeros enteros
print(matriz) #hago un print de la matriz



#------------------------------------EMPIEZO CON EL METODO-------------------------



def sec4Numeros(matriz): # metodo para encontrar secuencias de 4 o mas numeros iguales
    
    respuesta='sin secuencia'
    posicionInicial=NULL
    posicionFinal=NULL
    j=0 #auxiliar para saber el indice de la matriz 
    k=0 #auxiliar para saber si ya hubo una secuencia 
     
    for c in range(len(matriz[1,:])): #recorro cada una de las columnas de la matriz
               
        tuplaAux=np.unique(matriz[:,c], return_counts=True, return_index=True)
        #con la columna que recorre, creo una tupla que contiene 3 listas
        #l primera tiene los elementos, la segunda contiene el indice donde se ubica, la tercera tiene la cantidad de veces que se repite.
        
        i=0 #auxiliar para saber el subindice de la matriz
        j=j+1
        
                  
        for x in tuplaAux[2]: #recorro la lista de cantidad de veces que se repite un elemento
            i=i+1
            
            if (x>3) and ((matriz[1,c])==tuplaAux[0][i-1]) and ((matriz[2,c])==tuplaAux[0][i-1]) and ((matriz[3,c])==tuplaAux[0][i-1]):
                # si hay algun elemento que se repite es mas de 3 
                # y que no tenga otro elemento en medio de la columna para corroborar que es secuencia
                if k<1:  
                    posicionInicial= str(tuplaAux[1][i-1]) + ' ' + str(j-1)
                    posicionFinal=str(tuplaAux[1][i-1] + x-1) + ' ' + str(j-1)
                    k=k+1 #Cambio auxiliar para saber que ya se encontro una secuencia
                    respuesta='Secuencia encontrada en posiciones: \n' + posicionInicial + ' , ' + posicionFinal    
                else:
                    posicionInicial= str(tuplaAux[1][i-1]) + ' ' + str(j-1)
                    posicionFinal=str(tuplaAux[1][i-1] + x-1) + ' ' + str(j-1)
                    respuesta= respuesta + '\n' + posicionInicial + ' , ' + posicionFinal
                    
                    
#-------------------ahora hago lo mismo para revisar cada fila de la matriz---------------------# 

               
    #primero reseteo el contador
    j=0 #auxiliar para saber el indice de la matriz 
    
    for l in range(len(matriz[:,1])): #recorro cada una de las listas de la matriz
               
        tuplaAux=np.unique(matriz[l,:], return_counts=True, return_index=True)
        #con la lista que recorre, creo una tupla que contiene 3 listas
        #la primera tiene los elementos, la segunda contiene el indice donde se ubica, la tercera tiene la cantidad de veces que se repite.
        
        i=0 #auxiliar para saber el subindice de la matriz
        j=j+1
        
                  
        for x in tuplaAux[2]: #recorro la lista de cantidad de veces que se repite un elemento
            i=i+1
            
            if (x>3) and ((matriz[l,1])==tuplaAux[0][i-1]) and ((matriz[l,2])==tuplaAux[0][i-1]) and ((matriz[l,3])==tuplaAux[0][i-1]):
                # si hay algun elemento que se repite es mas de 3 
                # y que no tenga otro elemento en medio de la lista para corroborar que es secuencia
                if k<1:  
                    posicionInicial= str(j-1) + ' ' + str(tuplaAux[1][i-1])
                    posicionFinal=str(j-1) + ' ' + str(tuplaAux[1][i-1] + x-1)  

                    k=k+1 #Cambio auxiliar para saber que ya se encontro una secuencia
                    respuesta='Secuencia encontrada en posiciones: \n' + posicionInicial + ' , ' + posicionFinal    
                else:
                    posicionInicial= str(j-1) + ' ' + str(tuplaAux[1][i-1])
                    posicionFinal=str(j-1) + ' ' + str(tuplaAux[1][i-1] + x-1)

                    respuesta= respuesta + '\n' + posicionInicial + ' , ' + posicionFinal
    
    

    
    
    
    return print(respuesta) 

    
                
print(sec4Numeros(matriz))    #hago un print del metodo pasandole por parametro la matriz     
    
              
        
        
                
             
            
        
            
        
       
        
    
        
    
        
        
    
    


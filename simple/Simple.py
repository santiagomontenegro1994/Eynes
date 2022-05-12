from ast import Lambda
import random
lista =[]
def listDiccionarios():
    i = 0
    while i < 10 :
        
        lista.append({'id':i,'edad':random.randint(1, 100)})
        i=i+1
    
    return lista    

      
def ordenarLista(lista):
    lista = sorted(lista, key=lambda p: p['edad'])
    return lista
 
print(listDiccionarios())
print(ordenarLista(lista))        

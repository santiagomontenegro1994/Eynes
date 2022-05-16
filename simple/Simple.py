from ast import Lambda
import random
from xml.dom.minidom import Element
lista =[]
def listDiccionarios():
    i = 0
    while i < 10 :
        
        lista.append({'id':i,'edad':random.randint(1, 100)})
        i=i+1
    
    return lista    

      
def ordenarLista(lista):
    lista = sorted(lista, key=lambda p: p['edad'])
    res = [ lista[0], lista[-1] ]
    
    print("los id de la persona mas joven y mas vieja son" + str(res))
    return lista

listDiccionarios()
ordenarLista(lista)      

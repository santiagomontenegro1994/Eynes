import random
lista =[]
def listDiccionarios():
    i = 0
    while i < 10 :
        
        lista.append({'id':i,'edad':random.randint(1, 100)})
        i=i+1
        
listDiccionarios()
print(lista)        
        

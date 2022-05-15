class Circulo:
    
    def __init__(self, radio):
        if radio>0:
            self.radio = radio
        else:    
            print("No se puede crear un circulo con radio menor o igual a cero \n Por favor ingrese otro valor...")
          
    
    def area(self):
        radio2=self.radio*self.radio
        area = 3.14 * radio2
        print("el area del circulo es: " + str(area))
        
         
    def perimetro(self):
        perim= 2 * 3.14 * self.radio
        print("el perimetro del circulo es: " + str(perim))              
    
        
mi = Circulo(5)
print(mi.area())
print(mi.perimetro())
                    
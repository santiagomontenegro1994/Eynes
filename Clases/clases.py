import turtle


class Circulo: # Defino la clase Circulo
    
    def __init__(self, radio): # Defino su constructor
        if radio>0:            # Verifico que el radio sea mayor a cero, si no es asi printeo el mensaje de error 
            self.radio = radio
        else:    
            print("No se puede crear un circulo con radio menor o igual a cero \n Por favor ingrese otro valor...")
          
    def __str__(self): # metodo para printear el objeto
        turtle.penup()
        turtle.goto(0,-self.radio) #muevo donde empieza el dibujo para centrarlo en la pantalla
        turtle.pendown()
        turtle.color("blue") # pintamos el circulo azul
        return(turtle.circle(self.radio,360))#imprimo el circulo como salida, pasandole el radio como parametro
    
    def set_Radio(self, radio): # Metodo set
        if radio>0:         # Verifico que el radio sea mayor a cero, si no es asi printeo el mensaje de error 
            self.radio = radio
        else:    
            print("No se puede modificar un circulo con radio menor o igual a cero \n Por favor ingrese otro valor...")    
    
        
    def area(self):
        radio2=self.radio*self.radio
        area = 3.14 * radio2
        print("el area del circulo es: " + str(area))
        
         
    def perimetro(self):
        perim= 2 * 3.14 * self.radio
        print("el perimetro del circulo es: " + str(perim))   
        
        
    def __mul__(self, num): # metodo para multiplicar 
        if(num>0):
            radio=self.radio*num
            return Circulo(radio)
        else:
            return(print("no se puede multiplicar un circulo por un numero menor o igual a cero"))
                            
    
        

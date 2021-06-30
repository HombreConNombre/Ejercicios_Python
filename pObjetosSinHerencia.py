import math

class Punto:
    #Constructor
    def __init__ (self, x=0,y=0):
        self.x=x
        self.y=y
    #Salid String
    def __str__(self):
        return "Las coordenadas del punto son: {} , {}".format(self.x,self.y)
    #Función para a que cuadrante pertenece
    def cuadrante(self):
        if self.x>0 :
            if self.y>0:
                return "Este punto está en el cuadrante superior derecho"
            elif self.y<0:
                return "Este punto está en el cuadrante inferior derecho"
            else:
                return "Este punto está en la mitad derecha"
        elif self.x<0:
            if self.y>0:
                return "Este punto está en el cuadrante superior izquierdo"
            elif self.y<0:
                return "Este punto está en el cuadrante inferior derecho"
            else:
                return "Este punto está en la mitad izquierda"
        else:
            return "Este punto está en el punto central {} , {}".format(self.x,self.y)
    #Función para calcular el vector entre dos puntos
    def vector(self,punto2):
        xVector=punto2.x-self.x
        yVector=punto2.y-self.y
        return xVector,yVector 
    #Función para calcular la distancia entre dos puntos
    def distancia(self,punto2):
        xVector=punto2.x,self.x
        yVector=punto2.x,self.x
        d=math.sqrt(math.pow(xVector,2)+math.pow(yVector,2))
        return d

class Rectangulo:

    #Constructor
    def __init__(self, punto1=Punto(0,0),punto2=Punto(0,0)):
        self.punto1=punto1
        self.punto2=punto2
    #String
    def __str__(self):
        return "{} y {}".format(self.punto1,self.punto2)
    #Calcular BASE  
    def base(self):
        vector=self.punto1.vector(self.punto2)
        return abs(vector[0])
    #Calcular ALTURA  
    def altura(self):
        vector=self.punto1.vector(self.punto2)
        return abs(vector[1])
    #Calcular AREA
    def area(self):
        base=self.base()
        altura=self.altura()
        area=base*altura
        return area


p1=Punto(10,10)
p2=Punto(5,5)
vectorp1=p1.vector(p2)
print("El vector es: {} , {}".format(vectorp1[0],vectorp1[1]))
r1=Rectangulo(p1,p2)
print(r1.base())
r2=Rectangulo()
print(str(r2))
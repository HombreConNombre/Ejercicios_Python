class Vehiculos:
    #Constructor
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    #String
    def __str__(self):
        return "color {} . {} ruedas".format(self.color,self.ruedas)
    
class Coche(Vehiculos):
    #Constructor
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas) #llamada constructor padre
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    #String
    def __str__(self):
        return super().__str__()," , {} km/h , {} CC".format(self.velocidad,self.cilindrada)

class Camioneta(Coche):
    #Constructor
    def __init__(self,color,ruedas,velocidad,cilindrada, carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga=carga
    #String
    def __str__(self):
        return super().__str__()," {} KG de carga".format(self.carga)

class Bicicleta(Vehiculos):
    #Constructor
    def __init__(self, color, ruedas, carretera):
        super().__init__(color,ruedas)
        self.carretera=carretera
    #STRING
    def __str__(self):
        if self.carretera==True:
            return super().__str__()," esta bici es de carretera"
        else:
            return super().__str__()," esta bici es de monte"

Vehiculos=[
    Coche("azul",4,120,1200),
    Camioneta("rojo",6,90,1600,800),
    Bicicleta("blanca",2,True)
]

def Catalogar(lista, ruedas=None):
    for x in Vehiculos:
        if ruedas==None:
            print(x.__str__())
        else:
            if ruedas==x.ruedas:
                print(x.__str__())


Catalogar(Vehiculos,6)
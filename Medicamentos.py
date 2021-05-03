#PARA NO PERDER LA REFERENCIA A JAVA USAMOS CLASES
class Medicamentos:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,nombremed,preciomed,descripcionmed,cantidadmed):
        self.nombremed = nombremed
        self.preciomed = preciomed
        self.descripcionmed= descripcionmed
        self.cantidadmed = cantidadmed


    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombremed(self):
        return self.nombremed
    
    def getPreciomed(self):
        return self.preciomed
    
    def getDescripcionmed(self):
        return self.descripcionmed

    def getCantidadmed(self):
        return self.cantidadmed



    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombremed(self, nombremed):
        self.nombremed = nombremed
    
    def setPreciomed(self, preciomed):
        self.preciomed = preciomed
    
    def setDescripcionmed(self, descripcionmed):
        self.descripcionmed = descripcionmed

    def setCantidadmed(self, cantidadmed):
        self.cantidadmed = cantidadmed

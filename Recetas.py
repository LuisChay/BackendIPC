class Recetas:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,fechareceta,pacientereceta,padecimientoreceta,descripcionrec):
        self.fechareceta = fechareceta
        self.pacientereceta = pacientereceta
        self.padecimientoreceta = padecimientoreceta
        self.descripcionrec = descripcionrec


    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getFechareceta(self):
        return self.fechareceta
      
    def getPacientereceta(self):
        return self.pacientereceta
    
    def getPadecimientoreceta(self):
        return self.padecimientoreceta

    def getDescripcionreceta(self):
        return self.descripcionrec

    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setFechareceta(self, fechareceta):
        self.fechareceta = fechareceta
    
    def setPacientereceta(self, pacientereceta):
        self.pacientereceta = pacientereceta
    
    def setPadecimientoreceta(self, padecimientoreceta):
        self.padecimientoreceta = padecimientoreceta

    def setDescripcionreceta(self, descripcionrec):
        self.descripcionrec = descripcionrec


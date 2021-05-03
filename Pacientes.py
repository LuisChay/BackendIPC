class Pacientes:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,nombrepac,apellidopac,fechapac,sexopac,usuariopac,contrapac,telefonopac):
        self.nombrepac = nombrepac
        self.apellidopac = apellidopac
        self.fechapac = fechapac
        self.sexopac = sexopac
        self.usuariopac = usuariopac
        self.contrapac = contrapac
        self.telefonopac = telefonopac

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombrepac(self):
        return self.nombrepac
    
    def getApellidopac(self):
        return self.apellidopac
    
    def getFechapac(self):
        return self.fechapac

    def getSexopac(self):
        return self.sexopac

    def getUsuariopac(self):
        return self.usuariopac

    def getContrapac(self):
        return self.contrapac      

    def getTelefonopac(self):
        return self.telefonopac


    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombrepac(self, nombrepac):
        self.nombrepac = nombrepac
    
    def setApellidopac(self, apellidopac):
        self.apellidopac = apellidopac
    
    def setFechapac(self, fechapac):
        self.fechapac = fechapac

    def setSexopac(self, sexopac):
        self.sexopac = sexopac

    def setUsuariopac(self, usuariopac):
        self.usuariopac = usuariopac 

    def setContrapac(self, contrapac):
        self.contrapac = contrapac

    def setTelefonopac(self, telefonopac):
        self.telefonopac = telefonopac

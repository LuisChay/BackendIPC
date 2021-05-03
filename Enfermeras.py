#PARA NO PERDER LA REFERENCIA A JAVA USAMOS CLASES
class Enfermeras:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,nombreenf,apellidoenf,fechaenf,sexoenf,usuarioenf,contraenf,telefonoenf):
        self.nombreenf = nombreenf
        self.apellidoenf = apellidoenf
        self.fechaenf = fechaenf
        self.sexoenf = sexoenf
        self.usuarioenf = usuarioenf
        self.contraenf = contraenf
        self.telefonoenf = telefonoenf


    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombreenf(self):
        return self.nombreenf
    
    def getApellidoenf(self):
        return self.apellidoenf
    
    def getFechaenf(self):
        return self.fechaenf

    def getSexoenf(self):
        return self.sexoenf

    def getUsuarioenf(self):
        return self.usuarioenf

    def getContraenf(self):
        return self.contraenf       

    def getTelefonoenf(self):
        return self.telefonoenf



    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombreenf(self, nombreenf):
        self.nombreenf = nombreenf
    
    def setApellidoenf(self, apellidoenf):
        self.apellidoenf = apellidoenf
    
    def setFechaenf(self, fechaenf):
        self.fechaenf = fechaenf

    def setSexoenf(self, sexoenf):
        self.sexoenf = sexoenf

    def setUsuarioenf(self, usuarioenf):
        self.usuarioenf = usuarioenf 

    def setContraenf(self, contraenf):
        self.contraenf = contraenf

    def setTelefonoenf(self, telefonoenf):
        self.telefonoenf = telefonoenf
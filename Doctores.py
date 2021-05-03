#PARA NO PERDER LA REFERENCIA A JAVA USAMOS CLASES
class Doctores:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,nombredoc,apellidodoc,fechadoc,sexodoc,usuariodoc,contradoc,telefonodoc,especialidaddoc):
        self.nombredoc = nombredoc
        self.apellidodoc = apellidodoc
        self.fechadoc = fechadoc
        self.sexodoc = sexodoc
        self.usuariodoc = usuariodoc
        self.contradoc = contradoc
        self.telefonodoc = telefonodoc
        self.especialidaddoc = especialidaddoc

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombredoc(self):
        return self.nombredoc
    
    def getApellidodoc(self):
        return self.apellidodoc
    
    def getFechadoc(self):
        return self.fechadoc

    def getSexodoc(self):
        return self.sexodoc

    def getUsuariodoc(self):
        return self.usuariodoc

    def getContradoc(self):
        return self.contradoc       

    def getTelefonodoc(self):
        return self.telefonodoc

    def getEspecialidaddoc(self):
        return self.especialidaddoc
        
    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombredoc(self, nombredoc):
        self.nombredoc = nombredoc
    
    def setApellidodoc(self, apellidodoc):
        self.apellidodoc = apellidodoc
    
    def setFechadoc(self, fechadoc):
        self.fechadoc = fechadoc

    def setSexodoc(self, sexodoc):
        self.sexodoc = sexodoc

    def setUsuariodoc(self, usuariodoc):
        self.usuariodoc = usuariodoc 

    def setContradoc(self, contradoc):
        self.contradoc = contradoc

    def setTelefonodoc(self, telefonodoc):
        self.telefonodoc = telefonodoc

    def seteEspecialidaddoc(self, especialidaddoc):
        self.especialidaddoc = especialidaddoc
class Citas:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,idpaciente,fechacita,horacita,motivocita,estadocita):
        self.idpaciente = idpaciente
        self.fechacita = fechacita
        self.horacita = horacita
        self.motivocita = motivocita
        self.estadocita = estadocita
      

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getIdpaciente(self):
        return self.idpaciente
    
    def getFechacita(self):
        return self.fechacita
    
    def getHoracita(self):
        return self.horacita

    def getMotivocita(self):
        return self.motivocita

    def getEstadocita(self):
        return self.estadocita


    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setIdpaciente(self, idpaciente):
        self.idpaciente = idpaciente
    
    def setFechacita(self, fechacita):
        self.fechacita = fechacita
    
    def setHoracita(self, horacita):
        self.horacita = horacita

    def setMotivocita(self, motivocita):
        self.motivocita = motivocita

    def setEstadocita(self, estadocita):
        self.estadocita = estadocita 

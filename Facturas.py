class Facturas:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,fechafactura,pacientefactura,doctorfactura,precioconsulta,costooperacion, costointernado,totalfactura):
        self.fechafactura = fechafactura
        self.pacientefactura = pacientefactura
        self.doctorfactura = doctorfactura
        self.precioconsulta = precioconsulta
        self.costooperacion = costooperacion
        self.costointernado = costointernado
        self.totalfactura = totalfactura

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getFechafactura(self):
        return self.fechafactura
    
    def getPacientefactura(self):
        return self.pacientefactura
    
    def getDoctorfactura(self):
        return self.doctorfactura

    def getPrecioconsulta(self):
        return self.precioconsulta

    def getCostooperacion(self):
        return self.costooperacion

    def getCostointernado(self):
        return self.costointernado
        
    def getTotalfactura(self):
        return self.totalfactura

    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setFechafactura(self, fechafactura):
        self.fechafactura = fechafactura
    
    def setPacientefactura(self, pacientefactura):
        self.pacientefactura = pacientefactura
    
    def setDoctorfactura(self, doctorfactura):
        self.doctorfactura = doctorfactura

    def setPrecioconsulta(self, precioconsulta):
        self.precioconsulta = precioconsulta

    def setCostooperacion(self, costooperacion):
        self.costooperacion = costooperacion 

    def setCostointernado(self, costointernado):
        self.costointernado = costointernado

    def setTotalfactura(self, totalfactura):
        self.totalfactura = totalfactura  

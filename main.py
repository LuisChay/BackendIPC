import _csv

# IMPORTAMOS LOS ARCHIVOS NECESARIOS PARA CORRER NUESTRO SERVIDOR
from flask import Flask, jsonify, request

from flask_cors import CORS

# IMPORTAMOS LAS "CLASES" CREADAS

from Doctores import Doctores
from Enfermeras import Enfermeras
from Medicamentos import Medicamentos
from Pacientes import Pacientes
from Citas import Citas
from Facturas import Facturas
from Recetas import Recetas

import json

# CREACION DE LISTAS PARA ALMACENAR INFORMACION

DoctoresArr = []
EnfermerasArr = []
MedicamentosArr = []
PacientesArr = []
CitasArr = []
FacturasArr = []
RecetasArr = []



# CREACION DE LA APLICACION FLASK

app = Flask(__name__)
# Agregamos el CORS para que esto no nos de problemas a la hora de comunicarnos con el FRONTEND
CORS(app)


@app.route('/', methods=['GET'])
# Seguido de definir la ruta, agregamos un def para declara una funcion en python y el nombre de la funcion
# Todo lo que hagamos dentro de esta funcion es lo que se ejecutara cuando utilicemos esta ruta.
def rutaInicial():
    # Todo metodo deberia de devolver un JSON para que sea entendido en el Frontend.
    return("<h1>Prueba</h1>")

# MISMA RUTA - DIFERENTE METODO
@app.route('/', methods=['POST'])
def rutaPost():
    # En este caso creamos un Diccionario de Python, los diccionarios son listas de clave-valor
    # Si lo comparamos, puede adaptarse perfectamente como un objeto JSON.
    objeto = {"Mensaje":"Prueba"}
    # Utilizamos el jsonify para devolver el objeto JSON de manera ordenada
    return(jsonify(objeto))



#DOCTOR

# METODO - OBTENER TODOS DOCTOR
@app.route('/Doctores', methods=['GET'])
def getDoctores():

    global DoctoresArr

    Datos = []

    for doctor in DoctoresArr:

        objeto = {
            'Nombre': doctor.getNombredoc(),
            'Apellido': doctor.getApellidodoc(),
            'Fecha': doctor.getFechadoc(),
            'Sexo': doctor.getSexodoc(),
            'Usuario': doctor.getUsuariodoc(),
            'Contrasena': doctor.getContradoc(),
            'Especialidad': doctor.getEspecialidaddoc(),
            'Telefono': doctor.getTelefonodoc(),    
        }
        Datos.append(objeto)

    return(jsonify(Datos))


# METODO - OBTENER UN DATO DOCTOR ESPECIFICO
@app.route('/Doctores/<string:nombredoc>', methods=['GET'])
def ObtenerDoctor(nombredoc): 

    global DoctoresArr

    for doctor in DoctoresArr:
    
        if doctor.getUsuariodoc() == nombredoc:
            objeto = {
            'Nombre': doctor.getNombredoc(),
            'Apellido': doctor.getApellidodoc(),
            'Fecha': doctor.getFechadoc(),
            'Sexo': doctor.getSexodoc(),
            'Usuario': doctor.getUsuariodoc(),
            'Contrasena': doctor.getContradoc(),
            'Telefono': doctor.getTelefonodoc(),
            'Especialidad': doctor.getEspecialidaddoc(),
            }

            return(jsonify(objeto))

    salida = { "Mensaje": "No existe el doctor con el nombre: " + nombredoc }

    return(jsonify(salida))

#doctor.getNombredoc() == nombredoc or 

# METODO - GUARDAR UN DATO DOCTOR
@app.route('/Doctores', methods=['POST'])
def AgregarDoctor():

    global DoctoresArr

    nombredoc = request.json['nombredoc']
    apellidodoc = request.json['apellidodoc']
    fechadoc = request.json['fechadoc']
    sexodoc= request.json['sexodoc']
    usuariodoc = request.json['usuariodoc']
    contradoc = request.json['contradoc']
    especialidaddoc = request.json['especialidaddoc']
    telefonodoc = request.json['telefonodoc']

    nuevo = Doctores(nombredoc,apellidodoc,fechadoc,sexodoc,usuariodoc,contradoc,especialidaddoc,telefonodoc)

    DoctoresArr.append(nuevo)

    return jsonify({'Mensaje':'Se agrego el doctor exitosamente',})


# METODO - ACTUALIZAR UN DATO DOCTOR
@app.route('/Doctores/<string:nombredoc>', methods=['PUT'])
def ActualizarDoctor(nombredoc):

    global DoctoresArr

    print (nombredoc)
    for i in range(len(DoctoresArr)):
            
        if nombredoc == DoctoresArr[i].getUsuariodoc():

            DoctoresArr[i].setNombredoc(request.json['Nombredoc'])
            DoctoresArr[i].setApellidodoc(request.json['Apellido'])
            DoctoresArr[i].setFechadoc(request.json['Fecha'])
            DoctoresArr[i].setSexodoc(request.json['Sexo'])
            DoctoresArr[i].setUsuariodoc(request.json['Usuario'])
            DoctoresArr[i].setContradoc(request.json['Contrasena'])
            DoctoresArr[i].seteEspecialidaddoc(request.json['Especialidad'])
            DoctoresArr[i].setTelefonodoc(request.json['Telefono'])

            return jsonify({'Mensaje':'Se actualizo el doctor exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})


# METODO - ELIMINAR UN DATO DOCTOR
@app.route('/Doctores/<string:nombredoc>', methods=['DELETE'])
def EliminarDoctor(nombredoc):

    global DoctoresArr

    for i in range(len(DoctoresArr)):

        if nombredoc == DoctoresArr[i].getNombredoc():

            del DoctoresArr[i]
            
            return jsonify({'Mensaje':'Se elimino el doctor exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
# NOTA IMPORTANTE: Cabe destacar que el dato que mandamos como parametro debe de ser el identificador del objeto
# Si trabajaramos con un Usuarios, mandamos username, si trabajamos con Recetas, mandamos el correlativo.


#ENFERMERAS

# METODO - OBTENER TODOS ENFERMERA
@app.route('/Enfermeras', methods=['GET'])
def getEnfermeras():

    global EnfermerasArr

    Datos = []

    for enfermera in EnfermerasArr:

        objeto = {
            'Nombre': enfermera.getNombreenf(),
            'Apellido': enfermera.getApellidoenf(),
            'Fecha': enfermera.getFechaenf(),
            'Sexo': enfermera.getSexoenf(),
            'Usuario': enfermera.getUsuarioenf(),
            'Contrasena': enfermera.getContraenf(),
            'Telefono': enfermera.getTelefonoenf(),
        }

        Datos.append(objeto)

    return(jsonify(Datos))


# METODO - OBTENER UN DATO ENFERMERA ESPECIFICO
@app.route('/Enfermeras/<string:nombreenf>', methods=['GET'])
def ObtenerEnfermera(nombreenf): 

    global EnfermerasArr

    for enfermera in EnfermerasArr:
        if enfermera.getUsuarioenf() == nombreenf:
            objeto = {
            'Nombre': enfermera.getNombreenf(),
            'Apellido': enfermera.getApellidoenf(),
            'Fecha': enfermera.getFechaenf(),
            'Sexo': enfermera.getSexoenf(),
            'Usuario': enfermera.getUsuarioenf(),
            'Contrasena': enfermera.getContraenf(),
            'Telefono': enfermera.getTelefonoenf(),
            }

            return(jsonify(objeto))

    salida = { "Mensaje": "No existe enfernera con ese nombre"}

    return(jsonify(salida))



# METODO - GUARDAR UN DATO ENFERMERA
@app.route('/Enfermeras', methods=['POST'])
def AgregarEnfermera():

    global EnfermerasArr

    nombreenf = request.json['nombreenf']
    apellidoenf = request.json['apellidoenf']
    fechaenf = request.json['fechaenf']
    sexoenf= request.json['sexoenf']
    usuarioenf = request.json['usuarioenf']
    contraenf = request.json['contraenf']
    telefonoenf = request.json['telefonoenf']

    nuevo = Enfermeras(nombreenf,apellidoenf,fechaenf,sexoenf,usuarioenf,contraenf,telefonoenf)

    EnfermerasArr.append(nuevo)

    return jsonify({'Mensaje':'Se agrego la enfermera exitosamente',})


# METODO - ACTUALIZAR UN DATO ENFERMERA
@app.route('/Enfermeras/<string:nombreenf>', methods=['PUT'])
def ActualizarEnfermera(nombreenf):

    global EnfermerasArr


    for i in range(len(EnfermerasArr)):

        if nombreenf == EnfermerasArr[i].getUsuarioenf():

            EnfermerasArr[i].setNombreenf(request.json['Nombre'])
            EnfermerasArr[i].setApellidoenf(request.json['Apellido'])
            EnfermerasArr[i].setFechaenf(request.json['Fecha'])
            EnfermerasArr[i].setSexoenf(request.json['Sexo'])
            EnfermerasArr[i].setUsuarioenf(request.json['Usuario'])
            EnfermerasArr[i].setContraenf(request.json['Contrasena'])
            EnfermerasArr[i].setTelefonoenf(request.json['Telefono'])

            return jsonify({'Mensaje':'Se actualizo la enfermera exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar la enfermera'})

# METODO - ELIMINAR UN DATO ENFERMERA
@app.route('/Enfermeras/<string:nombreenf>', methods=['DELETE'])
def EliminarEnfermera(nombreenf):

    global EnfermerasArr

    for i in range(len(EnfermerasArr)):

        if nombreenf == EnfermerasArr[i].getNombreenf():

            del EnfermerasArr[i]
            
            return jsonify({'Mensaje':'Se elimino la enfermera exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para eliminar a la enfermera'})


#PACIENTES

# METODO - OBTENER TODOS PPACIENTES
@app.route('/Pacientes', methods=['GET'])
def getPacientes():

    global PacientesArr

    Datos = []

    for paciente in PacientesArr:

        objeto = {
            'Nombre': paciente.getNombrepac(),
            'Apellido': paciente.getApellidopac(),
            'Fecha': paciente.getFechapac(),
            'Sexo': paciente.getSexopac(),
            'Usuario': paciente.getUsuariopac(),
            'Contrasena': paciente.getContrapac(),
            'Telefono': paciente.getTelefonopac(),
        }

        Datos.append(objeto)

    return(jsonify(Datos))


# METODO - OBTENER UN DATO PACIENTE ESPECIFICO
@app.route('/Pacientes/<string:nombrepac>', methods=['GET'])
def ObtenerPacientes(nombrepac): 

    global PacientesArr

    for paciente in PacientesArr:

        if paciente.getUsuariopac() == nombrepac:
            objeto = {
            'Nombre': paciente.getNombrepac(),
            'Apellido': paciente.getApellidopac(),
            'Fecha': paciente.getFechapac(),
            'Sexo': paciente.getSexopac(),
            'Usuario': paciente.getUsuariopac(),
            'Contrasena': paciente.getContrapac(),
            'Telefono': paciente.getTelefonopac(),
            }

            return(jsonify(objeto))

    salida = { "Mensaje": "No existe el paciente con ese nombre"}

    return(jsonify(salida))



# METODO - GUARDAR UN DATO PACIENTE
@app.route('/Pacientes', methods=['POST'])
def AgregarPaciente():

    global PacientesArr

    nombrepac = request.json['nombrepac']
    apellidopac = request.json['apellidopac']
    fechapac = request.json['fechapac']
    sexopac= request.json['sexopac']
    usuariopac = request.json['usuariopac']
    contrapac = request.json['contrapac']    
    telefonopac = request.json['telefonopac']

    nuevo = Pacientes(nombrepac,apellidopac,fechapac,sexopac,usuariopac,contrapac,telefonopac)

    PacientesArr.append(nuevo)

    return jsonify({'Mensaje':'Se agrego el paciente exitosamente',})


# METODO - ACTUALIZAR UN DATO PACIENTE
@app.route('/Pacientes/<string:nombrepac>', methods=['PUT'])
def ActualizarPaciente(nombrepac):

    global PacientesArr


    for i in range(len(PacientesArr)):

        if nombrepac == PacientesArr[i].getUsuariopac():

            PacientesArr[i].setNombrepac(request.json['nombre'])
            PacientesArr[i].setApellidopac(request.json['apellido'])
            PacientesArr[i].setFechapac(request.json['fecha'])
            PacientesArr[i].setSexopac(request.json['sexo'])
            PacientesArr[i].setUsuariopac(request.json['usuario'])
            PacientesArr[i].setContrapac(request.json['contrasena'])
            PacientesArr[i].setTelefonopac(request.json['telefono'])

            return jsonify({'Mensaje':'Se actualizo el paciente exitosamente'})

    return jsonify({'Mensaje':'No se encontro el paciente para actualizar'})


# METODO - ELIMINAR UN DATO PACIENTE
@app.route('/Pacientes/<string:nombrepac>', methods=['DELETE'])
def EliminarPaciente(nombrepac):

    global PacientesArr

    for i in range(len(PacientesArr)):

        if nombrepac == PacientesArr[i].getNombrepac():

            del PacientesArr[i]
            
            return jsonify({'Mensaje':'Se elimino el paciente exitosamente'})

    return jsonify({'Mensaje':'No se encontro el paciente para eliminar'})


#MEDICAMENTOS

# METODO - OBTENER TODOS MEDICAMENTOS
@app.route('/Medicamentos', methods=['GET'])
def getMedicamentos():

    global MedicamentosArr

    Datos = []

    for medicamento in MedicamentosArr:

        objeto = {
            'Nombre': medicamento.getNombremed(),
            'Precio': medicamento.getPreciomed(),
            'Descripcion': medicamento.getDescripcionmed(),
            'Cantidad': medicamento.getCantidadmed(),
            
        }

        Datos.append(objeto)

    return(jsonify(Datos))


# METODO - OBTENER UN DATO MEDICAMENTOS ESPECIFICO
@app.route('/Medicamentos/<string:nombremed>', methods=['GET'])
def ObtenerMedicamentos(nombremed): 

    global MedicamentosArr

    for medicamento in MedicamentosArr:

        if medicamento.getNombremed() == nombremed:
            objeto = {
            'Nombre': medicamento.getNombremed(),
            'Precio': medicamento.getPreciomed(),
            'Descripcion': medicamento.getDescripcionmed(),
            'Cantidad': medicamento.getCantidadmed(),
            }

            return(jsonify(objeto))

    salida = { "Mensaje": "No existe el medicamento con ese nombre"}

    return(jsonify(salida))



# METODO - GUARDAR UN DATO MEDICAMENTOS
@app.route('/Medicamentos', methods=['POST'])
def AgregarMedicamento():

    global MedicamentosArr

    nombremed = request.json['nombremed']
    preciomed = request.json['preciomed']
    descripcionmed = request.json['descripcionmed']
    cantidadmed= request.json['cantidadmed']
   

    nuevo = Medicamentos(nombremed,preciomed,descripcionmed,cantidadmed)

    MedicamentosArr.append(nuevo)

    return jsonify({'Mensaje':'Se agrego el medicamento exitosamente',})


# METODO - ACTUALIZAR UN DATO MEDICAMENTOS
@app.route('/Medicamentos/<string:nombremed>', methods=['PUT'])
def ActualizarMedicamento(nombremed):

    global MedicamentosArr


    for i in range(len(MedicamentosArr)):

        if nombremed == MedicamentosArr[i].getNombremed():

            MedicamentosArr[i].setNombremed(request.json['nombre'])
            MedicamentosArr[i].setPreciomed(request.json['precio'])
            MedicamentosArr[i].setDescripcionmed(request.json['descripcion'])
            MedicamentosArr[i].setCantidadmed(request.json['cantidad'])


            return jsonify({'Mensaje':'Se actualizo el medicamento exitosamente'})

    return jsonify({'Mensaje':'No se encontro el medicamento para actualizar'})


# METODO - ELIMINAR UN DATO MEDICAMENTOS
@app.route('/Medicamentos/<string:nombremed>', methods=['DELETE'])
def EliminarMedicamento(nombremed):

    global MedicamentosArr

    for i in range(len(MedicamentosArr)):

        if nombremed == MedicamentosArr[i].getNombremed():

            del MedicamentosArr[i]
            
            return jsonify({'Mensaje':'Se elimino el medicamento exitosamente'})

    return jsonify({'Mensaje':'No se encontro el medicamento para eliminar'})



#CITAS

# METODO - OBTENER TODOS CITAS
@app.route('/Citas', methods=['GET'])
def getCitas():

    global CitasArr

    Datos = []

    for cita in CitasArr:

        objeto = {
            'Idpaciente': cita.getIdpaciente(),
            'Fechacita': cita.getFechacita(),
            'Horacita': cita.getHoracita(),
            'Motivocita': cita.getMotivocita(),
            'Estadocita': cita.getEstadocita(),
        }

        Datos.append(objeto)

    return(jsonify(Datos))

# METODO - OBTENER UN DATO CITAS ESPECIFICO
@app.route('/Citas/<string:nombrecitas>', methods=['GET'])
def ObtnerCitas(nombrecitas): 

    global CitasArr

    for cita in CitasArr:

        if cita.getIdpaciente() == nombrecitas:
            objeto = {
            'Idpaciente': cita.getIdpaciente(),
            'Fechacita': cita.getFechacita(),
            'Horacita': cita.getHoracita(),
            'Motivocita': cita.getMotivocita(),
            'Estadocita': cita.getEstadocita(),
            }

            return(jsonify(objeto))

    salida = { "Mensaje": "No existe esa cita"}

    return(jsonify(salida))

# METODO - GUARDAR UN DATO CITAS
@app.route('/Citas', methods=['POST'])
def AgregarCitas():

    global CitasArr

    idpaciente = request.json['idpaciente']
    fechacita = request.json['fechacita']
    horacita = request.json['horacita'] 
    motivocita = request.json['motivocita']
    estadocita = request.json['estadocita']

   

    nuevo = Citas(idpaciente,fechacita,horacita,motivocita,estadocita)

    CitasArr.append(nuevo)

    return jsonify({'Mensaje':'Se agrego la cita exitosamente',})

@app.route('/Citas/<string:citas>', methods=['PUT'])
def ActualizarCita(citas):

    global CitasArr

    for i in range(len(CitasArr)):

        if citas == CitasArr[i].getIdpaciente():

            CitasArr[i].setIdpaciente(request.json['id'])
            CitasArr[i].setFechacita(request.json['fecha'])
            CitasArr[i].setHoracita(request.json['hora'])
            CitasArr[i].setMotivocita(request.json['motivo'])
            CitasArr[i].setEstadocita(request.json['estado'])


            return jsonify({'Mensaje':'Se actualizo la cita exitosamente'})

    return jsonify({'Mensaje':'No se encontro la cita para actualizar'})






# RECETAS

# METODO - OBTENER TODOS RECETAS
@app.route('/Recetas', methods=['GET'])
def getRecetas():

    global RecetasArr

    Datos = []

    for receta in RecetasArr:

        objeto = {
            'Fecha': receta.getFechareceta(),
            'Paciente': receta.getPacientereceta(),
            'Padecimiento': receta.getPadecimientoreceta(),
            'Descripcion': receta.getDescripcionreceta(),
        }

        Datos.append(objeto)

    return(jsonify(Datos))


# METODO - GUARDAR UN DATO RECETAS
@app.route('/Recetas', methods=['POST'])
def AgregarRecetas():

    global RecetasArr

    fechareceta = request.json['fecharec']
    pacientereceta = request.json['pacienterec']
    padecimientoreceta = request.json['padecimientorec']
    descripcionreceta = request.json['descripcionrec']
   

    nuevo = Recetas(fechareceta,pacientereceta,padecimientoreceta,descripcionreceta)

    RecetasArr.append(nuevo)

    return jsonify({'Mensaje':'Se agrego la receta exitosamente',})


# FACTURAS


# METODO - OBTENER TODOS FACTURAS
@app.route('/Facturas', methods=['GET'])
def getFacturas():

    global FacturasArr

    Datos = []

    for factura in FacturasArr:

        objeto = {
            'Fecha': factura.getFechafactura(),
            'Paciente': factura.getPacientefactura(),
            'Doctor': factura.getDoctorfactura(),
            'Preciocon': factura.getPrecioconsulta(),
            'Costoop': factura.getCostooperacion(),
            'Costoin': factura.getCostointernado(),
            'Total': factura.getTotalfactura(),
        }

        Datos.append(objeto)

    return(jsonify(Datos))


# METODO - GUARDAR UN DATO FACTURAS
@app.route('/Facturas', methods=['POST'])
def AgregarFacturas():

    global FacturasArr

    fechafactura = request.json['fechafac']
    pacientefactura = request.json['pacientefac']
    doctorfactura = request.json['doctorfac']
    precioconsulta = request.json['preciocon']
    costooperacion = request.json['costoop']
    costointernado = request.json['costoin']
    totalfactura = request.json['totalfac']

    nuevo = Facturas(fechafactura,pacientefactura,doctorfactura,precioconsulta, costooperacion, costointernado, totalfactura)

    FacturasArr.append(nuevo)

    return jsonify({'Mensaje':'Se agrego la factura exitosamente',})




# NOTA IMPORTANTE: Cabe destacar que el dato que mandamos como parametro debe de ser el identificador del objeto
# Si trabajaramos con un Usuarios, mandamos username, si trabajamos con Recetas, mandamos el correlativo.

# Y POR ULTIMO, CORRER LA APLICACION
# Una vez definido todas nuestras rutas para ser consumidas por un cliente solo nos queda correr la aplicacion
if __name__ == "__main__":
    # Le decimos que el host es 0.0.0.0 para que corra en Localhost
    # Le indicamos el puerto (Tema pendiente por ver) para indicarle en que puerto levantara la aplicacion
    app.run(host="0.0.0.0", port=3000, debug=True)
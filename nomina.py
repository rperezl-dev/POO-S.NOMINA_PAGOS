from componente import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArchivos import Archivo
from entidadesRol import *
from datetime import date
import time
'''
==================================================================================================
                   Procesos de las Opciones del Menu Mantenimiento
==================================================================================================
'''
#Inicio
def empAdministrativos():
   validar = Valida()
   borrarPantalla()
   gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADO ADMINISTRATIVOS")
   gotoxy(15,3);print("Codigo: ")
   gotoxy(15,4);print("Nombre: ")
   gotoxy(15,5);print("Departamento: ")
   gotoxy(15,6);print("Cargo: ")
   gotoxy(15,7);print("Dirección: ")
   gotoxy(15,8);print("Cedula: ")
   gotoxy(15,9);print("Telefono: ")
   gotoxy(15,10);print("Fecha Ingreso: ")
   gotoxy(15,11);print("Sueldo: ")
   gotoxy(15,12);print("Comision(s/n): ")
   archiEmpAdmin = Archivo("./archivos/administrativo.txt","|")
   archiCargo = Archivo("./archivos/cargo.txt","|")
   archiDepartamento = Archivo("./archivos/departamento.txt","|")
   empleados = archiEmpAdmin.leer()
   if empleados : idSig = int(empleados[-1][0][1:])+1
   else: idSig=1
   idSig = f'A{idSig}'
   gotoxy(33,3);print(idSig)
   nombre =validar.es_vacio('Nombre',33,4)
   departamento = validar.id('Departamento',33,5,archiDepartamento)
   cargo = validar.id('Cargo',33,6,archiCargo)
   direccion = validar.es_vacio('Direccion',33,7) 
   cedula = validar.cedula('Cedula',33,8,archiEmpAdmin)
   telefono = validar.telefono('Telefono',33,9) 
   fecha_ingreso = validar.fecha('Fecha Ingreso',33,10)
   sueldo = validar.solo_decimales_1('Sueldo',33,11)
   comision = validar.opcion('Comisión',33,12)
   comision = True if comision == 's' else False;
   departamento = Departamento(departamento[1],int(departamento[0]))
   cargo = Cargo(cargo[1],int(cargo[0]))
   emple_Admin = Administrativo(nombre,departamento,cargo,direccion,cedula,telefono,fecha_ingreso,sueldo,idSig,comision)
   datos = emple_Admin.getEmpleado()
   datos = '|'.join(datos)
   gotoxy(15,14);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,15);grabar = input().lower()
   if grabar == "s":
       archiEmpAdmin.escribir([datos],"a")
       gotoxy(10,16);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,17);input("Registro No fue Grabado\n presione una tecla para continuar...")     

def empObreros():
   validar = Valida()
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADO OBREROS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Nombre: ")
   gotoxy(15,6);print("Departamento: ")
   gotoxy(15,7);print("Cargo: ")
   gotoxy(15,8);print("Dirección: ")
   gotoxy(15,9);print("Cedula: ")
   gotoxy(15,10);print("Telefono: ")
   gotoxy(15,11);print("Fecha Ingreso: ")
   gotoxy(15,12);print("Sueldo: ")
   gotoxy(15,13);print("CC(s/n): ")
   archiEmpObrero = Archivo("./archivos/obrero.txt","|")
   archiCargo = Archivo("./archivos/cargo.txt","|")
   archiDepartamento = Archivo("./archivos/departamento.txt","|")
   empleados = archiEmpObrero.leer()
   if empleados : idSig = int(empleados[-1][0][1:])+1
   else: idSig=1
   idSig = f'O{idSig}'
   gotoxy(24,4);print(idSig)
   nombre = validar.es_vacio('Nombre',33,5)
   departamento = validar.id('Departamento',33,6,archiDepartamento)
   cargo = validar.id('Cargo',33,7,archiCargo)
   direccion = validar.es_vacio('Direccion',33,8) 
   cedula = validar.cedula('Cedula',33,9,archiEmpObrero)
   telefono = validar.telefono('Telefono',33,10) 
   fecha_ingreso = validar.fecha('Fecha Ingreso',33,11)
   sueldo = validar.solo_decimales_1('Sueldo',33,12)
   cc = validar.opcion('cc',33,13)
   cc = True if cc == 's' else False;
   departamento = Departamento(departamento[1],int(departamento[0]))
   cargo = Cargo(cargo[1],int(cargo[0]))
   emple_Obrero = Obrero(nombre,departamento,cargo,direccion,cedula,telefono,fecha_ingreso,sueldo,idSig,cc)
   datos = emple_Obrero.getEmpleado()
   datos = '|'.join(datos)
   gotoxy(15,14);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,15);grabar = input().lower()
   if grabar == "s":
       archiEmpObrero.escribir([datos],"a")
       gotoxy(10,16);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,17);input("Registro No fue Grabado\n presione una tecla para continuar...") 

def cargos():
   validar =Valida()
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARGOS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Cargo: ")
   archiCargo = Archivo("./archivos/cargo.txt","|")
   cargos = archiCargo.leer()
   if cargos : idSig = int(cargos[-1][0])+1
   else: idSig=1
   gotoxy(24,4);print(idSig)
   gotoxy(33,5)
   desCargo = validar.es_vacio('Nombre',33,5)
   cargo = Cargo(desCargo,idSig)
   datos = cargo.getCargo()
   datos = '|'.join(datos)
   gotoxy(15,7);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,8);grabar = input().lower()
   if grabar == "s":
       archiCargo.escribir([datos],"a")
       gotoxy(10,9);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...") 

def departamentos():
   validar = Valida()
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE DEPARTAMENTO")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Departamento: ")
   archiDepartamento = Archivo("./archivos/departamento.txt","|")
   departamentos = archiDepartamento.leer()
   if departamentos : idSig = int(departamentos[-1][0])+1
   else: idSig=1
   gotoxy(24,4);print(idSig)
   gotoxy(40,5)
   desDepartamento = validar.es_vacio('Nombre',33,5)
   departamento = Departamento(desDepartamento,idSig)
   datos = departamento.getDepartamento()
   datos = '|'.join(datos)

   gotoxy(15,7);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,8);grabar = input().lower()
   if grabar == "s":
       archiDepartamento.escribir([datos],"a")
       gotoxy(10,9);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...") 

def empresas():
   validar = Valida()
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE EMPRESA")
   gotoxy(15,5);print("Razón Social: ")
   gotoxy(15,6);print("Dirección: ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Ruc: ")
   archiEmpresa = Archivo("./archivos/empresa.txt","|")
   empresas = archiEmpresa.leer()
   gotoxy(40,5)
   desEmpresa =  validar.es_vacio('Nombre',33,5)
   gotoxy(40,6)
   direccion = validar.es_vacio('Nombre',33,6)
   gotoxy(40,7)
   telefono = validar.telefono('Telefono',33,7)
   gotoxy(40,8)
   ruc = validar.ruc('Ruc',33,8,archiEmpresa)
   empresa = Empresa(desEmpresa,direccion,telefono,ruc)
   datos = empresa.getEmpresa()
   datos = '|'.join(datos)
   
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,11);grabar = input().lower()
   if grabar == "s":
       archiEmpresa.escribir([datos],"a")
       gotoxy(10,12);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,13);input("Registro No fue Grabado\n presione una tecla para continuar...") 

def deducciones():
   validar = Valida()
   gotoxy(20,2);print("MANTENIMIENTO DE PARAMETROS")
   gotoxy(15,5);print("Iess: ")
   gotoxy(15,6);print("Comisión: ")
   gotoxy(15,7);print("Antiguedad: ")
   archiDeduccion = Archivo("./archivos/deducciones.txt","|")
   iess =  validar.solo_decimales_1('Iess',33,5)
   comision =  validar.solo_decimales_1('Comisión',33,6)
   antiguedad =  validar.solo_numeros_enteros('Antiguedad',33,7)
   deduccion = Deduccion(iess,comision,antiguedad)
   datos = deduccion.getDeduccion()
   datos = '|'.join(datos)
   
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
       archiDeduccion.escribir([datos],"a")
       gotoxy(10,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,12);input("Registro No fue Grabado\n presione una tecla para continuar...") 

#
# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[    ]: ")
      gotoxy(27,5);id = input().upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(entEmpleado.nombre)
      else: 
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         time.sleep(2);gotoxy(27,5);print(" "*40)
    
    
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(15,7);print("Horas50:")
   gotoxy(15,8);print("Horas100:")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   #gotoxy(23,6);aamm = input()
   gotoxy(23,7);h50 = validar.solo_numeros("Error: Solo numeros",33,7)
   gotoxy(24,8);h100 = validar.solo_numeros("Error: Solo numeros",33,7)
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
   
def prestamos():
   validar = Valida()
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DE PRESTAMO")
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[    ]: ")
      gotoxy(27,5);id = input().upper()
      archivo = './archivos/obrero.txt'
      archivo_prestamo = './archivos/prestamo.txt'
      if id[0] == "A":
          archivo = './archivos/administrativo.txt'
      else:
          archivo = './archivos/obrero.txt'
      archiEmpleado = Archivo(archivo,"|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
        entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
        if empleado[0][0] == "A":
            entEmpleado = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
        gotoxy(35,5);print(entEmpleado.nombre)
      else: 
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         time.sleep(2);gotoxy(27,5);print(" "*40)

   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(15,7);print("Valor:")
   gotoxy(15,8);print("NumPagos:")
   gotoxy(15,9);print("Saldo:")
   
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   valor = validar.solo_decimales_1("Valor",33,7)
   num_pagos = validar.solo_numeros_enteros("NumPagos",33,8)
   saldo = validar.solo_decimales_1("Saldo",33,9)
   #gotoxy(23,6);aamm = input()
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiPrestamo = Archivo(archivo_prestamo,"|")
        prestamos = archiPrestamo.leer()
        if prestamos : idSig = int(prestamos[-1][0])+1
        else: idSig=1
        prestamo = Prestamo(entEmpleado,aamm,valor,num_pagos,saldo,True,idSig)
        datos = prestamo.getPrestamo()
        datos = '|'.join(datos)
        archiPrestamo.escribir([datos],"a")                 
        gotoxy(10,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     

# opciones de Rol de Pago
def rolAdministrativo():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"ADMINISTRATIVOS")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")  

def consultaRol():
   borrarPantalla()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar     
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input().upper()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])    
            # print(entCabRol.getNomina())
            # print(entCabRol.getDetalle())
            # input()
            # imprimir rol    
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")     
            
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...")  

def rolObrero():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL OBRERO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm :
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObr.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObr.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"OBREROS")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...") 

def sobreEmpleado():
   borrarPantalla()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar     
   gotoxy(20,2);print("CONSULTA DE Empleado")
   id=0
   aamm=""
   gotoxy(15,4);print("Empleado ID[    ]: ")
   gotoxy(27,4)
   id=input().upper()
   gotoxy(15,5);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,5);procesar = input().lower()
   empleado,entEmpleado = [],None
   if procesar == "s":       
        if id[0] == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiEmpleado = Archivo("./archivos/administrativo.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiEmpleado = Archivo("./archivos/obrero.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt","|")
        archiCargo = Archivo("./archivos/Cargo.txt","|")
        archiDepartamento = Archivo("./archivos/departamento.txt","|")

        empleado = archiEmpleado.buscar(id)
        if empleado:
            depa = archiDepartamento.buscar(empleado[2])
            carg = archiCargo.buscar(empleado[3])
            departamento = Departamento(depa[1] if depa else 'Sin Departamento',depa[0] if depa else 0)
            cargo = Cargo(carg[1] if carg else 'Sin Cargo',carg[0] if carg else 0)
            entEmpleado = Obrero(empleado[1],departamento,cargo,empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
            if empleado[0][0] == "A":
                entEmpleado = Administrativo(empleado[1],departamento,cargo,empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
            detalle= archiRolDet.buscarLista(id,1)
            for det in detalle:
                entEmpleado.detalleRol.append(det)       
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entEmpleado.mostrarCabeceraRol(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entEmpleado.mostrarDetalleRol()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")     
            
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...") 

# Menu Proceso Principal

opc=''

while opc !='4':  
    borrarPantalla()    
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Salir"],0,0)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Empleados Administratvos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],0,0)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            if opc1 == "2":
                empObreros()
            elif opc1 == "3":
                cargos()
            elif opc1 == "4":
                departamentos()
            elif opc1 == "5":
                empresas()
            elif opc1 == "6":
                borrarPantalla()
                deducciones()
         
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Novedades",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Rol",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Sobre Empleado","5) Salir"],0,0)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()

            elif opc3 == "4":
                sobreEmpleado()
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

#Nomina 1. Registro de empleados - identificiacion , nombre, cargo , salario
#Registro de inasistencia . identificacion y se debe guardar la fecha de la falta 
# Registro de bono extra - legales - identificacion   - fecha , valor y concepto

import time
from datetime import datetime
import json
empleados =[]
salario_trabajador = 0


def guardar_datos_json():
    
    info = {
        "Empleado": empleados,       
        "Salario": salario_trabajador
    }
    
    with open("salario.json","w")as json_file:
        json.dump(info, json_file, indent=4)  # Guardar con formato legible
    print("datos guardados en ingresos.json")

def cargar_datos_json():
    global empleados , salario_trabajador
    try:
        with open("salario.json", "r") as json_file:
            info = json.load(json_file)
            empleados = info.get("ingresos_laborales", [])
            salario_trabajador = info.get("total_ingreso", 0)
            print("Datos cargados desde ingresos.json")
    except FileNotFoundError:
        print("No se encontró el archivo ingresos.json.")
    
def registro_empleados():
    global salario_trabajador
    print("====== R E G I S T R A R  E M P L E A D O S ====")
    id_Trabajador = int(input(">> Ingresa el Numero de Identificacion del empleado: "))
    Nombre = input(">> Ingresa el Nombre del empleado: ")
    Cargo = input(">> Ingresa el Cargo del empleado: ")
    Salario = int(input(">> Ingresa el Salario del Empleado:$ "))
    
    datos={
        "identificacion": id_Trabajador,
        "Nombre": Nombre,
        "Cargo": Cargo,
        "Salario":Salario
    }
    
    empleados.append(datos)
    salario_trabajador += Salario
    print("===== I N F O R M A C I O N ====")
    print("Nombre: " , Nombre)
    print("ID: ", id_Trabajador)
    print("Cargo: ", Cargo)
    print("Salarion: $" , Salario)
    print("---- R e g i s t r o  E x i t o s o -----")

def  registro_inasistencia():
    
    print("===== R E G I S T R O  I N A S I S T E N C I A ======")
    id_Trabajador = int(input(">> Ingresa el Numero de Identificacion del empleado: "))
    for empleado in empleados:
        if  empleado["identificacion"] == id_Trabajador:
            falta = int(input(">> Registra la inasistencia: "))
            fecha_falta = input("Ingresa la fecha en formato DD/MM/AA: ")

        try: 
            fecha = datetime.strptime(fecha_falta, "%d/%m/%Y")
            fecha_formateada = fecha.strftime("%d/%m/%Y")
            
            
            inasistencia={
            "identificacion": id_Trabajador,
            "Inasistencia": falta,
            "Fecha": fecha_formateada 
            }    
            empleados.append(inasistencia)
            print("==== I N F O R M A C I O N =====")
            print("ID: " , id_Trabajador)
            print("Inasistencia: ", falta)
            print("Fecha Insistencia: " , fecha_formateada)
            print("---R e g i s t r o  e x i t o s o ---")
            break
        except ValueError:
            print("Formato de ingreso de fecha... Incorrecto")
       
def bono_extra():
    global salario_trabajador
    print("====== R E G I S T R O  B O N O  E X T R A  $ =========")
    id_trabajador= int(input(">> Ingresa el Numero de identificacion del empleado: "))
    for empleado in empleados:
        if empleado["identificacion"] == id_trabajador:
            concepto = input(">> Ingresa el concepto del bono: ")
            valor_Bono = int(input(">> Ingresa el valor del Bono:$  "))
            fecha_Bono = input(">> Ingresa la fecha en formato DD/MM/AA: ")
        
        try:
            fecha = datetime.strptime(fecha_Bono, "%d/%m/%Y")
            fecha_formateada = fecha.strftime("%d/%m/%Y")
            
            bono ={
                "identificacion": id_trabajador,
                "Bono": valor_Bono,
                "Concepto": concepto,
                "fecha": fecha_formateada
            }
            empleados.append(bono)
            salario_trabajador += valor_Bono
            print("=== I N F O R M A C I O N =====")
            print("ID:", id_trabajador)
            print("Bono:", valor_Bono)
            print("Concepto", concepto)
            print("Fecha: ", fecha_formateada)
            print(f"Total acumulado de salario laboral: $ {salario_trabajador}")
            break
        except ValueError:
            print("Formato de ingreso de fecha... Incorrecto.")
       
def calculo_nomina():
    salariobase = 1000
    global salario_trabajador
    print("====== N O M  I N  A   A C M E =========")
    id_Trabajador= int(input(">> Ingresa el Numero de identificacion del empleado: "))
    for empleado in empleados:
        if empleado["identificacion"]== id_Trabajador:
            if  salario_trabajador > 2* salariobase:
                descuento_salud = salario_trabajador*0.04
                descuento_pension = salario_trabajador*0.04
                salario_trabajador -= (descuento_salud+descuento_pension)
                print(f"Total acumulado de salario laboral: $ {salario_trabajador}")
                break
            else :
                descuento_salud = salario_trabajador*0.04
                descuento_pension = salario_trabajador*0.04
                auxilio_tranporte = salario_trabajador *0.10
                salario_trabajador -= (descuento_pension+descuento_salud)
                salario_trabajador += auxilio_tranporte
                print(f"Total acumulado de salario laboral con auxilio: $ {salario_trabajador}")
            
  
    
menu = """
======= A C M E ======
==== N O M I N  A =====
======================
1.R E G I S T R O  D E  E M P L E A D O S
2.R E G I S T R O  I N A S I S T E N C I A S 
3.R E G I S T R O  B O N O  E X T R A 
4.C A L C U L A R   N O M I N A 
0. S A L I R 
"""



while True:
    print(menu)
    opc=int(input(">> Ingresa una opcion: "))
    if opc == 1:
            registro_empleados()
    elif opc == 2:
            registro_inasistencia()
    elif opc == 3:
            bono_extra()
    elif opc == 4:
            calculo_nomina()
    elif opc == 0:
            guardar_datos_json()
            print("Saliendo...")
            time.sleep(1.5)
            break
    else:
        print("Ingresa una opcion valida..")
    
#!/usr/bin/python
import logging
import subprocess
from colorama import init
import main_menu
import hashlib
import os
import sys
import argparse
from datetime import datetime
import main_menu

from os import system

logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo de mensajes que se registrarán
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de los mensajes
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
    filename='main_script.log',  # Archivo donde se guardarán los logs
    filemode='a'  # Modo de escritura a para no sobreescribir 
)


def show_menuW():
    print("\n")
    print("""\
    
    ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
    ████╗░████║██╔════╝████╗░██║██║░░░██║
    ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
    ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

    ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
    ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
    ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
    ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
    ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝
          
    """)
    print("1. Módulos de Power Shell")
    print("2. Módulos de Python ")
    print("3. Salir")

def show_menuL():
    print("\n")
    print("""\
    
    ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
    ████╗░████║██╔════╝████╗░██║██║░░░██║
    ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
    ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

    ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
    ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
    ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
    ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
    ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝
          
    """)
    print("1. Módulos de Bash")
    print("2. Módulos de Python ")
    print("3. Salir")

def execute_moduleW(option):
    if option == '1':
        logging.info("Usuario seleccionó scripts de Powershell.")
        execute_ps()  # Llama a la función main de sho.py
    elif option == '2':
        logging.info("Usuario seleccionó scripts de python")
        main_menu.main()
    if option == '3':
        logging.info("Usuario seleccionó salir")
        sys.exit()  # Llama a la función main de sho.py
    else:
        logging.warning("Opción no válida seleccionada.")
        print("Opción no válida. Por favor, selecciona una opción del menú.")
    return True

def execute_moduleL(option):
    if option == '1':
        logging.info("Usuario seleccionó scripts de Bash")
        execute_bh()  # Llama a la función main de sho.py
    elif option == '2':
        logging.info("Usuario seleccionó scripts de Python")
        
    if option == '3':
        logging.info("Usuario seleccionó salir")
        sys.exit()  # Llama a la función main de sho.py
    else:
        logging.warning("Opción no válida seleccionada.")
        print("Opción no válida. Por favor, selecciona una opción del menú.")
    return True

def execute_ps():
    system("cls")
    while True:
        print("""\nSeleccione el módulo que desea ejecutar:"
        \n[1] Revisión de Hashes
        \n[2] Listado de Archivos
        \n[3] Uso de RAM
        \n[4] Uso de Disco
        \n[5] Uso de CPU
        \n[6] Información de la Red
        \n[7] Auditoría de Permisos de Carpeta
        \n[8] Salir""")
        
        while True: # Ciclo de validacion
            try:
                option=int(input())
                if option==8:
                    system("cls")
                    main()
                else:
                    ps_report(option)
                break
                
            except ValueError: # Exepcion
                print("La opción que ingreso es invalida")
                logging.error("El usuario ingreso un caracter invalido")
        

        

    return 0

def execute_bh():
    while True:
        system("cls")
        print("Seleccione la funcion que desea ejecutar")
        print("1-Escaneo de puertos")
        print("2-Revision de archivos")
        print("3-Salir")
            
        while True: # Ciclo de validacion
            try:
                option=int(input())
                if option==1:
                    script_path="check_files"
                    print("Ingrese la carpeta a escanear: ")
                    pathbash=input() #Carpeta a escanear 
                    opcion_menu = "2"

                    # Crear el proceso con subprocess.Popen
                    process = subprocess.Popen(['bash', script_path, pathbash], 
                                                stdin=subprocess.PIPE, 
                                                stdout=subprocess.PIPE, 
                                                stderr=subprocess.PIPE, 
                                                text=True)
                        
                    # Enviamos la opción 2 la cual es la que genera el reporte 
                    stdout, stderr = process.communicate(input=opcion_menu + "\n")  #"\n" es como si fuera un enter
    
                elif option==2:

                    # Función para ejecutar el script bash y enviar las entradas necesarias
                    script_path="scan_ports"
                    print("Ingrese host a escanear: ")
                    host=input()
                    print("Ingrese Puerto inicial")
                    pi=input()
                    print("Ingrese Puerto final: ")
                    pf=input()

                    # Ruta al script bash
                    script_path = './PUERTOS'

                    # Ejecutar el script en modo interactivo
                    process = subprocess.Popen(
                            script_path, 
                            stdin=subprocess.PIPE, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            text=True
                        )

                    #Enviar entradas al script 
                    process.stdin.write('1\n')  
                    process.stdin.write(host+'\n')  
                    process.stdin.write('2\n')  
                    process.stdin.write(pi+'\n')  
                    process.stdin.write(pf+'\n') 
                    process.stdin.write('3\n')  
                    process.stdin.write('4\n')  
                    process.stdin.write('5\n')  

                    stdout, stderr = process.communicate()
                                        

                elif option==3:
                    system("cls")
                    main()
                
                
            except ValueError: # Exepcion
                print("La opción que ingreso es invalida")
                logging.error("El usuario ingreso un caracter invalido")
        
    
    return 0

def ps_report(option):

    if option==1:
        filename="Hash_check"
    elif option==2:
        filename="File_list"
    elif option==3:
        filename="ResourcesSystemMemInfo"
    elif option==4:
        filename="ResourcesSystemDiskInfo"
    elif option==5:
        filename="ResourcesSystemCPUInfo"
    elif option==6:
        filename="ResourcesSystemNetInfo"
    elif option==7:
        filename="AuditFolPer.txt"
    else:
        pass

    if option in [1,2,3,4,5,6,7]:
        
    
        now = datetime.now()
        now=now.date()
        path = os.getcwd()

        
        script_path = r"\PowerShell\menu_ps.ps1"
        
        # Ejecuta el script y muestra los resultados directamente en la terminal
        process= subprocess.Popen(
        ["powershell", "-command", f"./{script_path} -op '{option}'"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,)


        extension = ".txt"
        counter = 1
        full_path = os.path.join(path,filename+extension)
        while os.path.exists(full_path):
            full_path = os.path.join(path, f"{filename}({counter}){extension}")
            counter += 1



        f = open(full_path, "w")
        for a in process.stdout:
            f.write(a)
        f.close()

        with open(full_path, "rb") as f:

        # Read the contents of the file
            contents = f.read()

            # Generate the SHA-256 hash of the contents
            hash_object = hashlib.sha256(contents)

            # Return the hexadecimal representation of the hash
            hash= hash_object.hexdigest()


        print("Se ejecuto opcion ",filename)
        print("Fecha de ejecucion:",now)
        print("El hash del archivo es: ",hash)
        print(f"Ruta: ",full_path)
        input()
        system("cls")


    else:
        pass

    return 0



def main():
    # Inicializar colorama para uso de colores en la salida
    init(autoreset=True)



    if opsis=="nt":
        logging.info("Inicio del programa principal.")
        while True:
            system("cls")  # Limpiar la pantalla
            show_menuW()
            option = input("Selecciona una opción: ")
            if not execute_moduleW(option):
                break
        logging.info("Fin del programa principal.")
    elif opsis=="posix":
        logging.info("Inicio del programa principal.")
        while True:
            system("cls")  # Limpiar la pantalla
            show_menuL()
            option = input("Selecciona una opción: ")
            if not execute_moduleL(option):
                break
        logging.info("Fin del programa principal.")
    
information="""
    Este script de ciberseguridad tiene diversas tareas de cibersegudiad que puede resultar
    muy utiles para cualquier persona , ya sea que tenga Linux o Windows. 
    Nota importante: en caso de ingresar una API KEY invalida se podra agregar otra 
    """

parser = argparse.ArgumentParser(description=information,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-Apikey1', '--Shodan', help="Api key valida para Shodan",required=True,type=str)
parser.add_argument('-Apikey2', '--Database', help="Api key valida para Database",required=True,type=str)

if __name__ == "__main__":
    opsis=os.name
    
    args = parser.parse_args()
    Apikey1=args.Shodan
    Apikey2=args.Database
    
    file=open("APIKShodan.txt","w")
    file.write(Apikey1)
    file.close()

    file2=open("APIKDataBase.txt","w")
    file2.write(Apikey2)
    file2.close()
    main()

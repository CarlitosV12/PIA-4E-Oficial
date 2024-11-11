#!/usr/bin/python

import shodan
import ipaddress
import logging
import os
import hashlib
from datetime import datetime
from os import system
from colorama import init, Fore

#Función para leer la API por el archivo de texto generado por argparse
def arg_sho(filename3):
    ct_dir = os.path.dirname(__file__)
    full_path3 = os.path.join(ct_dir,filename3)

    if os.path.exists(full_path3):
        with open(full_path3, "r") as doc2:
            body3 = doc2.read()
        API_key = body3
        
        try:
            api = shodan.Shodan(API_key)
            api.info()  # Validar API key con una consulta de prueba
            logging.info("API Key válida.")
            return api
        except shodan.APIError as e:
            logging.error(f"Error con el API Key: {e}")
            print("API Key ingresada por argparse inválida.")
    else:
        print(f"No se encontró el archivo {filename3} en la ruta {ct_dir}.\nPor favor, ingrese manualmente un API key válida.\n")
        return None

#Función que guarda la última IP
def save_ip(filename2, body2):
    path2 = os.getcwd()
    extension2 = ".txt"
    counter2 = 1
    full_path2 = os.path.join(path2, filename2 + extension2)

    while os.path.exists(full_path2):
        full_path2 = os.path.join(path2, f"{filename2}({counter2}){extension2}")
        counter2 += 1
    
    with open(full_path2, "a") as doc:
        doc.write(body2)
    
    print(f"Última IP guardada en: {full_path2}\n")

#Función que maneja los reportes en txt
def write_arc(filename, body):
    path = os.getcwd()
    extension = ".txt"
    counter = 1
    full_path = os.path.join(path, filename + extension)

    while os.path.exists(full_path):
        full_path = os.path.join(path, f"{filename}({counter}){extension}")
        counter += 1
    
    with open(full_path, "a") as doc:
        doc.write(body)
    
    with open(full_path,"rb") as f:
        contents = f.read()
        hash_object = hashlib.sha256(contents)
        hash = hash_object.hexdigest()

    now = datetime.now().date()

    print(f"Fecha en la que se realizó la tarea: {now}\n")
    print(f"Resultados guardados en: {full_path}\n")
    print(f"Hash SHA-256 del archivo con los resultados: {hash}\n")

# Configuracion del loggin 
logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo de mensajes que se registrarán
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de los mensajes
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
    filename='shodan.log',  # Archivo donde se guardarán los logs
    filemode='a'  # Modo de escritura a para no sobreescribir 
)

# Función para validar el API Key
def validate_API_key(max_attempts=3):
    attempts = 0  # Contador de intentos

    while attempts < max_attempts:
        API_key = input("Ingresa un API Key válida para Shodan: ")
        
        try:
            # Inicializar el cliente de Shodan
            api = shodan.Shodan(API_key)
            
            # Intentar realizar una consulta simple para verificar si el API key es válido
            api.info()
            logging.info("API Key válida.")
            return api
        except shodan.APIError as e:
            logging.error(f"Error con el API Key: {e}")
            print("API Key inválida. Inténtalo de nuevo.")
            attempts += 1  # Incrementar el contador de intentos

    print("Has excedido el número máximo de intentos.")
    logging.error("Número máximo de intentos alcanzado para la clave API de Shodan.")
    print("Presione enter para continuar ")
    input()
    return None  # Devolver None si no se ingresó una clave válida

# Función para validar una dirección IP
def validate_IP(ip):
    try:
        # Usar el módulo ipaddress para verificar si es una IP válida
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Función para buscar dispositivos y recopilar información
def find_devices(api, consult):
    try:
        # Realizar la búsqueda en Shodan
        results = api.search(consult)
        logging.info(f'Resultados encontrados para "{consult}": {results["total"]}')

        filename = "APIShodan"
        total_body = ""
        total_body += "Resultados encontrados:\n\n"

        # Recorrer los resultados y mostrar información clave
        for device in results['matches']:
            ip = device['ip_str']
            port = device['port']
            organization = device.get('org', 'Desconocido')
            operative_system = device.get('os', 'Desconocido')

            logging.info(f'IP: {ip}, Puerto: {port}, Organización: {organization}, Sistema Operativo: {operative_system}')
            """print(f"IP: {ip}")
            print(f"Puerto: {port}")
            print(f"Organización: {organization}")
            print(f"Sistema Operativo: {operative_system}")
            print("-" * 50)"""

            body_cycle = f"\nIP: {ip}\n"
            body_cycle2 = f"Puerto: {port}\n"
            body_cycle3 = f"Organización: {organization}\n"
            body_cycle4 = f"Sistema Operativo: {operative_system}\n\n"
            body_cycle5 = "-" * 50
            body_cycle6 = "\n"
            total_body += body_cycle
            total_body += body_cycle2
            total_body += body_cycle3
            total_body += body_cycle4
            total_body += body_cycle5
            total_body += body_cycle6
        filename2 = "LastIP"
        total_body2 = f"{ip}"
        print("")
        save_ip(filename2,total_body2)
        print("Presione enter para continuar ")
        input()

    except shodan.APIError as e:
        logging.error(f'Error en la búsqueda: {e}')
        print("Presione enter para continuar ")
        input()
    print("Tarea que se ejecutó: Buscar dispositivos\n")
    write_arc(filename,total_body)
    print("Presione enter para continuar")
    input()

# Función para buscar vulnerabilidades en un dispositivo específico
def find_vulnerabilities(api, ip):
    try:
        # Obtener detalles del host en Shodan
        host = api.host(ip)
        logging.info(f'Información del dispositivo {ip}:')
        """print(f"Información del dispositivo {ip}:")
        print(f"País: {host.get("country_name", "Desconocido")}")
        print(f"Sistema Operativo: {host.get("os", "Desconocido")}")
        print(f"Puertos Abiertos: {host["ports"]}")"""

        filename = "APIShodan"
        total_body = ""
        total_body += "Resultados:\n\n"

        total_body += f"Información del dispositivo {ip}:\n"
        total_body += f"País: {host.get("country_name", "Desconocido")}\n"
        total_body += f"Sistema Operativo: {host.get("os", "Desconocido")}\n"
        total_body += f"Puertos Abiertos: {host["ports"]}\n"

        # Mostrar las vulnerabilidades encontradas
        if 'vulns' in host:
            logging.info('Vulnerabilidades encontradas:')
            """print("Vulnerabilidades encontradas:")"""
            total_body += "Vulnerabilidades encontradas:\n"
            for vulnerability in host['vulns']:
                cve = vulnerability.split(':')[-1]
                logging.info(f'CVE: {cve}')
                """print(f"CVE: {cve}")"""
                body_cycle = f"CVE: {cve}\n"
                total_body += body_cycle
        else:
            logging.info('No se encontraron vulnerabilidades.')
            print('No se encontraron vulnerabilidades.')
        print("Presione enter para continuar ")
        input()

    except shodan.APIError as e:
        logging.error(f'Error obteniendo detalles del host: {e}')
        print("Presione enter para continuar ")
        input()
    print("Tarea que se ejecutó: Buscar vulnerabilidades en un dispositivo\n")
    write_arc(filename,total_body)
    print("Presione enter para continuar")
    input()

# Función para mostrar el menú de consultas predefinidas
def select_consult():
    print("\n--- Selecciona una consulta ---")
    consults = ['apache', 'nginx', 'IIS', 'ftp', 'ssh']
    for i, consult in enumerate(consults, 1):
        print(f"{i}. {consult}")
    option = input("Selecciona una opción (1-5): ")

    # Validar que la opción ingresada sea correcta
    if option.isdigit() and 1 <= int(option) <= 5:
        return consults[int(option) - 1]
    else:
        logging.warning("Opción no válida en selección de consulta.")
        print("Opción no válida. Intenta de nuevo.")
        return select_consult()

# Función para mostrar el menú y ejecutar las funciones según la elección
def show_menu(api):
    while True:
        system("cls")  # Limpiar la pantalla
        print("""      
              
        ░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗
        ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║
        ╚█████╗░███████║██║░░██║██║░░██║███████║██╔██╗██║
        ░╚═══██╗██╔══██║██║░░██║██║░░██║██╔══██║██║╚████║
        ██████╔╝██║░░██║╚█████╔╝██████╔╝██║░░██║██║░╚███║
        ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝
              
        """)
        print("\n--- Menú de Shodan ---")
        print("1. Buscar dispositivos")
        print("2. Buscar vulnerabilidades en un dispositivo")
        print("3. Salir")
        option = input("Selecciona una opción: ")

        if option == '1':
            consult = select_consult()
            find_devices(api, consult)
        elif option == '2':
            ip = input("Ingresa la IP del dispositivo para buscar vulnerabilidades: ")
            
            # Validar la IP antes de proceder
            if validate_IP(ip):
                find_vulnerabilities(api, ip)
            else:
                logging.warning("IP no válida ingresada.")
                print("IP no válida. Por favor, ingresa una IP correcta.")
                print("Presione enter para continuar ")
                input()
        elif option == '3':
            logging.info("Salida del programa.")
            print("Saliendo...")
            break
        else:
            logging.warning("Opción no válida en el menú principal.")
            print("Opción no válida. Intenta de nuevo.")

# Programa principal
def main():
    # Inicializar colorama para uso de colores en la salida
    init(autoreset=True)

    # Llamar a validate_API_key en lugar de pedir API_key directamente
    api = arg_sho("APIKShodan.txt")
    if api is None:
        api = validate_API_key()  # Validar la clave API sin necesidad de pasarla como argumento

    if api:
        # Mostrar el menú de opciones
        show_menu(api)
    else:
        logging.error("No se puede continuar sin un API Key válido.")
        print("No se puede continuar sin un API Key válido.")

# Ejecutar el programa principal si el script se llama directamente
if __name__ == "__main__":
    main()

#!/usr/bin/python

import requests
import logging
import os
import hashlib
from datetime import datetime
from os import system
from colorama import init, Fore

#Función para leer la API por el archivo de texto generado por argparse
def arg_abu(filename3):
    ct_dir = os.path.dirname(__file__)
    full_path3 = os.path.join(ct_dir,filename3)

    if os.path.exists(full_path3):
        with open(full_path3, "r") as doc2:
            body3 = doc2.read()
        api_key = body3
        
        if len(api_key) == 80:  # Asumiendo que las API Keys son de 80 caracteres
            logging.info("Clave API válida ingresada.")
            return api_key
        else:
            logging.warning("Clave API inválida ingresada. Debe tener 80 caracteres.")
            print("\nLa clave API ingresada en el argparse es inválida.\nPor favor, ingrese manualmente un API key válida.\n")
    else:
        print(f"\nNo se encontró el archivo {filename3} en la ruta {ct_dir}.\nPor favor, ingrese manualmente un API key válida.\n")
        return None


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
    filename='ip_abuse.log',  # Archivo donde se guardarán los logs
    filemode='a'  # Modo de escritura a para no sobreescribir 
)

# Función para solicitar la clave API
def validate_api_key(max_attempts=3):
    attempts = 0  # Contador de intentos

    while attempts < max_attempts:
        api_key = input("Ingresa un API Key válida: ")
        
        if len(api_key) == 80:  # Asumiendo que las API Keys son de 80 caracteres
            logging.info("Clave API válida ingresada.")
            return api_key
        else:
            logging.warning("Clave API inválida ingresada. Debe tener 80 caracteres.")
            print("Clave API inválida. Inténtalo de nuevo.")
            attempts += 1  # Incrementar el contador de intentos

    print("Has excedido el número máximo de intentos.")
    logging.error("Número máximo de intentos alcanzado para la clave API.")
    print("Presione enter para continuar ")
    input()
    return None  # Devolver None si no se ingresó una clave válida

# URL base de la API de IP Abuse
URL = 'https://api.abuseipdb.com/api/v2/check'

# Función para buscar información de una IP
def search_ip_abuse(ip_address, api_key):
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'  # Tiempo en días para los reportes
    }

    # Realizar la solicitud a la API
    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()  # Lanza un error si la respuesta es 4xx o 5xx
        data = response.json()
        return data
    except requests.RequestException as e:
        logging.error(f"Error en la solicitud: {e}")
        print("Error al realizar la solicitud. Verifica la conexión y la clave API.")
        print("Presione enter para continuar ")
        input()
        return None

# Procesar y mostrar la información
def show_ip_info(data):
    if data:
        """print(f"Dirección IP: {data['data']['ipAddress']}")
        print(f"País: {data['data']['countryCode']}")
        print(f"Reportes totales: {data['data']['totalReports']}")
        print(f"Actividad abusiva: {data['data']['abuseConfidenceScore']}%")"""

        filename = "APIDataAbuse"
        total_body = ""
        total_body += f"Dirección IP: {data['data']['ipAddress']}\n"
        total_body += f"País: {data['data']['countryCode']}\n"
        total_body += f"Reportes totales: {data['data']['totalReports']}\n"
        total_body += f"Actividad abusiva: {data['data']['abuseConfidenceScore']}%\n"
        
        # Verificar si hay reportes disponibles
        if 'reports' in data['data'] and data['data']['reports']:
            # Mostrar los detalles de los reportes
            for report in data['data']['reports']:
                """print(f"Fecha del reporte: {report['reportedAt']}")
                print(f"Comentario: {report['comment']}")
                print("-----")"""

                body_cycle = f"Fecha del reporte: {report['reportedAt']}"
                body_cycle2 = f"Comentario: {report['comment']}"
                body_cycle3 = "-----"
                total_body += body_cycle
                total_body += body_cycle2
                total_body += body_cycle3
        else:
            print("No hay reportes disponibles para esta IP.")
    else:
        print("No se pudo obtener información.")
    print("Presione enter para continuar ")
    input()

# Función para ejecutar la búsqueda de IP
def main():
    # Inicializar colorama para uso de colores en la salida
    init(autoreset=True)

    API_key = arg_abu("APIKDataBase.txt")
    if API_key is None:
        validate_api_key()  # Solicitar la clave API al inicio de la función main
    
    if API_key is None:
        print("No se pudo obtener una clave API válida. Saliendo del módulo.")
        return  # Salir si no se obtuvo una clave válida

    while True:
        system("cls")  # Limpiar la pantalla
        print("""\
        
        ██╗██████╗░  ██████╗░░█████╗░████████╗░█████╗░
        ██║██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
        ██║██████╔╝  ██║░░██║███████║░░░██║░░░███████║
        ██║██╔═══╝░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
        ██║██║░░░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
        ╚═╝╚═╝░░░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

        ░█████╗░██████╗░██╗░░░██╗░██████╗███████╗
        ██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔════╝
        ███████║██████╦╝██║░░░██║╚█████╗░█████╗░░
        ██╔══██║██╔══██╗██║░░░██║░╚═══██╗██╔══╝░░
        ██║░░██║██████╦╝╚██████╔╝██████╔╝███████╗
        ╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═════╝░╚══════╝
              
        """)
        target = input("Ingresa la dirección IP que deseas consultar (o 'salir' para terminar): ")
        if target.lower() == 'salir':
            logging.info("El usuario ha decidido salir.")
            break
        info_ip = search_ip_abuse(target, API_key)  # Pasar la API key a la función
        show_ip_info(info_ip)

if __name__ == "__main__":
    main()

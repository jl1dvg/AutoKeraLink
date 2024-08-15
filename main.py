# main.py
from serial_config import connect_serial
from data_processor import process_data
from server import run_server
import threading

def read_from_serial(ser):
    while True:
        data = ser.readline()
        if data:
            processed_data = process_data(data)
            if processed_data:
                # Aquí puedes enviar los datos al servidor o almacenarlos para la consulta
                print(f"Datos listos para enviar al servidor: {processed_data}")

if __name__ == "__main__":
    ser = connect_serial('/dev/ttyUSB0', 9600)
    if ser:
        # Iniciar un hilo separado para ejecutar el servidor Flask
        server_thread = threading.Thread(target=run_server)
        server_thread.start()

        # Leer continuamente desde el puerto serial
        read_from_serial(ser)

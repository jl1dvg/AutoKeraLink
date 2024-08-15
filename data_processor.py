# data_processor.py

def process_data(data):
    try:
        # Aquí puedes agregar lógica para procesar los datos según el formato del HRK-8000A
        decoded_data = data.decode('utf-8').strip()
        print(f"Datos procesados: {decoded_data}")
        return decoded_data
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
        return None

# serial_config.py
import serial

def connect_serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=timeout
        )
        print("Conexión con el autorrefractor establecida.")
        return ser
    except serial.SerialException as e:
        print(f"Error al conectar con el puerto serial: {e}")
        return None

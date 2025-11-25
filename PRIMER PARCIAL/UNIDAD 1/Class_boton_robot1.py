import time
import RPi.GPIO as GPIO

# Intentamos importar Adafruit_DHT, si falla lo atrapamos y seguimos (modo "simulado")
try:
    import Adafruit_DHT
    _HAS_DHT = True
except Exception as e:
    Adafruit_DHT = None
    _HAS_DHT = False
    print("ADVERTENCIA: no se encontró la librería Adafruit_DHT. "
          "Las lecturas DHT serán simuladas. Para instalar: sudo pip3 install Adafruit-DHT")

# ===================== CLASE BASE =====================
class Robot:
    def __init__(self, nombre, modelo, pin_led=18):
        self.nombre = nombre
        self.modelo = modelo
        self.pin_led = pin_led

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_led, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin_led, True)
        print(f"{self.nombre} encendido")

    def apagar(self):
        GPIO.output(self.pin_led, False)
        print(f"{self.nombre} apagado")

    def estado(self):
        print(f"Robot: {self.nombre}, Modelo: {self.modelo}")


# ===================== CLASE HIJA: EXPLORADOR =====================
class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona_exploracion):
        super().__init__(nombre, modelo)
        self.zona_exploracion = zona_exploracion

        self.pin_boton = 25
        self.pin_led = 18

        GPIO.setup(self.pin_boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pin_led, GPIO.OUT)

    def explorar(self):
        print(f"{self.nombre} está explorando la zona: {self.zona_exploracion}")

    def detectar_pulsador(self):
        print("Robot listo. Presiona el pulsador para iniciar exploración...")
        while True:
            if GPIO.input(self.pin_boton) == GPIO.LOW:
                GPIO.output(self.pin_led, True)
                print("Explorando...")
                time.sleep(0.5)
            else:
                GPIO.output(self.pin_led, False)
                time.sleep(0.1)

class RobotObrero(Robot):
    def __init__(self, nombre, modelo, tarea):
        super().__init__(nombre, modelo)
        self.tarea = tarea

    def trabajar(self):
        print(f"{self.nombre} está realizando la tarea: {self.tarea}")


# ===================== CLASE HIJA: MÉDICO (robusta) =====================
class RobotMedico(Robot):
    def __init__(self, nombre, modelo, pin_dht=4, tipo_dht=None):
        # No usamos Adafruit_DHT en la firma para evitar errores si no está instalado
        super().__init__(nombre, modelo)
        self.pin_dht = pin_dht
        # Si el usuario no pasa tipo_dht, asignamos uno solo si la librería está disponible
        if tipo_dht is not None:
            self.tipo_dht = tipo_dht
        else:
            if _HAS_DHT:
                self.tipo_dht = Adafruit_DHT.DHT11  # por defecto si la librería existe
            else:
                self.tipo_dht = None  # modo simulación / no disponible

    def medir_temperatura(self):
        """Lee los valores del sensor DHT; si no hay librería, simula una lectura."""
        if not _HAS_DHT or self.tipo_dht is None:
            # Simulación para pruebas sin hardware
            print("Modo SIMULADO: lectura DHT (no hay Adafruit_DHT).")
            temperatura = 36.6
            humedad = 45.0
            print(f"Temperatura simulada: {temperatura:.1f}°C  |  Humedad: {humedad:.1f}%")
            return temperatura, humedad

        humedad, temperatura = Adafruit_DHT.read_retry(self.tipo_dht, self.pin_dht)
        if humedad is not None and temperatura is not None:
            print(f"Temperatura: {temperatura:.1f}°C  |  Humedad: {humedad:.1f}%")
            return temperatura, humedad
        else:
            print("Error al leer el sensor DHT. Verifica la conexión y el pin.")
            return None, None

    def monitorear_paciente(self):
        print(f"{self.nombre} está monitoreando la temperatura del paciente...")
        try:
            while True:
                temp, hum = self.medir_temperatura()
                if temp is not None:
                    if temp > 37.5:
                        print("⚠️ Temperatura alta detectada. Activando alerta visual...")
                        GPIO.output(self.pin_led, True)
                    else:
                        GPIO.output(self.pin_led, False)
                time.sleep(2)
        except KeyboardInterrupt:
            print("Monitoreo detenido por usuario.")
            GPIO.cleanup()


# ===================== SIMULACIÓN =====================
def simulacion_robots():
    # Prueba el médico. Si no tienes el sensor o la librería, funcionará en modo simulado.
    
    
    medico = RobotMedico("Robot_Medico", "HM-7", pin_dht=4)
    medico.encender()
    medico.estado()
    medico.monitorear_paciente()
    explorador=RobotExplorador("Robor explorador","HM2", "Marte")
    obrero = RobotObrero("R-Worker", "MK-3", "Construcción de puente")

    explorador.encender()
    explorador.explorar()
    explorador.estado()
    explorador.apagar()
    
    obrero.encender()
    obrero.trabajar()
    obrero.estado()
    obrero.apagar()

if __name__ == "__main__":
    simulacion_robots()


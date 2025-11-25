import RPi.GPIO as GPIO
import time

class Robot:
    def __init__(self, nombre, modelo, pin_led=18):
        self.nombre = nombre
        self.modelo = modelo
        self.pin_led = pin_led

        # Configurar GPIO una sola vez
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_led, GPIO.OUT)
        GPIO.output(self.pin_led, False)

    def encender(self):
        GPIO.output(self.pin_led, True)
        print(f"{self.nombre} encendido (LED ON)")

    def apagar(self):
        GPIO.output(self.pin_led, False)
        print(f"{self.nombre} apagado (LED OFF)")

    def estado(self):
        print(f"Robot: {self.nombre}, Modelo: {self.modelo}")


# === CLASE HIJA: RobotExplorador ====
class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona_exploracion, pin_boton=25,):
        super().__init__(nombre, modelo)
        self.zona_exploracion = zona_exploracion

        # Configurar pulsador
        self.pin_boton = pin_boton
        GPIO.setup(self.pin_boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def explorar(self):
        print(f"{self.nombre} está explorando la zona: {self.zona_exploracion}")

    def detectar_pulsador(self):
        print("Robot listo. Presiona el pulsador para iniciar exploración...")

        while True:
            if GPIO.input(self.pin_boton) == GPIO.LOW:
                GPIO.output(self.pin_led, True)
                print("explorando…")
                time.sleep(0.5)
            else:
                GPIO.output(self.pin_led, False)
                time.sleep(0.1)


# ==== CLASE HIJA: RobotObrero =====
class RobotObrero(Robot):
    def __init__(self, nombre, modelo, tarea, pin_led=18):
        super().__init__(nombre, modelo, pin_led)
        self.tarea = tarea

    def trabajar(self):
        print(f"{self.nombre} está realizando la tarea: {self.tarea}")


# ===================== SIMULACIÓN =====================
def simulacion_robots():

    # ----- Robot Explorador: usa pulsador -----
    explorador = RobotExplorador("Robot_Explorador", "XJ-9", "Zona A1")
    explorador.encender()
    explorador.estado()
# robot obrero para prender el led
    obrero1=RobotObrero()
    obrero1.encender()
    obrero1.apagar()
    obrero1.trabajar()
	
    # Comienza detección del pulsador
    explorador.detectar_pulsador()

# Inicio del programa
simulacion_robots()

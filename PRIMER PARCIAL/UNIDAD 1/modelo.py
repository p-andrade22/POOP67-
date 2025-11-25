# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:32:31 2025

@author: ESTUDIANTE
"""

# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import adafruit_dht
import board

# === CONFIGURACIÓN GENERAL ===
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN_LED = 18
PIN_BOTON = 25

GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BOTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LOG_FILE = "data_log.txt"     # Archivo donde se guardan los datos


# === FUNCIÓN GENERAL DE LOG ===
def escribir_log(texto):
    with open(LOG_FILE, "a") as f:
        f.write(texto + "\n")


# === CLASE PADRE ===
class Robot:
    def __init__(self, nombre):
        self.nombre = nombre

    def contar_uso(self):
        escribir_log(f"[USO] Robot {self.nombre} llamado - {time.ctime()}")


# === ROBOT CONSTRUCTOR ===
class RobotConstructor(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)

    def encender(self):
        self.contar_uso()
        GPIO.output(PIN_LED, True)
        return "🤖 Constructor encendido (LED ON)"

    def apagar(self):
        self.contar_uso()
        GPIO.output(PIN_LED, False)
        return "🤖 Constructor apagado (LED OFF)"


# === ROBOT MEDICO ===
class RobotMedico(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.sensor = adafruit_dht.DHT11(board.D4)

    def medir_temperatura(self):
        self.contar_uso()
        try:
            time.sleep(2)
            t = self.sensor.temperature
            escribir_log(f"[DHT] Temperatura: {t}°C - {time.ctime()}")
            return f"🌡️ Temperatura: {t}°C"
        except:
            return "⚠️ Error al leer temperatura."

    def medir_humedad(self):
        self.contar_uso()
        try:
            time.sleep(2)
            h = self.sensor.humidity
            escribir_log(f"[DHT] Humedad: {h}% - {time.ctime()}")
            return f"💧 Humedad: {h}%"
        except:
            return "⚠️ Error al leer humedad."


# === ROBOT EXPLORADOR ===
class RobotExplorador(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)

    def explorar(self):
        self.contar_uso()

        # Esperar a presionar
        while GPIO.input(PIN_BOTON) == GPIO.HIGH:
            time.sleep(0.01)

        GPIO.output(PIN_LED, True)
        escribir_log("[EXPLORACION] Inicio de exploración")

        # Mientras esté presionado
        while GPIO.input(PIN_BOTON) == GPIO.LOW:
            print("Explorando...")
            time.sleep(0.2)

        # Soltado
        GPIO.output(PIN_LED, False)
        escribir_log("[EXPLORACION] Fin de exploración")

        return "🛑 Robot explorador ha dejado de explorar"

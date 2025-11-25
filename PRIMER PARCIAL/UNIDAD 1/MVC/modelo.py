# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:55:03 2025

@author: ESTUDIANTE
"""

# modelo.py

import gpiozero
import Adafruit_DHT

# ------------------------------
# Clase base Robot
# ------------------------------
class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

    def encender(self):
        print(f"{self.nombre} está encendido.")

    def apagar(self):
        print(f"{self.nombre} está apagado.")

    def estado(self):
        print(f"Robot: {self.nombre}, Modelo: {self.modelo}")


# ------------------------------
# Robot explorador (con pulsador)
# ------------------------------
class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona_exploracion, pin_pulsador):
        super().__init__(nombre, modelo)
        self.pulsador = gpiozero.Button(pin_pulsador)
        self.zona_exploracion = zona_exploracion

    def explorar(self):
        if self.pulsador.is_pressed:
            return f"{self.nombre} está explorando la zona: {self.zona_exploracion}"
        else:
            return None


# ------------------------------
# Robot obrero (LED controlable)
# ------------------------------
class RobotObrero(Robot):
    def __init__(self, nombre, modelo, tarea, pin_led):
        super().__init__(nombre, modelo)
        self.tarea = tarea
        self.led = gpiozero.LED(pin_led)

    def trabajar(self):
        return f"{self.nombre} está realizando la tarea: {self.tarea}"

    def encender_led(self):
        self.led.on()
        return f"{self.nombre}: LED encendido."

    def apagar_led(self):
        self.led.off()
        return f"{self.nombre}: LED apagado."


# ------------------------------
# Robot médico (DHT11)
# ------------------------------
class Robot_Medico(Robot):
    DHT_SENSOR = Adafruit_DHT.DHT11

    def __init__(self, nombre, modelo, especialidad, pin_data):
        super().__init__(nombre, modelo)
        self.especialidad = especialidad
        self.pin_data = pin_data

    def diagnosticar(self):
        return f"{self.nombre} ha diagnosticado {self.especialidad}"

    def leer_temperatura(self):
        humedad, temperatura = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.pin_data)
        if temperatura is not None:
            return round(temperatura, 1)
        return None

    def leer_humedad(self):
        humedad, temperatura = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.pin_data)
        if humedad is not None:
            return round(humedad, 1)
        return None

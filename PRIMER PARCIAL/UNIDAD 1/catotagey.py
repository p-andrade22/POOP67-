# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 14:33:04 2025

@author: ESTUDIANTE
"""

import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

class RobotMedico:
    def __init__(self, nombre, modelo, pin_dht=board.D4, pin_led=18):
        self.nombre = nombre
        self.modelo = modelo
        self.pin_led = pin_led
        self.dht_device = adafruit_dht.DHT11(pin_dht)

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_led, GPIO.OUT)

    def medir_temperatura(self):
        try:
            temperatura = self.dht_device.temperature
            humedad = self.dht_device.humidity
            if temperatura is not None and humedad is not None:
                print(f"Temperatura: {temperatura:.1f}°C | Humedad: {humedad:.1f}%")
                return temperatura, humedad
            else:
                print("Lectura no válida del sensor.")
                return None, None
        except RuntimeError as err:
            print(f"Error de lectura: {err}")
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
            print("Monitoreo detenido por el usuario.")
            GPIO.cleanup()

if __name__ == "__main__":
    medico = RobotMedico("Robot_Medico", "HM-7")
    medico.monitorear_paciente()

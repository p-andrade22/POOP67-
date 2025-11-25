# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:55:26 2025

@author: ESTUDIANTE
"""

# controlador.py

from modelo import RobotExplorador, RobotObrero, Robot_Medico

class Controlador:
    def __init__(self):
        # Configuración de pines según tu Raspberry Pi
        self.robot_explorador = RobotExplorador("R-Explorer", "XJ-9", "Zona Ártica", pin_pulsador=17)  # BCM 17
        self.robot_obrero = RobotObrero("R-Worker", "MK-3", "Construcción de puente", pin_led=27)  # BCM 27
        self.robot_medico = Robot_Medico("WR-2", "UE16", "CARDIÓLOGO", pin_data=4)  # DHT11 GPIO4

    # Métodos para Telegram
    def encender_led(self):
        return self.robot_obrero.encender_led()

    def apagar_led(self):
        return self.robot_obrero.apagar_led()

    def explorar(self):
        return self.robot_explorador.explorar() or "No se está explorando"

    def diagnosticar(self):
        return self.robot_medico.diagnosticar()

    def temperatura(self):
        temp = self.robot_medico.leer_temperatura()
        return f"Temperatura: {temp}°C" if temp is not None else "Error al leer temperatura"

    def humedad(self):
        hum = self.robot_medico.leer_humedad()
        return f"Humedad: {hum}%" if hum is not None else "Error al leer humedad"

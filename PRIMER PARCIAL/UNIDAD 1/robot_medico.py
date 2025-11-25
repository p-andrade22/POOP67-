# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 14:36:22 2025

@author: ESTUDIANTE
"""

import RPi.GPIO as GPIO
import time
import adafruit_dht
import board

# ==== CONFIGURACIÓN GENERAL ====
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN_LED = 18
PIN_BOTON = 25

GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BOTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# ==== CLASE PADRE ====
class Robot:
    def _init_(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")

# ==== ROBOT CONSTRUCTOR ====
class RobotConstructor(Robot):
    def encender(self):
        GPIO.output(PIN_LED, True)
        print("🧱 Constructor encendido. LED ON (trabajando...)\n")

    def apagar(self):
        GPIO.output(PIN_LED, False)
        print("🧱 Constructor apagado. LED OFF\n")

# ==== ROBOT MÉDICO ====
class RobotMedico(Robot):
    def _init_(self, nombre):
        super()._init_(nombre)
        self.sensor = adafruit_dht.DHT11(board.D4)

    def diagnosticar(self):
        print("🩺 El médico está preparando los instrumentos...")
        time.sleep(2)
        print("¿Qué deseas medir?")
        print("1. Temperatura 🌡️")
        print("2. Humedad 💧")
        opcion = input("Selecciona una opción: ")

        # Espera a que el sensor se estabilice
        time.sleep(2)

        for intento in range(3):  # intenta hasta 3 veces leer el sensor
            try:
                t = self.sensor.temperature
                h = self.sensor.humidity

                if opcion == "1":
                    if t is not None:
                        print(f"🌡️ Temperatura actual: {t}°C\n")
                        break
                    else:
                        print("⚠️ No se pudo leer la temperatura, reintentando...")
                elif opcion == "2":
                    if h is not None:
                        print(f"💧 Humedad actual: {h}%\n")
                        break
                    else:
                        print("⚠️ No se pudo leer la humedad, reintentando...")
                else:
                    print("❌ Opción inválida.\n")
                    break

            except Exception as e:
                print(f"⚠️ Error al leer el sensor (intento {intento+1}/3): {e}")
                time.sleep(1)
        else:
            print("❌ No se pudo obtener datos del DHT11. Intenta nuevamente.\n")

# ==== ROBOT EXPLORADOR ====
class RobotExplorador(Robot):
    def explorar(self):
        print("🚀 Explorador listo.")
        print("👉 Mantén presionado el botón para EXPLORAR.")
        print("👉 Cuando sueltes el botón, se detiene y vuelve al menú.\n")

        # Espera hasta que el botón sea presionado por primera vez
        while GPIO.input(PIN_BOTON) == GPIO.LOW:
            time.sleep(0.01)

        print("🔎 Explorando... (mantén presionado el botón)")
        # Mientras el botón esté presionado, el LED se mantiene encendido
        while GPIO.input(PIN_BOTON) == GPIO.HIGH:
            GPIO.output(PIN_LED, True)
            # Pequeño delay para no saturar la CPU
            time.sleep(0.01)

        # Cuando suelta el botón:
        GPIO.output(PIN_LED, False)
        print("🛑 Exploración detenida. Volviendo al menú...\n")
        time.sleep(1)

# ==== CONTROLADOR ====
class Controlador:
    def _init_(self):
        self.constructor = RobotConstructor("Constructor")
        self.medico = RobotMedico("Médico")
        self.explorador = RobotExplorador("Explorador")

    def iniciar(self):
        while True:
            print("\n=== MENÚ DE CONTROL ===")
            print("1. Encender Constructor")
            print("2. Apagar Constructor")
            print("3. Activar Médico (medir temperatura o humedad)")
            print("4. Activar Explorador (mantén presionado el botón)")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.constructor.encender()
            elif opcion == "2":
                self.constructor.apagar()
            elif opcion == "3":
                self.medico.diagnosticar()
            elif opcion == "4":
                self.explorador.explorar()
            elif opcion == "5":
                print("👋 Cerrando programa...")
                GPIO.cleanup()
                break
            else:
                print("❌ Opción no válida\n")

# ==== PROGRAMA PRINCIPAL ====
if __name__ == "__main__":
    try:
        sistema = Controlador()
        sistema.iniciar()
    except KeyboardInterrupt:
        print("\n👋 Programa interrumpido por el usuario.")
    finally:
        GPIO.cleanup()

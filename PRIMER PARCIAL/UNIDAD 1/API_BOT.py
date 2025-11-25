# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:30:02 2025

@author: ESTUDIANTE
"""

import time
import datetime

# ===========================
#   CONFIGURACIÓN DEL GPIO
# ===========================
try:
    import RPi.GPIO as GPIO
    print("GPIO real detectado")
except ImportError:
    print("GPIO no encontrado. Usando simulación...")

    class FakeGPIO:
        BCM = "BCM"
        OUT = "OUT"

        @staticmethod
        def setmode(mode):
            print(f"[SIM GPIO] setmode({mode})")

        @staticmethod
        def setwarnings(flag):
            print(f"[SIM GPIO] setwarnings({flag})")

        @staticmethod
        def setup(pin, mode):
            print(f"[SIM GPIO] setup(pin={pin}, mode={mode})")

        @staticmethod
        def output(pin, value):
            estado = "HIGH (1)" if value else "LOW (0)"
            print(f"[SIM GPIO] Pin {pin} -> {estado}")

        @staticmethod
        def cleanup():
            print("[SIM GPIO] cleanup() ejecutado")

    GPIO = FakeGPIO


# ===========================
#         BOT TELEGRAM
# ===========================
import telepot
from telepot.loop import MessageLoop

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, 0)  # iniciar apagado


def action(msg):
    chat_id = msg['chat']['id']
    command = msg.get('text', '').lower()

    print("Comando recibido:", command)

    if command == "led on":
        GPIO.output(LED_PIN, 1)
        telegram_bot.sendMessage(chat_id, "✅ LED Encendido")

    elif command == "led off":
        GPIO.output(LED_PIN, 0)
        telegram_bot.sendMessage(chat_id, "✅ LED Apagado")

    else:
        telegram_bot.sendMessage(chat_id,
            "Comandos disponibles:\n"
            "🔹 led on\n"
            "🔹 led off"
        )


# ⚠️ IMPORTANTE: PON AQUÍ TU TOKEN CORRECTO
telegram_bot = telepot.Bot("AQUÍ_TU_TOKEN_REAL")
print("Bot info:", telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print("✅ Bot listo y escuchando comandos...")


# ===========================
#       BUCLE PRINCIPAL
# ===========================
try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print("Programa detenido")
    GPIO.cleanup()

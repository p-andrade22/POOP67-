# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:55:50 2025

@author: ESTUDIANTE
"""

# menu.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from controlador import Controlador
from vista import Vista

TOKEN = "7593988348:AAE0Cv0FYG8M9y4pJTr9L1GycWIqfRGBjg8"
controlador = Controlador()
vista = Vista()

# --------- Handlers ---------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Soy tu bot de robots.")

async def led_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(vista.mostrar(controlador.encender_led()))

async def led_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(vista.mostrar(controlador.apagar_led()))

async def explorar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    estado = controlador.explorar()
    await update.message.reply_text(vista.mostrar(estado))

async def diagnosticar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(vista.mostrar(controlador.diagnosticar()))

async def temperatura(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(vista.mostrar(controlador.temperatura()))

async def humedad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(vista.mostrar(controlador.humedad()))

# --------- Main ---------
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("led_on", led_on))
    app.add_handler(CommandHandler("led_off", led_off))
    app.add_handler(CommandHandler("explorar", explorar))
    app.add_handler(CommandHandler("diagnosticar", diagnosticar))
    app.add_handler(CommandHandler("temperatura", temperatura))
    app.add_handler(CommandHandler("humedad", humedad))

    print("Bot iniciado...")
    app.run_polling()

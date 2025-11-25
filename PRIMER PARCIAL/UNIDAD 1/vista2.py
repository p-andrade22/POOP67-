# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:33:03 2025

@author: ESTUDIANTE
"""

# -*- coding: utf-8 -*-

class TelegramView:
    def enviar(self, bot, chat_id, mensaje):
        bot.sendMessage(chat_id, mensaje)

    def menu_principal(self):
        return (
            "🤖 *Robots disponibles*\n\n"
            "/constructor_on\n"
            "/constructor_off\n"
            "/medico_temp\n"
            "/medico_hum\n"
            "/explorar\n"
            "/estado\n"
            "/salir\n"
        )

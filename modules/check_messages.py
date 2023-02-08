# -*- coding: utf-8 -*-
"""
    modules.check_messages
    ~~~~~~~~~~~~~~~~~~~~~~

    IMPRIME MENSAJES CON UNA DISTANCIA DE PUNTOS CON UN OK O UN FAIL.
    MIDEL EL MANAJE Y DE ACUERDO A ESO COLOCA LOS PUNTOS PARA QUE TODOS LOS
    MENSAJES ESTEN ALINADOS.

    :copyright: (c) 2023 by Jaime Feldman.
    :license: MIT, see LICENSE for more details.
"""

class ChkMessage:
    def __init__(self, point_number):
        self.number_points = point_number
    
    def message(self, message):
        self.message_len = len(message)
        print(message+"."*10)


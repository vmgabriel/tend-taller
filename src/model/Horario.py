#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependecias
import datetime
from datetime import date

class Horario:
    """
    Clase horario
    """
    def __init__(self, curso, fecha_inicio, fecha_fin, semestre):
        """
        Construccion del horario del estudiante

        @param curso: Curso Vinnculado al horario
        @param fecha_inicio: Fecha de inicio de clase
        @param fecha_fin: Fecha de finalizacion de clase
        @param semestre: Semestre que esta ubicado el horario

        @type curso: Curso
        @type fecha_inicio: datetime
        @type fecha_fin: datetime
        @type semestre: int
        """
        self.curso = curso
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.semestre = semestre

    def __str__(self):
        """
        Conversion de clase a str de Horario

        @return: Clase convertida a str
        @rtype: str
        """
        str_datos = """
        fecha de Inicio = {},
        fecha de Fin = {},
        semestre del horario = {}
        """.format(self.curso, self.fecha_inicio, self.fecha_fin, self.semestre)
        return str(self.curso) + str_datos

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

class Planificacion():
    """
    Clase de Planificacion de los estudiantes
    """
    def __init__(self, semestre):
        """
        Constructor de clase de Planificacion
        @param semestre: Semestre en el que se esta planificando
        @type semestre: integer
        """
        self.semestre = semestre
        self.cursos_a_tomar = []

    def __str__(self):
        """
        Convierte Clase a str

        @return: Clase convertida
        @rtype: str
        """
        cont = 0
        str_clase = ""
        for curso in self.cursos_a_tomar:
            cont += 1
            str_clase += " Clase {}: {}".format(cont, curso)
        return "Semestre {}".format(self.semestre) + str_clase

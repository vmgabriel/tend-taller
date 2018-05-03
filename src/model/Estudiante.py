#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependecias

# Modelo
from model.Persona import Persona

class Estudiante(Persona):
    """
    Clase de los estudiantes
    """
    def __init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia, dir_residencia, semestre, usuario, contra):
        """
        Constructor de estudiante, tiene datos de persona, quien es su super-clase
        """
        Persona.__init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia, dir_residencia, usuario, contra)
        self.semestre = semestre

    def __init__(self, datos):
        """
        Convierte una tupla y la genera en su respectiva clase, se identifica con ella para su tratamiento

        @param datos: datos en forma de tupla que se obtienen de una relacion de datos
        @type datos: tuple
        """
        Persona.__init__(self, datos[0][0], datos[0][1], datos[0][2], datos[0][3], datos[0][4], datos[0][5], datos[0][6], datos[0][7], datos[0][8], datos[0][11], datos[0][12])
        self.semestre = datos[0][9]
        self.consejero = datos[0][10]

    def es_is_graduado(self):
        """
        Retorna en español si esta graduado o no

        @return: Retorno de graduado en español
        @rtype: str
        """
        if (self.semestre == 11):
            return "si"
        else:
            return "no"

    def __str__(self):
        """
        Conversion de clase a str de Estudiante

        @return: Clase convertida a str
        @rtype: str
        """
        datos_persona = Persona.__str__(self)
        datos_estudiante = """Esta graduado?: {}
        """.format(self.es_is_graduado())
        return datos_persona + datos_estudiante

    def set_consejero(self, consejero):
        """
        Pone consejero a estudiante solo si esta graduado

        @param consejero: Profesor consejero que esta disponible
        @return: retron true si se puso consejero correctamente y false de no se estudiante graduado
        @type consejero: Profesor
        @rtype: bool
        """
        if (self.is_graduado):
            self.consejero = consejero
            return True
        return False

    def set_horario(self, horario):
        """
        Modifica y relaciona el horario dado

        @param horario: Horario que se va a vincular a estudiante
        @type horario: Horario
        """
        self.horario = horario

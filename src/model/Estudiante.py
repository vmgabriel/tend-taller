#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependecias
from Persona import Persona

class Estudiante(Persona):
    """
    Clase de los estudiantes
    """
    def __init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia, dir_residencia, semestre):
        """
        Constructor de estudiante, tiene datos de persona, quien es su super-clase

        @param is_graduado: Dato de si esta graduado o no

        @type is_graduado: bool
        """
        Persona.__init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia, dir_residencia)
        self.semestre = semestre

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
        datos_persona = Persona.__str__()
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

        @param planificion: Horario que se va a vincular a estudiante
        @type planificion: Horario
        """
        self.horario = horario

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencias
import datetime
from datetime import date

class Curso():
    """
    Clase Curso
    """
    def __init__(self, nombre, aula, tiempo, dia_reunion, edificio, id = 0):
        """
        Constructor de clase Curso

        @param nombre: Nombre del Curso
        @param aula: Aula donde se va hacer el curso
        @param id: Identificacion del curso
        @param tiempo: Tiempo en horas del curso
        @param dia_reunion: Fecha de Reunion
        @param edificio: Edificio donde es el lugar de Reunion

        @type nombre: str
        @type aula: str
        @type id: integer
        @type tiempo: double
        @type dia_reunion: datetime
        @type edificio: str
        """
        self.nombre = nombre
        self.aula = aula
        self.id = id
        self.profesor = None
        self.tiempo = tiempo
        self.dia_reunion = dia_reunion
        self.edificio = edificio

    def __str__(self):
        """
        Conversion de Clase a str

        @return: Conversion de Clase
        @rtype: str
        """
        str_clase = """Nombre de Curso: {},
        Aula de Curso: {},
        tiempo del Curso: {},
        Dia y Hora de Reunion: {},
        Edificio del Aula: {}
        Profesor a Cargo ->
        """.format(self.nombre, self.aula, self.tiempo, self.dia_reunion, self.edificio)
        str_profesor = str(self.profesor)
        return str_clase + str_profesor

    def set_profesor(self, profesor):
        """
        Pone profesor a cargo del curso

        @param profesor: Profesor encargado del curso
        @type profesor: Profesor
        """
        self.profesor = profesor

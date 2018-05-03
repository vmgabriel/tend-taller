#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencias
import datetime
from datetime import date

from model.Persona import Persona

class Profesor(Persona):
    """
    Clase de Profesor
    """
    def __init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia, dir_residencia, titulo, contrato, usuario, contra ,is_visitante = False, ini_nombramiento = None, fin_nombramiento = None):
        """
        Constructor de clase de Profesor

        @param is_visitante: Obtener si un profesor es visitante o no
        @param titulo: Titulo obtenido
        @param contrato: Contrato que se ha firmado ante la universidad para ejercer enseñanza
        @param ini_nombramiento: Fecha de inicio de Nombramiento solo si es profesor visitante
        @param fin_nombramiento: Fecha de fin de Nombramiento solo si es profesor visitante

        @type is_visitante: bool
        @type titulo: str
        @type contrato: str
        @type ini_nombramiento: datetime
        @type fin_nombramiento: datetime
        """
        Persona.__init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia, dir_residencia, usuario, contra)
        self.is_visitante = is_visitante
        self.contrato = contrato
        self.titulo = titulo
        self.departamento = None
        if (is_visitante):
            self.inicio_nombramiento = ini_nombramiento
            self.fin_nombramiento = fin_nombramiento

    def __init__(self, datos):
        """
        Constructor especificado para la implementacion directa de diseño de labase de datos a traves de la tupla

        @param datos: Tupla con los datos del profesor listos para ser identificados en la clase
        @type datos: tuple
        """
        Persona.__init__(self, datos[0][0], datos[0][1], datos[0][2], datos[0][3], datos[0][4], datos[0][5],
                         datos[0][6], datos[0][7], datos[0][8], datos[0][16], datos[0][15])
        self.is_visitante = datos[0][9]
        self.titulo = datos[0][10]
        self.contrato = datos[0][11]
        self.inicio_nombramiento = datos[0][12]
        self.fin_nombramiento = datos[0][13]
        self.departamento = datos[0][14]

    def es_is_visitante(self):
        """
        Retorna en español si esta visitante o no

        @return: Retorno de visitante en español
        @rtype: str
        """
        if (self.is_visitante):
            return "si"
        else:
            return "no"

    def __str__(self):
        """
        Conversion de clase a str de Profesor
        """
        datos_persona = Persona.__str__()
        datos_profesor = """Es visitante?: {},
        Titulo obtenido: {},
        Contrato: {},
        Departamento vinculado ->
        """.format(self.es_is_visitante(), self.contrato)
        datos_departamento = str(self.departamento)
        if (self.is_visitante):
            datos_profesor_especial = """---
            Inicio de Nombramiento: {},
            Fin de Nombramiento: {}
            """.format(self.inicio_nombramiento, self.fin_nombramiento)
            return datos_persona + datos_profesor + datos_profesor_especial + datos_departamento
        return datos_persona + datos_profesor + datos_departamento

    def set_departamento(self, departamento):
        """
        Pone el profesor en un departamento

        @param departamento: Departamento a cambiar

        @type departamento: Departamento
        """
        self.departamento = departamento

    def set_ini_nombramiento(self, fecha):
        """
        Modifica la fecha de inicio de nombramiento

        @param fecha: Fecha de nombramiento_ini

        @type fecha: date
        """
        self.inicio_nombramiento = fecha

    def set_fin_nombramiento(self, fecha):
        """
        Modifica la fecha de fin de nombramiento

        @param fecha: Fecha de nombramiento_fin

        @type fecha: date
        """
        self.fin_nombramiento = fecha

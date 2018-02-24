#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencias
import datetime
from datetime import date
from Persona import Persona

class Profesor(Persona):
    """
    Clase de Profesor
    """
    def __init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia, titulo, contrato ,is_visitante = False, ini_nombramiento = None, fin_nombramiento = None):
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
        Persona.__init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, lug_residencia)
        self.is_visitante = is_visitante
        self.contrato = contrato
        self.titulo = titulo
        self.departamento = None
        if (is_visitante):
            self.inicio_nombramiento = ini_nombramiento
            self.fin_nombramiento = fin_nombramiento

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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# Gabriel Vargas Monroy

class Persona(object):
    """
    Representacion de los datos basicos de la persona
    """
    def __init__(self, num, nombre1, nombre2, apellido1, apellido2, edad, lug_nacimiento, ciu_residencia, dir_residencia):
        """
        Constructor de Persona

        @param num: Numero de identificacion, Unico e Irrepetible
        @param nombre1: Primer nombre
        @param nombre2: Segundo nombre
        @param apellido1: Primer apellido
        @param apellido2: Segundo apellido
        @param edad: Edad de persona
        @param lug_nacimiento: Lugar de nacimiento
        @param ciu_residencia: Ciudad de Residencia
        @param dir_residencia: Direccin de Residencia

        @type num: integer
        @type nombre1: str
        @type nombre2: str
        @type apellido1: str
        @type apellido2: str
        @type edad: int
        @type lug_nacimiento: Ciudad
        @type ciu_residencia: Ciudad
        @type dir_residencia: str
        """
        self.num = num
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        self.lugar_nacimiento = lug_nacimiento
        self.ciudad_residencia = ciu_residencia
        self.direccion_residencia = dir_residencia

    def __str__(self):
        """
        Conversion a str de clase

        @return: Datos de clase en str
        @rtype: str
        """
        str_datos = """
        Identificacion: {},
        Nombre1: {},
        Nombre2: {}
        Apellido1: {},
        Apellido2: {},
        Edad: {},
        Lugar de Nacimiento {},
        Ciudad de Residencia Actual {},
        Direccion de Residencia Actual {}
        """.format(self.num, self.nombre1, self.nombre2, self.apellido1, self.apellido2, self.edad, self.lugar_nacimiento.get_nom(), self.ciudad_residencia.get_nom(), self.direccion_residencia)
        return str_datos

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

class Departamento():
    """
    Clase Departamento
    """
    def __init__(self, nombre, ciudad, telefono,id = 0):
        """
        Constructor de clase Departamento

        @param nombre: Nombre del Departamento
        @param ciudad: Ciudad donde esta el Departamento
        @param telefono: Telefono de contacto del Departamento
        @param id: Identificacion de Departamento

        @type nombre: str
        @type ciudad: Ciudad
        @type telefono: integer
        @type id: integer
        """
        self.nombre = nombre
        self.ciudad = ciudad
        self.telefono = telefono
        self.id = id

    def __str__(self):
        """
        Conversion de clase a str

        @return: Conversion de clase
        @rtype: str
        """
        str_clase = """Nombre de Departamento: {},
        Ciudad de Ubicacion de Departamento: {},
        Telefono de Contacto de Departamento: {}
        """.format(self.nombre, self.ciudad, self.telefono)
        return str_clase

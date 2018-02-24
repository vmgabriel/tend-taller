#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

class Ciudad():
    """
    Clase Ciudad, con datos especificos del mismo
    """
    def __init__(self, nombre, descripcion, id = 0):
        """
        Constructor de Ciudad

        @param nombre: Nombre de la Ciudad
        @param descripcion: descripcion de la Ciudad
        @param id: Identificacion de la Ciudad

        @type nombre: str
        @type descripcion: str
        @type id: integer
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.id = id

    def __str__(self):
        """
        Convierte clase a str

        @return: Str convertido de la clase
        @rtype: str
        """
        str_ciudad = """Nombre de la ciudad: {},
        descripcion de la ciudad: {}
        """.format(self.nombre, self.descripcion)
        return str_ciudad

    def set_id(self, id):
        """
        Modifica id de la ciudad

        @param id: Identificacion nueva
        @type id: integer
        """
        self.id = id

    def get_nom(self):
        """
        Retorna Nombre de la Ciudad

        @return: Nombre de la Ciudad
        @rtype: str
        """
        return self.nombre

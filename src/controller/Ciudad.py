#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Conexion con la base de datos
from model.conector import Conexion

class Ciudad_service:
    """
    Servicio de eventos para la ciudad, su estructura va formada como scripting
    """

    def __init__(self):
        """
        Constructor fachada
        """
        self.conexion = Conexion()

    def ver_todos(self):
        """
        Se obtienen todas las ciudades de la base de datos

        @return: Lista de ciudades en la base de datos
        @rtype: <class 'list'>
        """
        query = "SELECT * FROM ciudad;"
        consulta = self.conexion.enviar_consulta(query)
        return consulta

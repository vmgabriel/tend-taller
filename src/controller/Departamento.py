#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Conexion con la base de datos
from model.conector import Conexion

class Departamento_service:
    """
    Servicio de eventos para el Departamento, su estructura va formada como scripting
    """

    def __init__(self):
        """
        Constructor fachada
        """
        self.conexion = Conexion()

    def ver_todos(self):
        """
        Se obtienen todas las Departamento de la base de datos

        @return: Lista de departamentos en la base de datos
        @rtype: <class 'list'>
        """
        query = "SELECT * FROM departamento;"
        consulta = self.conexion.enviar_consulta(query)
        return consulta

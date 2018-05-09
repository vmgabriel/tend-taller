#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Conexion con la base de datos
from model.conector import Conexion

class Curso_service:
    """
    Servicio de eventos para los cursos, su estructura va formada como scripting
    """

    def __init__(self):
        """
        Constructor fachada
        """
        self.conexion = Conexion()

    def ver_todos(self):
        """
        Se obtienen todos los cursos de la base de datos

        @return: Lista de cursos en la base de datos
        @rtype: <class 'list'>
        """
        query = "SELECT * FROM curso;"
        consulta = self.conexion.enviar_consulta(query)
        return consulta

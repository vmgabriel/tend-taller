#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Conexion con la base de datos
from model.conector import Conexion

class Profesor_service:
    """
    Clase enfocada en la construccion de los eventos del servicio del profesor
    """
    def __init__(self):
        """
        Constructor enfocado en el diseccionamiento de los servicios
        """
        self.conexion = Conexion()

    def ver_todos(self, facultad=0):
        """
        Servicio/Metodo enfoca en ver todos por facultad

        @return: lista de todos los profesores en una facultad que estan en la base de datos
        @rtype: <class= 'list'>
        """
        if (facultad == 0):
            query = "SELECT * FROM profesor;"
            consulta = self.conexion.enviar_consulta(query)
            return consulta
        else:
            query = "SELECT * FROM profesor WHERE facultad = '{}';".format(facultad)
            consulta = self.conexion.enviar_consulta(query)
            return consulta

    def ver_todas_facultades(self):
        """
        Servicio/Metodo enfocado en la muestra de todas las facultades en la base de datos

        @return: lista de todas las facultades de la base de datos
        @rtype: <class= 'list'>
        """
        query = "SELECT * FROM departamento;"
        consulta = self.conexion.enviar_consulta(query)
        return consulta

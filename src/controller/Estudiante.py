#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Modelo
from model.Estudiante import Estudiante

# Conexion con la base de datos
from model.conector import Conexion

class Estudiante_service:
    """
    Servicio de eventos para el estudiante, su estructura va formada como scripting
    """

    def __init__(self):
        """
        Constructor fachada
        """
        self.conexion = Conexion()

    def guardar(self, estudiante):
        """
        Guarda el estudiante actual en la base de datos

        @param estudiante: estudiante y sus respectivos datos
        @type: <class= 'Estudiante'>

        @return: guardado satisfactorio
        @rtype: boolean
        """
        profesor = estudiante.consejero
        if (not profesor):
            profesor = "NULL"
        query = """INSERT INTO estudiante(
        id_estudiante,
        nombre1,
        nombre2,
        apellido1,
        apellido2,
        edad,
        lugar_nacimiento,
        ciudad_residencia,
        direccion_residencia,
        semestre,
        consejero,
        contra,
        usuario
        ) VALUES ({}, '{}', '{}', '{}', '{}', {}, {}, {}, '{}', {}, {}, '{}', '{}')""".format(estudiante.num,
                                                                                              estudiante.nombre1,
                                                                                              estudiante.nombre2,
                                                                                              estudiante.apellido1,
                                                                                              estudiante.apellido2,
                                                                                              estudiante.edad,
                                                                                              estudiante.lugar_nacimiento,
                                                                                              estudiante.ciudad_residencia,
                                                                                              estudiante.direccion_residencia,
                                                                                              estudiante.semestre,
                                                                                              profesor,
                                                                                              estudiante.contra,
                                                                                              estudiante.usuario)

        return (not self.conexion.enviar_registro(query))

    def ver_todos(self):
        """
        Retornara todos los datos del estudiante almacenados en la base de datos

        @return: Datos de la base de datos
        @rtype: [tuple]
        """
        query = "SELECT * FROM estudiante;"
        return self.conexion.enviar_consulta(query)

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

    def guardar(self, profesor):
        """
        Servicio/Metodo enfocado en el guardado de los datos del profesor

        @param profesor: Datos del profesor a introducir
        @type profesor: <class= 'Profesor'>

        @return: Retrna true si los datos se almacenaron correctamente
        @rtype: boolean
        """
        es_visitante = "FALSE"
        if (profesor.es_is_visitante() == "si"):
            es_visitante = "TRUE"

        query=""

        f1 = f2 = "NULL"

        if (profesor.inicio_nombramiento):
            f1 = "{}-{}-{}".format(profesor.inicio_nombramiento.year, profesor.inicio_nombramiento.month, profesor.inicio_nombramiento.day)
            f2 = "{}-{}-{}".format(profesor.fin_nombramiento.year, profesor.fin_nombramiento.month, profesor.fin_nombramiento.day)
            query = """
        INSERT INTO profesor(id_profesor, nombre1, nombre2, apellido1, apellido2, edad, lugar_nacimiento, ciudad_residencia, direccion_residencia, es_visitante, titulo, contrato, inicio_nombramiento, fin_nombramiento, facultad, contra, usuario) VALUES ({}, '{}', '{}', '{}', '{}', {}, {}, {}, '{}', {}, '{}', '{}', '{}', '{}', {}, '{}', '{}');
        """.format(profesor.num,
                   profesor.nombre1,
                   profesor.nombre2,
                   profesor.apellido1,
                   profesor.apellido2,
                   profesor.edad,
                   profesor.lugar_nacimiento,
                   profesor.ciudad_residencia,
                   profesor.direccion_residencia,
                   es_visitante,
                   profesor.titulo,
                   profesor.contrato,
                   f1,
                   f2,
                   profesor.departamento,
                   profesor.contra,
                   profesor.usuario)
        else:
            query = """
        INSERT INTO profesor(id_profesor, nombre1, nombre2, apellido1, apellido2, edad, lugar_nacimiento, ciudad_residencia, direccion_residencia, es_visitante, titulo, contrato, inicio_nombramiento, fin_nombramiento, facultad, contra, usuario) VALUES ({}, '{}', '{}', '{}', '{}', {}, {}, {}, '{}', {}, '{}', '{}', {}, {}, {}, '{}', '{}');
        """.format(profesor.num,
                   profesor.nombre1,
                   profesor.nombre2,
                   profesor.apellido1,
                   profesor.apellido2,
                   profesor.edad,
                   profesor.lugar_nacimiento,
                   profesor.ciudad_residencia,
                   profesor.direccion_residencia,
                   es_visitante,
                   profesor.titulo,
                   profesor.contrato,
                   f1,
                   f2,
                   profesor.departamento,
                   profesor.contra,
                   profesor.usuario)
        return (not self.conexion.enviar_registro(query))

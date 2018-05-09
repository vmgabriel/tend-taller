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

    def guardar(self, curso):
        """
        Servicio para guardado de datos del curso

        @param curso: Datos del curso al que se debe guardar en la base de datos
        @type curso: <clase= 'Curso'>

        @return: True si se guardaron los datos correctamente
        @rtype: boolean
        """
        f1 = "{}-{}-{}".format(curso.dia_reunion.year, curso.dia_reunion.month, curso.dia_reunion.day)
        query = """
            INSERT INTO curso(nombre, aula, tiempo, dia_reunion, edificio, profesor)
            VALUES ('{}', '{}', {}, '{}', {}, {});""".format(
                curso.nombre,
                curso.aula,
                curso.tiempo,
                f1,
                curso.edificio,
                curso.profesor
            )
        return (not self.conexion.enviar_registro(query))

    def cursos_profesor(self, profesor):
        """
        Muestra los cursos del profesor, espeficado, los que tiene administracion total

        @param profesor: Id de profesor
        @type profesor: int

        @return: Lista de datos que tiene que ver con el profesor en cuestion
        @rtype: [tuple]
        """
        query = "SELECT * FROM curso WHERE profesor={}".format(profesor)
        return self.conexion.enviar_consulta(query)

    def eliminar(self, curso):
        """
        Elimina un curso de la base de datos

        @param curso: id del curso a eliminar
        @type curso: int

        @return: True si se hizo correctamente
        @rtype: boolean
        """
        query = "DELETE FROM curso WHERE id_curso={}".format(curso)
        return (not self.conexion.enviar_registro(query))

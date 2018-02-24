#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

class Inscripcion():
    """
    Clase Inscripcion, enfocada para romper el muchos a muchos de curso - estudiante
    """
    def __init__(self, id_estudiante, id_curso, semestre):
        """
        Constructor de clase Inscripcion

        @param id_estudiante: Codigo unico del estudiante
        @param id_curso: Codigo unico del curso
        @param semestre: Semestre en el que el estudiante se inscribio

        @type id_estudiante: integer
        @type id_curso: integer
        @type semestre: integer
        """
        self.id_estudiante = id_estudiante
        self.id_curso = id_curso
        self.semestre = semestre

    def __str__(self):
        """
        Conversion de clase a str

        @return: Conversion de clase
        @rtype: str
        """
        str_clase = """Codigo de Estudiante: {},
        Codigo de Clase: {},
        Semestre: {},
        Nota: {}
        """.format(self.id_estudiante, self.id_curso, self.semestre, self.nota)
        return str_clase

    def set_nota(self, nota):
        """
        Poner nota al estudiante que esta inscrito en el curso

        @param nota: Nota obtenida del curso

        @type nota: double
        """
        self.nota = nota

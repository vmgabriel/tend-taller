#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Modelo
from model.Persona import Persona
from model.Estudiante import Estudiante
from model.Profesor import Profesor
from model.conector import Conexion

class Persona_service:
    """
    Servicio de eventos para la persona, su estructura va formada como scripting
    """

    def __init__(self):
        """
        Constructor fachada
        """
        self.conexion = Conexion()

    def login(self, usuario, contra):
        """
        Enfocado en iniciar la sesion, aqui se toman las caracteristicas necesarias
        rol :
        - 0 -> logueo erroneo
        - 1 -> estudiante
        - 2 -> profesor

        @param usuario: Nombre de Usuario de ingreso
        @param contra: Contraseña de Usuario para ingreso

        @type usuario: str
        @type contra: str

        @return: Valor de salida de consulta donde se establece la relacion de los datos con su clase, y si fue satisfactorio o no
        @rtype: [rol, tuple]
        """
        query_est = "SELECT * FROM estudiante WHERE usuario = '{}' AND contra = '{}'".format(usuario, contra)
        query_pro = "SELECT * FROM profesor WHERE usuario = '{}' AND contra = '{}'".format(usuario, contra)
        consulta = self.conexion.enviar_consulta(query_est)
        rol = 0
        datos = None
        if (not consulta):
            # revision de si es profesor
            consulta = self.conexion.enviar_consulta(query_pro)
            if (consulta):
                # Es Profesor
                rol = 2
                datos = Profesor(consulta)
        else:
            # Es estudiante
            rol = 1
            datos = Estudiante(consulta)
        salida = []
        salida.append(rol)
        salida.append(datos)
        return salida

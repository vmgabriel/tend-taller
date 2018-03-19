#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Frm_Principal_Estudiante(Gtk.Window):
    """
    Formulario principal de estudiante
    """
    def __init__(self):
        """
        Construtor de la clase Frm_Rol, enfocado a la vista
        """
        self.titulo = "Menu de Estudiante"
        Gtk.Window.__init__(self, title=self.titulo)

    def dev_frm(self):
        """
        Enfocado en la construccion de cada una de las partes del formulario
        este funcionara cargando la caja principal y mostrando algunas propiedades del mismo
        """
        print("CHIIIIIIII")

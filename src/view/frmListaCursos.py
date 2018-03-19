#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Frm_Lista_Curso(Gtk.Window):
    """
    Clase de la lista de los cursos, segun profesor
    """
    def __init__(self, id_profesor):
        """
        Construtor de la clase Frm_Lista_Curso, enfocado a la vista
        """
        self.titulo = "Lista de Cursos"
        Gtk.Window.__init__(self, title=self.titulo)

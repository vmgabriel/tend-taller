#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from view.frmPrincipalProfesor import Frm_Principal_Profesor
from view.frmPrincipalEstudiante import Frm_Principal_Estudiante

class Frm_Rol(Gtk.Window):
    """
    Clase en la que se va a poder seleccionar el rol
    """
    def __init__(self):
        """
        Construtor de la clase Frm_Rol, enfocado a la vista
        """
        self.titulo = "Seleccion de Rol"
        Gtk.Window.__init__(self, title=self.titulo)

    def box1(self):
        """
        Construccion de la caja 1, caja superior que va a albergar un boton

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_estudiante = Gtk.Button(label="Rol de Estudiante")
        self.btn_estudiante.connect("clicked", self.on_btn_estudiante_clicked)
        box_p.pack_end(self.btn_estudiante, True, True, 0)

        return box_p

    def box2(self):
        """
        Construccion de la caja 2, caja inferior que va a albergar un boton

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_profesor = Gtk.Button(label="Rol de Profesor")
        self.btn_profesor.connect("clicked", self.on_btn_profesor_clicked)
        box_p.pack_end(self.btn_profesor, True, True, 0)

        return box_p

    def index_box(self):
        """
        Construccion de la caja Principal, caja principal que se va a mostrar

        @return: Caja con cajas dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        box1 = self.box1()
        box_p.pack_end(box1, True, True, 0)

        box2 = self.box2()
        box_p.pack_end(box2, True, True, 0)

        return box_p

    def dev_frm(self):
        """
        Enfocado en la construccion de cada una de las partes del formulario
        este funcionara cargando la caja principal y mostrando algunas propiedades del mismo
        """
        index = self.index_box()
        self.add(index)

        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size (450, 120)
        self.show_all()
        Gtk.main()

    def on_btn_estudiante_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        frmsig = Frm_Principal_Estudiante()
        frmsig.dev_frm(self)

    def on_btn_profesor_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        frmsig = Frm_Principal_Profesor()
        frmsig.dev_frm(self)

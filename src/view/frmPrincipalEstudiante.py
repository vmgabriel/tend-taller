#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from view.frmListaEstudiante import Frm_Lista_Estudiante
from view.frmListaCursos import Frm_Lista_Curso
from view.frmCrearHorario import Frm_Crear_Horario

class Frm_Principal_Estudiante(Gtk.Window):
    """
    Formulario principal de estudiante
    """
    def __init__(self, sesion):
        """
        Construtor de la clase Frm_Principal_Estudiante, enfocado a la vista
        """
        self.titulo = "Menu de Estudiante"
        self.sesion = sesion
        Gtk.Window.__init__(self, title=self.titulo)

    def box1(self):
        """
        Construccion de la caja 1, caja superior que va a albergar un boton

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_crear_horario = Gtk.Button(label="Crear Horario")
        self.btn_crear_horario.connect("clicked", self.on_btn_crear_horario_clicked)
        box_p.pack_end(self.btn_crear_horario, True, True, 0)

        return box_p

    def box2(self):
        """
        Construccion de la caja 2, caja superior que va a albergar un boton

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_modificar_estudiante = Gtk.Button(label="Modificar Estudiante")
        self.btn_modificar_estudiante.connect("clicked", self.on_btn_modificar_estudiante_clicked)
        box_p.pack_end(self.btn_modificar_estudiante, True, True, 0)

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

    def on_btn_crear_horario_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        frm_estudiante = Frm_Lista_Estudiante("crear_horario")
        frm_estudiante.dev_frm()
        frm_curso = Frm_Lista_Curso("0", "crear_horario")
        frm_curso.dev_frm()
        frm_n_horario = Frm_Crear_Horario(frm_estudiante.get_seleccion(), frm_curso.get_seleccion())

    def on_btn_modificar_estudiante_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

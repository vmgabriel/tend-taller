#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import time
from datetime import date

from view.frmCrearProfesor import Frm_Crear_Profesor

class Frm_Crear_Nombramiento(Gtk.Window):
    """
    Clase en la que se va a poder crear o modificar el Nombramiento del Profesor
    """
    def __init__(self):
        """
        Construtor de la clase Frm_Crear_Nombramiento, enfocado a la vista
        """
        self.titulo = "Crear Nombramiento de Profesor"
        Gtk.Window.__init__(self, title=self.titulo)
        self.modificar = False

    def load(self, profesor):
        """Carga los datos para su posterior modificacion

        @param profesor: Datos referentes al profesor

        @type profesor: Profesor

        """
        self.profesor = profesor
        self.modificar = True

    def box1(self):
        """
        Construccion de la caja 1, caja intermedia que va a dato acerca del Nombramiento del profesor
        nombramiento fecha inicio

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.nombramiento_ini = Gtk.Calendar()
        box_p.pack_end(self.nombramiento_ini, True, True, 1)

        if (self.modificar):
            self.nombramiento_ini.day = self.profesor.inicio_nombramiento.day
            self.nombramiento_ini.month = self.profesor.inicio_nombramiento.month
            self.nombramiento_ini.year = self.profesor.inicio_nombramiento.year

        self.lbl_nombramiento_ini = Gtk.Label("Seleccione Inicio de Nombramiento:")
        box_p.pack_end(self.lbl_nombramiento_ini, False, False, 1)

        return box_p

    def box2(self):
        """
        Construccion de la caja 2, caja intermedia que va a dato acerca del Nombramiento del profesor
        nombramiento fecha fin

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.nombramiento_fin = Gtk.Calendar()
        box_p.pack_end(self.nombramiento_fin, True, True, 1)

        if (self.modificar):
            self.nombramiento_fin.day = self.profesor.fin_nombramiento.day
            self.nombramiento_fin.month = self.profesor.fin_nombramiento.month
            self.nombramiento_fin.year = self.profesor.fin_nombramiento.year

        self.lbl_nombramiento_fin = Gtk.Label("Seleccione Fin de Nombramiento:")
        box_p.pack_end(self.lbl_nombramiento_fin, False, False, 1)

        return box_p

    def box3(self):
        """
        Construccion de la caja 3, caja final, da a los botones

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_guardar = Gtk.Button(label="Guardar")
        self.btn_guardar.connect("clicked", self.on_btn_guardar_clicked)
        box_p.pack_end(self.btn_guardar, True, True, 0)

        self.btn_borrar = Gtk.Button(label="Borrar")
        self.btn_borrar.connect("clicked", self.on_btn_borrar_clicked)
        box_p.pack_end(self.btn_borrar, True, True, 0)

        self.btn_salir = Gtk.Button(label="Salir")
        self.btn_salir.connect("clicked", self.on_btn_salir_clicked)
        box_p.pack_end(self.btn_salir, True, True, 0)

        return box_p

    def index_box(self):
        """
        Construccion de la caja Principal, caja principal que se va a mostrar

        @return: Caja con cajas dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        box3 = self.box3()
        box_p.pack_end(box3, True, True, 0)

        box2 = self.box2()
        box_p.pack_end(box2, True, True, 0)

        box1 = self.box1()
        box_p.pack_end(box1, True, True, 0)

        return box_p

    def dev_frm(self):
        """
        Enfocado en la construccion de cada una de las partes del formulario
        este funcionara cargando la caja principal y mostrando algunas propiedades del mismo
        """
        index = self.index_box()
        self.add(index)

        self.connect("delete-event", self.destroy)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size (400, 400)
        self.show_all()

    def on_btn_guardar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        fi = self.nombramiento_ini.get_date()
        ff = self.nombramiento_fin.get_date()
        if (self.modificar):
            self.profesor.set_ini_nombramiento(fi)
            self.profesor.set_fin_nombramiento(ff)

            frm = Frm_Crear_Profesor()
            frm.load(self.profesor)
            frm.dev_frm()
        else:
            frm = Frm_Crear_Profesor(fi, ff)
            frm.dev_frm()
        self.destroy()

    def on_btn_borrar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        hoy = date.today()
        self.nombramiento_ini.day = hoy.day
        self.nombramiento_ini.month = hoy.month
        self.nombramiento_ini.year = hoy.year
        self.nombramiento_fin.day = hoy.day
        self.nombramiento_fin.month = hoy.month
        self.nombramiento_fin.year = hoy.year

    def on_btn_salir_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.destroy()

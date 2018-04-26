#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencias
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Frm_Crear_Horario(Gtk.Window):
    """
    Clase enfocda en la construccion del horario, tiene permiso desde el formulario principal del estudiante
    """
    def __init__(self, estudiante, curso):
        """
        Constructor de la clase Frm_Crear_Horario, enfocado en la construccion de la creacion del horario,
        antes de cargar este formulario habra que cargar varias cosas, como lo pueden ser la lista de estudiantes y cursos

        @param estudiante: id del estudiante seleccionado previamente
        @type estudiante: int
        @param curso: codigo del curso seleccionado previamente
        @type curso: int
        """
        self.estudiante = estudiante
        self.curso = curso
        self.titulo = "Crear Horario"
        Gtk.Window.__init__(self, title=self.titulo)

    def box1(self):
        """
        Construccion de la caja1, caja superior que va a reunir los datos acerca del horario

        @return Caja con comboBox Adentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        lista_semestres = Gtk.ListStore(str)
        semestres = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                     "11", "12", "13", "14", "15"]
        for semestre in semestres:
            lista_semestres.append([semestre])

        self.cb_semestre = Gtk.ComboBox.new_with_model(lista_semestres)
        self.cb_semestre.connect("changed", self.on_cb_semestre_changed)
        renderer_text = Gtk.CellRendererText()
        self.cb_semestre.pack_start(renderer_text, True)
        self.cb_semestre.add_attribute(renderer_text, "text", 0)
        box_p.pack_end(self.cb_semestre, True, True, 1)

        self.lbl_semestre = Gtk.Label("Seleccione Semestre de Horario:")
        box_p.pack_end(self.lbl_semestre, False, False, 1)

        return box_p

    def box2(self):
        """Construccion de la caja 2, caja intermedia enfocada en la presentacion la construccion del calendario en pantalla
        para su posterior seleccion"""
        box_p = Gtk.Box(spacing=6)

        self.fecha_ini = Gtk.Calendar()
        box_p.pack_end(self.fecha_ini, True, True, 1)

        self.lbl_fecha_ini = Gtk.Label("Seleccione Fecha de Inicio:")
        box_p.pack_end(self.lbl_fecha_ini, False, False, 1)

        return box_p

    def box3(self):
        """Construccion de la caja 3, caja intermedia enfocada en la presentacion la construccion del calendario en pantalla
        para su posterior seleccion"""
        box_p = Gtk.Box(spacing=6)

        self.fecha_fin = Gtk.Calendar()
        box_p.pack_end(self.fecha_fin, True, True, 1)

        self.lbl_fecha_fin = Gtk.Label("Seleccione Fecha de Finalizacion:")
        box_p.pack_end(self.lbl_fecha_fin, False, False, 1)

        return box_p

    def box4(self):
        """
        Construccion de la caja 4, caja final, da a los botones

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
        Enfocado en la construccion de cada una de las partes del formulario
        este funcionara cargando la caja principal y mostrara alguna propiedades del mismo
        """
        box_p = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        box4 = self.box4()
        box_p.pack_end(box4, False, False, 0)

        box3 = self.box3()
        box_p.pack_end(box3, False, False, 0)

        box2 = self.box2()
        box_p.pack_end(box2, False, False, 0)

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
        self.set_default_size (500, 400)
        self.show_all()

    def on_cb_semestre_changed(self, widget):
        """
        Metodo enfocado en ejecutar el evento del combobox para el cambio de semestre

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_guardar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_borrar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_salir_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.destroy()

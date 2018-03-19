#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Frm_Lista_Profesor(Gtk.Window):
    """
    Clase de la lista de los profesores
    """
    def __init__(self, formulario_siguiente=""):
        """
        Construtor de la clase Frm_Lista_Profesor, enfocado a la vista

        @param formulario_siguiente: Formulario que estara cargado despues de la seleccion
        @type formulario_siguiente: str
        """
        self.titulo = "Lista de Profesores"
        Gtk.Window.__init__(self, title=self.titulo)
        self.formulario_siguiente = formulario_siguiente

    def box1(self):
        """
        Construccion de la lista de seleccion para el Profesor
        """
        box_p = Gtk.Box(spacing=6)

        software_liststore = Gtk.ListStore(int, str, str, str)
        treeview = Gtk.TreeView.new_with_model(software_liststore.filter_new())

        scrollable_treelist = Gtk.ScrolledWindow()
        scrollable_treelist.set_vexpand(True)
        box_p.pack_end(scrollable_treelist, True, True, 0)
        scrollable_treelist.add(treeview)

        return box_p

    def box2(self):
        """
        Boton de seleccion para su posterior control
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_facultad_siguiente = Gtk.Button(label="Facultad siguiente")
        self.btn_facultad_siguiente.connect("clicked", self.on_btn_facultad_siguiente_clicked)
        box_p.pack_end(self.btn_facultad_siguiente, True, True, 0)

        self.btn_facultad_anterior = Gtk.Button(label="Facultad Anterior")
        self.btn_facultad_anterior.connect("clicked", self.on_btn_facultad_anterior_clicked)
        box_p.pack_end(self.btn_facultad_anterior, True, True, 0)

        return box_p

    def box3(self):
        """
        Boton de seleccion
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_seleccionar = Gtk.Button(label="Seleccionar")
        self.btn_seleccionar.connect("clicked", self.on_btn_seleccionar_clicked)
        box_p.pack_end(self.btn_seleccionar, True, True, 0)

        return box_p

    def index_box(self):
        """
        Construccion de la caja Principal, caja principal que se va a mostrar

        @return: Caja con cajas dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

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

    def on_btn_facultad_siguiente_clicked(self):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_facultad_anterior_clicked(self):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_seleccionar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (self.formulario_siguiente == "lista_curso"):
            print("seleccionado {}".format(self.formulario_siguiente))
        elif (self.formulario_siguiente == "crear_estudiante"):
            print("seleccionado {}".format(self.formulario_siguiente))
        elif (self.formulario_siguiente == ""):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
                Gtk.ButtonsType.YES_NO, "Eliminar Profesor")
            dialog.format_secondary_text(
                "Desea eliminar el profesor?, de ser asi no volvera a recuperar sus datos")
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                print("eliminando")

            dialog.destroy()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Frm_Lista_Estudiante(Gtk.Window):
    """
    Clase de la lista de los estudiantes
    """
    def __init__(self, formulario_siguiente):
        """
        Construtor de la clase Frm_Lista_Estudiante, enfocado a la vista

        @param formulario_siguiente: Formulario que estara cargado despues de la seleccion
        @type formulario_siguiente: str
        """
        self.formulario_siguiente = formulario_siguiente
        self.titulo = "Lista de Estudiantes"
        Gtk.Window.__init__(self, title=self.titulo)
        self.id_estudiante = 0

    def box1(self):
        """
        Construccion de la lista de seleccion para el Estudiante

        @return: Caja con datos referentes a la lista de estudiantes
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        software_liststore = Gtk.ListStore(int, str, str, str, str, int)
        treeview = Gtk.TreeView.new_with_model(software_liststore.filter_new())

        scrollable_treelist = Gtk.ScrolledWindow()
        scrollable_treelist.set_vexpand(True)
        box_p.pack_end(scrollable_treelist, True, True, 0)
        scrollable_treelist.add(treeview)

        return box_p

    def box2(self):
        """
        Boton de seleccion para su posterior control

        @return: Caja con cajas dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_semestre_siguiente = Gtk.Button(label="Semestre siguiente")
        self.btn_semestre_siguiente.connect("clicked", self.on_btn_semestre_siguiente_clicked)
        box_p.pack_end(self.btn_semestre_siguiente, True, True, 0)

        self.btn_semestre_anterior = Gtk.Button(label="Semestre Anterior")
        self.btn_semestre_anterior.connect("clicked", self.on_btn_semestre_anterior_clicked)
        box_p.pack_end(self.btn_semestre_anterior, True, True, 0)

        return box_p

    def box3(self):
        """
        Boton de seleccion
        """
        box_p = Gtk.Box(spacing=6)

        if (self.formulario_siguiente == "crear_horario"):
            self.btn_borrar = Gtk.Button(label="Seleccionar")
        else:
            self.btn_borrar = Gtk.Button(label="Borrar")
        self.btn_borrar.connect("clicked", self.on_btn_borrar_clicked)
        box_p.pack_end(self.btn_borrar, True, True, 0)

        self.btn_cerrar = Gtk.Button(label="Cerrar")
        self.btn_cerrar.connect("clicked", self.destroy)
        box_p.pack_end(self.btn_cerrar, True, True, 0)

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

    def on_btn_semestre_siguiente_clicked(self):
        """
        Evento que funciona al accionar el boton de Estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_semestre_anterior_clicked(self):
        """
        Evento que funciona al accionar el boton de Estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_borrar_clicked(self):
        """
        Evento que funciona al accionar el boton de Estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (self.formulario_siguinte == "crear_horario"):
            self.id_estudiante = 1
            self.destroy()
        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
                                       Gtk.ButtonsType.YES_NO, "Eliminar Estudiante")
            dialog.format_secondary_text(
                "Está seguro que desea eliminar estudiante, los datos no se recuperarán?")
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                print("eliminado")
            elif response == Gtk.ResponseType.NO:
                print("menos mal")

                dialog.destroy()

    def get_seleccion(self):
        """
        Retorna el valor de la seleccion de la lista aqui mostrada y con ello tomar decisiones

        @return: Valor de id_estudiante que se seleccionó al oprimir
        @rtype: int
        """
        return self.id_estudiante

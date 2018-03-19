#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Frm_Crear_Curso(Gtk.Window):
    """
    Clase en la que se va a poder crear o modificar curso
    """
    def __init__(self):
        """
        Construtor de la clase Frm_Crear_Curso, enfocado a la vista
        """
        self.titulo = "Crear Curso"
        Gtk.Window.__init__(self, title=self.titulo)

    def box1(self):
        """
        Construccion de la caja 1, caja superior que va a dato acerca del curso

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_nombre = Gtk.Entry()
        box_p.pack_end(self.txt_nombre, True, True, 1)

        self.lbl_nombre = Gtk.Label("Ingrese nombre:")
        box_p.pack_end(self.lbl_nombre, False, False, 1)

        return box_p

    def box2(self):
        """
        Construccion de la caja 2, caja intermedia que va a dato acerca del curso

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_aula = Gtk.Entry()
        box_p.pack_end(self.txt_aula, True, True, 1)

        self.lbl_aula = Gtk.Label("Ingrese aula:")
        box_p.pack_end(self.lbl_aula, False, False, 1)

        return box_p

    def box3(self):
        """
        Construccion de la caja 3, caja intermedia que va a dato acerca del curso

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_tiempo = Gtk.Entry()
        box_p.pack_end(self.txt_tiempo, True, True, 1)

        self.lbl_tiempo = Gtk.Label("Ingrese tiempo dado:")
        box_p.pack_end(self.lbl_tiempo, False, False, 1)

        return box_p

    def box4(self):
        """
        Construccion de la caja 3, caja intermedia que va a dato acerca del curso

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.calendar = Gtk.Calendar()
        box_p.pack_end(self.calendar, True, True, 1)

        self.lbl_dia = Gtk.Label("Seleccione Dia de Reunion:")
        box_p.pack_end(self.lbl_dia, False, False, 1)

        return box_p

    def box5(self):
        """
        Construccion de la caja 3, caja intermedia que va a dato acerca del curso

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        country_store = Gtk.ListStore(str)
        countries = ["Austria", "Brazil", "Belgium", "France", "Germany",
            "Switzerland", "United Kingdom", "United States of America",
            "Uruguay"]
        for country in countries:
            country_store.append([country])

        self.cb_edificio = Gtk.ComboBox.new_with_model(country_store)
        self.cb_edificio.connect("changed", self.on_cb_edificio_changed)
        renderer_text = Gtk.CellRendererText()
        self.cb_edificio.pack_start(renderer_text, True)
        self.cb_edificio.add_attribute(renderer_text, "text", 0)
        box_p.pack_end(self.cb_edificio, True, True, 1)

        self.lbl_edificio = Gtk.Label("Seleccione Edificio:")
        box_p.pack_end(self.lbl_edificio, False, False, 1)

        return box_p

    def box6(self):
        """
        Construccion de la caja 6, caja final, da a los botones

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

        box6 = self.box6()
        box_p.pack_end(box6, True, True, 0)

        box5 = self.box5()
        box_p.pack_end(box5, True, True, 0)

        box4 = self.box4()
        box_p.pack_end(box4, True, True, 0)

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
        self.set_default_size (600, 600)
        self.show_all()


    def on_cb_edificio_changed(self, widget):
        """
        Evento para combobox cuando este cambia

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

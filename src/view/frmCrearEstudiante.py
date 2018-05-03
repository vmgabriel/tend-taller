#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Model
from model.Estudiante import Estudiante

class Frm_Crear_Estudiante(Gtk.Window):
    """
    Clase en la que se va a poder crear o modificar estudiante
    """
    def __init__(self, profesor=None):
        """
        Construtor de la clase Frm_Crear_Estudiante, enfocado a la vista
        """
        self.profesor = profesor
        self.titulo = "Crear Estudiante"
        Gtk.Window.__init__(self, title=self.titulo)

    def box1(self):
        """
        Construccion de la caja 1, caja superior que va a dato acerca del estudiante
        enfocado en el codigo del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_cod = Gtk.Entry()
        box_p.pack_end(self.txt_cod, True, True, 1)

        self.lbl_cod = Gtk.Label("Ingrese Codigo:")
        box_p.pack_end(self.lbl_cod, False, False, 1)

        return box_p

    def box2(self):
        """
        Construccion de la caja 2, caja intermedia que va a dato acerca del estudiante
        enfocado en el nombre 1 del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_nombre1 = Gtk.Entry()
        box_p.pack_end(self.txt_nombre1, True, True, 1)

        self.lbl_nombre1 = Gtk.Label("Ingrese Nombre1:")
        box_p.pack_end(self.lbl_nombre1, False, False, 1)

        return box_p

    def box3(self):
        """
        Construccion de la caja 3, caja intermedia que va a dato acerca del estudiante
        enfocado en el nombre 2 del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_nombre2 = Gtk.Entry()
        box_p.pack_end(self.txt_nombre2, True, True, 1)

        self.lbl_nombre2 = Gtk.Label("Ingrese Nombre2:")
        box_p.pack_end(self.lbl_nombre2, False, False, 1)

        return box_p

    def box4(self):
        """
        Construccion de la caja 4, caja intermedia que va a dato acerca del estudiante
        enfocado en el Apellido 1 del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_apellido1 = Gtk.Entry()
        box_p.pack_end(self.txt_apellido1, True, True, 1)

        self.lbl_apellido1 = Gtk.Label("Ingrese Apellido1:")
        box_p.pack_end(self.lbl_apellido1, False, False, 1)

        return box_p

    def box5(self):
        """
        Construccion de la caja 5, caja intermedia que va a dato acerca del estudiante
        enfocado en el Apellido 2 del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_apellido2 = Gtk.Entry()
        box_p.pack_end(self.txt_apellido2, True, True, 1)

        self.lbl_apellido2 = Gtk.Label("Ingrese Apellido2:")
        box_p.pack_end(self.lbl_apellido2, False, False, 1)

        return box_p

    def box6(self):
        """
        Construccion de la caja 6, caja intermedia que va a dato acerca del estudiante
        enfocado en la edad del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_edad = Gtk.Entry()
        box_p.pack_end(self.txt_edad, True, True, 1)

        self.lbl_edad = Gtk.Label("Ingrese Edad:")
        box_p.pack_end(self.lbl_edad, False, False, 1)

        return box_p

    def box7(self):
        """
        Construccion de la caja 7, caja intermedia que va a dato acerca del estudiante
        enfocado en el lugar de nacimiento del estudiante

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

        self.cb_lug_nacimiento = Gtk.ComboBox.new_with_model(country_store)
        self.cb_lug_nacimiento.connect("changed", self.on_cb_lug_nacimiento_changed)
        renderer_text = Gtk.CellRendererText()
        self.cb_lug_nacimiento.pack_start(renderer_text, True)
        self.cb_lug_nacimiento.add_attribute(renderer_text, "text", 0)
        box_p.pack_end(self.cb_lug_nacimiento, True, True, 1)

        self.lbl_lug_nacimiento = Gtk.Label("Seleccione Lugar de Nacimiento:")
        box_p.pack_end(self.lbl_lug_nacimiento, False, False, 1)

        return box_p

    def box8(self):
        """
        Construccion de la caja 8, caja intermedia que va a dato acerca del estudiante
        enfocado en el lugar de residencia del estudiante

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

        self.cb_lug_residencia = Gtk.ComboBox.new_with_model(country_store)
        self.cb_lug_residencia.connect("changed", self.on_cb_lug_residencia_changed)
        renderer_text = Gtk.CellRendererText()
        self.cb_lug_residencia.pack_start(renderer_text, True)
        self.cb_lug_residencia.add_attribute(renderer_text, "text", 0)
        box_p.pack_end(self.cb_lug_residencia, True, True, 1)

        self.lbl_lug_residencia = Gtk.Label("Seleccione Lugar de Residencia:")
        box_p.pack_end(self.lbl_lug_residencia, False, False, 1)

        return box_p

    def box9(self):
        """
        Construccion de la caja 9, caja intermedia que va a dato acerca del estudiante
        enfocado en la direccion de residencia del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_residencia = Gtk.Entry()
        box_p.pack_end(self.txt_residencia, True, True, 1)

        self.lbl_residencia = Gtk.Label("Ingrese Direccion de Residencia:")
        box_p.pack_end(self.lbl_residencia, False, False, 1)

        return box_p

    def box10(self):
        """
        Construccion de la caja 10, caja intermedia que va a dato acerca del estudiante
        enfocado en la semestre del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_semestre = Gtk.Entry()
        box_p.pack_end(self.txt_semestre, True, True, 1)

        self.lbl_semestre = Gtk.Label("Ingrese Semestre:")
        box_p.pack_end(self.lbl_semestre, False, False, 1)

        return box_p

    def box11(self):
        """
        Construccion de la caja 11, caja intermedia que va a dato acerca del estudiante
        enfocado en el usuario del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_usuario = Gtk.Entry()
        box_p.pack_end(self.txt_usuario, True, True, 1)

        self.lbl_usuario = Gtk.Label("Ingrese Usuario:")
        box_p.pack_end(self.lbl_usuario, False, False, 1)

        return box_p

    def box12(self):
        """
        Construccion de la caja 12, caja intermedia que va a dato acerca del estudiante
        enfocado en la contraseña del estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_contra = Gtk.Entry()
        box_p.pack_end(self.txt_contra, True, True, 1)

        self.lbl_contra = Gtk.Label("Ingrese Contraseña:")
        box_p.pack_end(self.lbl_contra, False, False, 1)

        return box_p

    def box13(self):
        """
        Construccion de la caja 13, caja final, da a los botones

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

        box13 = self.box13()
        box_p.pack_end(box13, True, True, 0)

        box12 = self.box12()
        box_p.pack_end(box12, True, True, 0)

        box11 = self.box11()
        box_p.pack_end(box11, True, True, 0)

        box10 = self.box10()
        box_p.pack_end(box10, True, True, 0)

        box9 = self.box9()
        box_p.pack_end(box9, True, True, 0)

        box8 = self.box8()
        box_p.pack_end(box8, True, True, 0)

        box7 = self.box7()
        box_p.pack_end(box7, True, True, 0)

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
        self.set_default_size (600, 700)
        self.show_all()


    def on_cb_lug_nacimiento_changed(self, widget):
        """
        Evento para combobox cuando este cambia

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_cb_lug_residencia_changed(self, widget):
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
        if (self.txt_cod.get_text() == "" or self.txt_nombre1.get_text() == "" or self.txt_apellido1.get_text() == ""
            or self.txt_edad.get_text() == "" or self.txt_residencia.get_text() == "" or self.txt_semestre.get_text() == ""
            or self.txt_usuario.get_text() == "" or self.txt_contra.get_text() == ""):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CANCEL, "Datos no Introducidos")
            dialog.format_secondary_text(
                "Uno o mas datos no han sido introducidos")
            dialog.run()
            dialog.destroy()
        else:
            ide = int(self.txt_cod.get_text())
            edad = int(self.txt_edad.get_text())
            #TODO: implementar la obtencion del codigo
            nuevo_estudiante = Estudiante(ide, self.txt_nombre1.get_text(), self.txt_nombre1.get_text(), self.txt_nombre2.get_text(), self.txt_apellido1.get_text(), self.txt_apellido2.get_text(), edad,)

    def on_btn_borrar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.txt_cod.set_text("")
        self.txt_nombre1.set_text("")
        self.txt_nombre2.set_text("")
        self.txt_apellido1.set_text("")
        self.txt_apellido2.set_text("")
        self.txt_edad.set_text("")
        self.txt_residencia.set_text("")
        self.txt_semestre.set_text("")
        self.txt_usuario.set_text("")
        self.txt_contra.set_text("")
        self.txt_cod.grab_focus_without_selecting()

    def on_btn_salir_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.destroy()

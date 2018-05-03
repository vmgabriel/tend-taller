#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Vista
from view.frmPrincipalProfesor import Frm_Principal_Profesor
from view.frmPrincipalEstudiante import Frm_Principal_Estudiante

# Controlador -> servicios
from controller.Persona import Persona_service

class Frm_Rol(Gtk.Window):
    """
    Clase en la que se va a poder seleccionar el rol
    """
    def __init__(self):
        """
        Construtor de la clase Frm_Rol, enfocado a la vista
        """
        self.titulo = "Login"
        Gtk.Window.__init__(self, title=self.titulo)

    def box1(self):
        """
        Construccion de la caja 1, caja usuario

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_usuario = Gtk.Entry()

        self.lbl_usuario = Gtk.Label("Ingrese usuario:")

        box_p.pack_end(self.txt_usuario, True, True, 0)
        box_p.pack_end(self.lbl_usuario, True, True, 0)

        return box_p

    def box2(self):
        """
        Construccion de la caja 2, caja de pass

        @return: Caja con entrada dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.txt_contra = Gtk.Entry()
        self.txt_contra.set_visibility(False)

        self.lbl_contra = Gtk.Label("Ingrese Contraseña:")

        box_p.pack_end(self.txt_contra, True, True, 0)
        box_p.pack_end(self.lbl_contra, True, True, 0)

        return box_p

    def box3(self):
        """
        Construccion de la caja 3, caja inferior que va a albergar los botones

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_guardar = Gtk.Button(label="Iniciar Sesion")
        self.btn_guardar.connect("clicked", self.on_btn_guardar_clicked)
        box_p.pack_end(self.btn_guardar, True, True, 0)

        self.btn_borrar = Gtk.Button(label="Borrar")
        self.btn_borrar.connect("clicked", self.on_btn_borrar_clicked)
        box_p.pack_end(self.btn_borrar, True, True, 0)

        return box_p

    def index_box(self):
        """
        Construccion de la caja Principal, caja principal que se va a mostrar

        @return: Caja con cajas dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        box3 = self.box3()

        box2 = self.box2()

        box1 = self.box1()

        box_p.pack_end(box3, True, True, 0)
        box_p.pack_end(box2, True, True, 0)
        box_p.pack_end(box1, True, True, 0)

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

    def on_btn_guardar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        service = Persona_service()
        usuario = service.login(self.txt_usuario.get_text(), self.txt_contra.get_text())
        frm = None
        if (usuario[0] == 0):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CANCEL, "Error de Autenticacion")
            dialog.format_secondary_text(
                "Error de inicio de sesion!!, Usuario o Contraseña no son correctos")
            dialog.run()
            dialog.destroy()
        elif (usuario[0] == 1):
            frm = Frm_Principal_Estudiante(usuario[1])
        else:
            frm = Frm_Principal_Profesor(usuario[1])
        if (frm):
            frm.dev_frm()
            self.destroy()


    def on_btn_borrar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.txt_contra.set_text("")
        self.txt_usuario.set_text("")
        self.txt_usuario.grab_focus_without_selecting()

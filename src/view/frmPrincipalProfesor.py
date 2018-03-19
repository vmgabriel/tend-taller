#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from view.frmListaCursos import Frm_Lista_Curso
from view.frmListaProfesor import Frm_Lista_Profesor
from view.frmCrearCurso import Frm_Crear_Curso
from view.frmCrearEstudiante import Frm_Crear_Estudiante

class Frm_Principal_Profesor(Gtk.Window):
    """
    Formulario principal del profesor
    """
    def __init__(self):
        """
        Construtor de la clase Frm_Principal_Profesor, enfocado a la vista
        """
        self.titulo = "Menu de Profesor"
        Gtk.Window.__init__(self, title=self.titulo)

    def box1(self):
        """
        Construccion de la caja 1, caja superior que va a albergar un boton

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_crear_curso = Gtk.Button(label="Crear Curso")
        self.btn_crear_curso.connect("clicked", self.on_btn_crear_curso_clicked)
        box_p.pack_end(self.btn_crear_curso, True, True, 1)

        self.btn_lista_curso = Gtk.Button(label="Lista de Cursos")
        self.btn_lista_curso.connect("clicked", self.on_btn_lista_curso_clicked)
        box_p.pack_end(self.btn_lista_curso, True, True, 0)

        return box_p

    def box2(self):
        """
        Construccion de la caja 2, caja media 1 que va a albergar dos botones referentes a estudiante

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_borrar_curso = Gtk.Button(label="Borrar Estudiante")
        self.btn_borrar_curso.connect("clicked", self.on_btn_borrar_estudiante_clicked)
        box_p.pack_end(self.btn_borrar_curso, True, True, 1)

        self.btn_crear_estudiante = Gtk.Button(label="Crear Estudiante")
        self.btn_crear_estudiante.connect("clicked", self.on_btn_crear_estudiante_clicked)
        box_p.pack_end(self.btn_crear_estudiante, True, True, 0)

        return box_p

    def box3(self):
        """
        Construccion de la caja 3, caja media 2 que va a albergar dos botones referentes a profesor

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_borrar_profesor = Gtk.Button(label="Borrar Estudiante")
        self.btn_borrar_profesor.connect("clicked", self.on_btn_borrar_profesor_clicked)
        box_p.pack_end(self.btn_borrar_profesor, True, True, 1)

        self.btn_crear_profesor = Gtk.Button(label="Crear Profesor")
        self.btn_crear_profesor.connect("clicked", self.on_btn_crear_profesor_clicked)
        box_p.pack_end(self.btn_crear_profesor, True, True, 0)

        return box_p

    def box4(self):
        """
        Construccion de la caja 4, caja media 3 que va a albergar un boton sobre el profesor

        @return: Caja con boton dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.btn_modificar_profesor = Gtk.Button(label="Modificar Profesor")
        self.btn_modificar_profesor.connect("clicked", self.on_btn_modificar_profesor_clicked)
        box_p.pack_end(self.btn_modificar_profesor, True, True, 0)

        return box_p

    def index_box(self):
        """
        Construccion de la caja Principal, caja principal que se va a mostrar

        @return: Caja con cajas dentro
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        box4 = self.box4()
        box_p.pack_end(box4, True, True, 0)

        box3 = self.box3()
        box_p.pack_end(box3, True, True, 1)

        box2 = self.box2()
        box_p.pack_end(box2, True, True, 2)

        box1 = self.box1()
        box_p.pack_end(box1, True, True, 3)

        return box_p

    def dev_frm(self, frm):
        """
        Enfocado en la construccion de cada una de las partes del formulario
        este funcionara cargando la caja principal y mostrando algunas propiedades del mismo

        @param frm: formulario anterior para su posterior cierre
        @type frm: Gtk.Windows
        """
        index = self.index_box()
        self.add(index)

        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size (600, 600)
        self.show_all()
        frm.destroy()

    def on_btn_lista_curso_clicked(self, widget):
        """
        Evento para btn de lista de cursos

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        frmprof = Frm_Lista_Profesor("lista_curso")
        frmprof.dev_frm()

    def on_btn_crear_curso_clicked(self, widget):
        """
        Evento para btn de crear curso

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        frmcur = Frm_Crear_Curso()
        frmcur.dev_frm()

    def on_btn_crear_estudiante_clicked(self, widget):
        """
        Evento para btn de crear estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
            Gtk.ButtonsType.YES_NO, "Estudiante Graduado")
        dialog.format_secondary_text(
            "Está el estudiante Graduado?")
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            frmprof = Frm_Lista_Profesor("crear_estudiante")
            frmprof.dev_frm()
        elif response == Gtk.ResponseType.NO:
            frmcur = Frm_Crear_Estudiante()
            frmcur.dev_frm()

        dialog.destroy()

    def on_btn_borrar_estudiante_clicked(elf, widget):
        """
        Evento para btn de borrar estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        print("4")

    def on_btn_crear_profesor_clicked(elf, widget):
        """
        Evento para btn de crear profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        print("5")

    def on_btn_borrar_profesor_clicked(elf, widget):
        """
        Evento para btn de borrar profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        print("6")

    def on_btn_modificar_profesor_clicked(elf, widget):
        """
        Evento para btn de modificar profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        print("7")

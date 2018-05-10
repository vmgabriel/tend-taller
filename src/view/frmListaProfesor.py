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

# Model
from model.Profesor import Profesor
from model.Ciudad import Ciudad

# Controller
from controller.Profesor import Profesor_service

#view
from view.frmCrearNombramiento import Frm_Crear_Nombramiento
from view.frmCrearEstudiante import Frm_Crear_Estudiante
from view.frmCrearCurso import Frm_Crear_Curso

class Frm_Lista_Profesor(Gtk.Window):
    """
    Clase de la lista de los profesores
    """
    def __init__(self, formulario_siguiente="", datos_profesor=None):
        """
        Construtor de la clase Frm_Lista_Profesor, enfocado a la vista

        @param formulario_siguiente: Formulario que estara cargado despues de la seleccion
        @type formulario_siguiente: str
        """
        self.titulo = "Lista de Profesores"
        Gtk.Window.__init__(self, title=self.titulo)
        self.formulario_siguiente = formulario_siguiente
        self.datos_profesor = datos_profesor
        self.modelo_mostrar = ["id", "Nombre", "Apellido 1", "Apellido 2", "Facultad"]

    def box1(self):
        """
        Construccion de la lista de seleccion para el Profesor
        """
        box_p = Gtk.Box(spacing=6)

        self.software_liststore = Gtk.ListStore(int, str, str, str, int)

        self.cargar_datos()
        self.matriz_to_liststore(self.filtro_parametros(self.datos))

        self.language_filter = self.software_liststore.filter_new()
        self.language_filter.set_visible_func(self.seleccionar_facultad)

        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)

        for i, column_title in enumerate(self.modelo_mostrar):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        box_p.pack_end(self.treeview, True, True, 0)

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

        if (self.formulario_siguiente == "crear_horario"):
            self.btn_modificar = Gtk.Button(label="Modificar")
        else:
            self.btn_seleccionar = Gtk.Button(label="Seleccionar")
        self.btn_seleccionar.connect("clicked", self.on_btn_seleccionar_clicked)
        box_p.pack_end(self.btn_seleccionar, True, True, 0)

        self.btn_borrar = Gtk.Button(label="Borrar")
        self.btn_borrar.connect("clicked", self.on_btn_borrar_clicked)
        box_p.pack_end(self.btn_borrar, True, True, 0)

        self.btn_cerrar = Gtk.Button(label="Cerrar")
        self.btn_cerrar.connect("clicked", self.on_btn_cerrar_clicked)
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

        self.connect("delete-event", self.on_btn_cerrar_clicked)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size (500, 400)
        self.show_all()

    def matriz_to_liststore(self, matriz):
        """
        Convierte una matriz comun y corriente en una listStore

        @param matriz: Matriz que se va a convertir en listStore
        @type matriz: <class= 'list'>

        @return: listStore correspondiente de la matriz
        @rtype: Gtk.listStore
        """
        for vector in matriz:
            self.software_liststore.append(list(vector))

    def filtro_parametro(self, vector):
        """
        Fitrla los parametros del vector deseado para ser puesto

        @param vector: Vector que se va a reducir
        @type vector: tuple

        @return: Vector reducido
        @rtype: tuple
        """
        return (vector[0],vector[1], vector[3], vector[4], vector[14])

    def filtro_parametros(self, matriz):
        """
        Filtra los parametros necesarios, no mas no menos

        @param matriz: Matriz que se va a reducir
        @type matriz: <class= 'list'>

        @return: Matriz reducida con los parametros necesarios
        @rtype: <class= 'list'>
        """
        return list(map(self.filtro_parametro, matriz))

    def seleccionar_facultad(self, model, ite, data):
        """
        Relacion con el metodo de filtro para el treeview

        @param model: Modelo
        @param ite: iterador
        @param data: datos relacionados
        """
        if (self.facultad_actual == 0):
            return True
        else:
            return model[ite][4] == self.facultad_actual

    def cargar_datos(self):
        """
        Evento de ejecucion para cargar datos de la base de datos
        """
        service = Profesor_service()
        self.facultad_actual = 0
        self.lista_facultades = service.ver_todas_facultades()
        self.datos = service.ver_todos()

    def on_btn_facultad_siguiente_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.facultad_actual += 1
        if (self.facultad_actual > len(self.lista_facultades)):
            self.facultad_actual = 0

        self.language_filter.refilter()

    def on_btn_facultad_anterior_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.facultad_actual -= 1
        if (self.facultad_actual < 0):
            self.facultad_actual = len(self.lista_facultades)

        self.language_filter.refilter()

    def on_btn_seleccionar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de profesor

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (self.formulario_siguiente == "crear_estudiante"):
            # Estudiante Graduado
            select = self.treeview.get_selection()

            (model, ite) = select.get_selected()
            id_seleccionado = model.get_value(ite, 0)

            frm_siguiente = Frm_Crear_Estudiante(id_seleccionado)
            frm_siguiente.dev_frm()
            self.destroy()
        elif (self.formulario_siguiente == "modificar_profesor"):
            # seleccionar y consultar los datos para su posteorior seleccion
            prof = Profesor(123, "Pedro", "Andres", "Paramo", "Diaz", 23, Ciudad("", ""), Ciudad("", ""), "calle", "Doctor", "contratista", True, date(2010,10,10), date(2012,12,12))
            if (prof.is_visitante):
                frm = Frm_Crear_Nombramiento()
                frm.load(prof)
                frm.dev_frm()
            else:
                frm = Frm_Crear_Profesor()
                frm.load(prof)
                frm.dev_frm()
        elif (self.formulario_siguiente == "crear_curso"):
            select = self.treeview.get_selection()

            (model, ite) = select.get_selected()
            id_seleccionado = model.get_value(ite, 0)

            frm_siguiente = Frm_Crear_Curso(id_seleccionado)
            frm_siguiente.dev_frm()
            self.destroy()
        elif (self.formulario_siguiente == "modificar_curso"):
            self.fs_modificar_profesor()
        elif (self.formulario_siguiente == ""):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
                Gtk.ButtonsType.YES_NO, "Eliminar Profesor")
            dialog.format_secondary_text(
                "Desea eliminar el profesor?, de ser asi no volvera a recuperar sus datos")
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                print("eliminando")

        dialog.destroy()

    def fs_modificar_profesor(self):
        """
        Evento de caracterizacion y limpieza de codigo
        """
        select = self.treeview.get_selection()

        (model, ite) = select.get_selected()

        lista_curso = list(self.datos_profesor)

        lista_curso[6] = model.get_value(ite, 0)

        frm = Frm_Crear_Curso(0,lista_curso)
        frm.dev_frm()
        self.destroy()

    def on_btn_borrar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de curso

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
                                   Gtk.ButtonsType.YES_NO, "Eliminar Profesor")
        dialog.format_secondary_text(
            "Está seguro que desea eliminar Profesor, los datos no se recuperarán?")
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.YES:
            select = self.treeview.get_selection()

            (model, ite) = select.get_selected()
            id_seleccionado = model.get_value(ite, 0);

            service = Profesor_service()
            if (service.eliminar(id_seleccionado)):
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                           Gtk.ButtonsType.OK, "Eliminado Correctamente")
                dialog.format_secondary_text("Eliminado Correctamente")
                dialog.run()
                dialog.destroy()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                           Gtk.ButtonsType.OK, "Error al eliminar")
                dialog.format_secondary_text("Error en la base de datos al eliminar")
                dialog.run()
                dialog.destroy()
            self.destroy()

    def on_btn_cerrar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de cerrar

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.destroy()

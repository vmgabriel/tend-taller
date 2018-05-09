#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Controlador
from controller.Curso import Curso_service

class Frm_Lista_Curso(Gtk.Window):
    """
    Clase de la lista de los cursos
    """
    def __init__(self, cod_profesor=0, formulario_siguiente="lista_curso"):
        """
        Construtor de la clase Frm_Lista_Curso, enfocado a la vista

        @param formulario_siguiente: Formulario que estara cargado despues de la seleccion
        @type formulario_siguiente: str
        """
        self.titulo = "Lista de Cursos"
        Gtk.Window.__init__(self, title=self.titulo)
        self.formulario_siguiente = formulario_siguiente
        self.cod_profesor = cod_profesor
        self.id_curso = 0
        self.modelo_mostrar = ["Nombre", "Aula", "Edificio", "Profesor", "Fecha_reunion"]

    def box1(self):
        """
        Construccion de la lista de seleccion para el curso
        """
        box_p = Gtk.Box(spacing=6)

        self.software_liststore = Gtk.ListStore(str, str, int, int, str)

        self.cargar_datos()
        self.matriz_to_liststore(self.filtro_parametros(self.lista_cursos))

        self.language_filter = self.software_liststore.filter_new()

        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)

        for i, column_title in enumerate(self.modelo_mostrar):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        box_p.pack_end(self.treeview, True, True, 0)

        return box_p

    def box2(self):
        """
        Boton de seleccion
        """
        box_p = Gtk.Box(spacing=6)

        if (self.formulario_siguiente == "crear_horario"):
            self.btn_modificar = Gtk.Button(label="Seleccionar")
        else:
            self.btn_modificar = Gtk.Button(label="Modificar")
        self.btn_modificar.connect("clicked", self.on_btn_modificar_clicked)
        box_p.pack_end(self.btn_modificar, True, True, 0)

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

    def cargar_datos(self):
        """
        Construccion de los datos dentro de la pantalla
        """
        service = Curso_service()
        self.lista_cursos = service.ver_todos()

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
        fecha = str(vector[4].day) + "/" + str(vector[4].month) + "/" + str(vector[4].year)
        return (vector[1],vector[2], vector[5], vector[6], fecha)

    def filtro_parametros(self, matriz):
        """
        Filtra los parametros necesarios, no mas no menos

        @param matriz: Matriz que se va a reducir
        @type matriz: <class= 'list'>

        @return: Matriz reducida con los parametros necesarios
        @rtype: <class= 'list'>
        """
        return list(map(self.filtro_parametro, matriz))

    def on_btn_modificar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de curso

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (self.formulario_siguiente == "crear_horario"):
            self.id_curso = 1
            self.destroy()
        else:
            print("modificar")

    def on_btn_borrar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de curso

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        pass

    def on_btn_cerrar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de cerrar

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.destroy()

    def get_seleccion(self):
        """
        Retorna el valor de la seleccion del formulario despues de aceptar

        @return: Valor seleccionado en la lista, especificamente el id
        @rtype: int
        """
        return self.id_curso

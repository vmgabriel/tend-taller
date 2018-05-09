#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Controller
from controller.Estudiante import Estudiante_service

class Frm_Lista_Estudiante(Gtk.Window):
    """
    Clase de la lista de los estudiantes
    """
    def __init__(self, formulario_siguiente=""):
        """
        Construtor de la clase Frm_Lista_Estudiante, enfocado a la vista

        @param formulario_siguiente: Formulario que estara cargado despues de la seleccion
        @type formulario_siguiente: str
        """
        self.formulario_siguiente = formulario_siguiente
        self.titulo = "Lista de Estudiantes"
        Gtk.Window.__init__(self, title=self.titulo)
        self.id_estudiante = 0
        self.modelo_mostrar = ["id", "Nombre 1", "Nombre 2", "Apellido 1", "Apellido 2", "Semestre"]

    def box1(self):
        """
        Construccion de la lista de seleccion para el Estudiante

        @return: Caja con datos referentes a la lista de estudiantes
        @rtype: Gtk.Box
        """
        box_p = Gtk.Box(spacing=6)

        self.software_liststore = Gtk.ListStore(int, str, str, str, str, int)
        self.cargar_datos()
        self.matriz_to_liststore(self.filtro_parametros(self.estudiantes))

        self.language_filter = self.software_liststore.filter_new()
        self.language_filter.set_visible_func(self.seleccionar_semestre)

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

        if (self.formulario_siguiente == ""):
            self.btn_seleccionar = Gtk.Button(label="Modificar")
        else:
            self.btn_seleccionar = Gtk.Button(label="Seleccionar")
        self.btn_seleccionar.connect("clicked", self.on_btn_seleccionar_clicked)
        box_p.pack_end(self.btn_seleccionar, True, True, 0)

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

    def cargar_datos(self):
        """
        Cargara los datos de la base de datos para su posterior muestreo
        """
        self.semestre_actual = 0
        service = Estudiante_service()
        self.estudiantes = service.ver_todos()

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
        return (vector[0],vector[1], vector[2], vector[3], vector[4], vector[9])

    def filtro_parametros(self, matriz):
        """
        Filtra los parametros necesarios, no mas no menos

        @param matriz: Matriz que se va a reducir
        @type matriz: <class= 'list'>

        @return: Matriz reducida con los parametros necesarios
        @rtype: <class= 'list'>
        """
        return list(map(self.filtro_parametro, matriz))

    def seleccionar_semestre(self, model, ite, data):
        """
        Relacion con el metodo de filtro para el treeview

        @param model: Modelo
        @param ite: iterador
        @param data: datos relacionados
        """
        if (self.semestre_actual == 0):
            return True
        else:
            return model[ite][5] == self.semestre_actual

    def on_btn_semestre_siguiente_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de Estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (not self.semestre_actual+1 == 15):
            self.semestre_actual += 1

        self.language_filter.refilter()

    def on_btn_semestre_anterior_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de Estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (not self.semestre_actual-1 == -1):
            self.semestre_actual -= 1

        self.language_filter.refilter()

    def on_btn_seleccionar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de Estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (self.formulario_siguiente == ""):
            #Modificar
            pass
        else:
            pass

    def on_btn_borrar_clicked(self, widget):
        """
        Evento que funciona al accionar el boton de Estudiante

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
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

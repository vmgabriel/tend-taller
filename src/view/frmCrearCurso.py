#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: GPL 3.0
# @author: Gabriel Vargas Monroy

# Dependencies
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Modelo
from model.Curso import Curso

#controller
from controller.Departamento import Departamento_service
from controller.Curso import Curso_service

class Frm_Crear_Curso(Gtk.Window):
    """
    Clase en la que se va a poder crear o modificar curso
    """
    def __init__(self, profesor=0, datos=None):
        """
        Construtor de la clase Frm_Crear_Curso, enfocado a la vista

        @param profesor: Dato importante del profesor encargado
        @type profesor: int
        """
        self.profesor = profesor
        self.titulo = "Crear Curso"
        self.datos = datos
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

        self.c_dia = Gtk.Calendar()
        box_p.pack_end(self.c_dia, True, True, 1)

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
        for country in list(map(self.solo_nombre, self.lista_facultades)):
            country_store.append([country])

        self.cb_lug_edificio = Gtk.ComboBox.new_with_model(country_store)

        renderer_text = Gtk.CellRendererText()
        self.cb_lug_edificio.pack_start(renderer_text, True)
        self.cb_lug_edificio.add_attribute(renderer_text, "text", 0)
        box_p.pack_end(self.cb_lug_edificio, True, True, 1)

        #Hacer parte para activar la seleccion

        self.lbl_lug_edificio = Gtk.Label("Seleccione Edificio:")
        box_p.pack_end(self.lbl_lug_edificio, False, False, 1)

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

    def cargar_datos(self):
        """
        Datos especificamente obtenidos de la base de datos puestos en el departamento
        """
        servicio = Departamento_service()
        self.lista_facultades = servicio.ver_todos()

    def solo_nombre(self, tupla):
        """
        Proceso funcional para que solo se tome el atributo de la posicion 1
        @param tupla: Tupla
        @type tupla: tuple

        @return: datos str con el nombre
        @rtype: str
        """
        return tupla[1]

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

        if (self.datos):
            self.txt_nombre.set_text(self.datos[1])
            self.txt_aula.set_text(self.datos[2])
            self.txt_tiempo.set_text(str(self.datos[3]))

        return box_p

    def dev_frm(self):
        """
        Enfocado en la construccion de cada una de las partes del formulario
        este funcionara cargando la caja principal y mostrando algunas propiedades del mismo
        """
        self.cargar_datos()
        index = self.index_box()
        self.add(index)

        self.connect("delete-event", self.destroy)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size (600, 600)
        self.show_all()

    def on_btn_guardar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        if (self.txt_nombre.get_text() == "" or self.txt_aula.get_text() == "" or self.txt_tiempo.get_text() == ""):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CANCEL, "Datos no Introducidos")
            dialog.format_secondary_text(
                "Uno o mas datos no han sido introducidos")
            dialog.run()
            dialog.destroy()
        else:
            if (self.datos):
                self.modificar()
            else:
                self.eliminar()
            self.destroy()

    def modificar(self):
        """
        Especializacion de Modificar
        """
        tiempo = int(self.txt_tiempo.get_text())
        facultad = self.lista_facultades[self.cb_lug_edificio.get_active()][0]
        fi = self.c_dia.get_date()
        m_curso = Curso(self.txt_nombre.get_text(), self.txt_aula.get_text(), tiempo, fi, facultad, self.datos[0])
        m_curso.set_profesor(self.datos[6])

        service = Curso_service()
        if (service.modificar(m_curso)):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.CANCEL, "Datos Modifcados correctamente")
            dialog.format_secondary_text("Datos modificados en la base de datos satisfactoriamente")
            dialog.run()
            dialog.destroy()
        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CANCEL, "Error almacenamiento de datos")
            dialog.format_secondary_text("Error de atualizacion de datos en la base de datos, comuniquese con soporte tecnico")
            dialog.run()
            dialog.destroy()

    def eliminar(self):
        """
        Especializacion de eliminar
        """
        tiempo = int(self.txt_tiempo.get_text())
        facultad = self.lista_facultades[self.cb_lug_edificio.get_active()][0]
        fi = self.c_dia.get_date()

        nuevo_curso = Curso(self.txt_nombre.get_text(), self.txt_aula.get_text(), tiempo, fi, facultad)
        nuevo_curso.set_profesor(self.profesor)

        service = Curso_service()
        if (service.guardar(nuevo_curso)):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.CANCEL, "Datos Introducidos")
            dialog.format_secondary_text("Datos introducidos satisfactoriamente")
            dialog.run()
            dialog.destroy()
        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CANCEL, "Error almacenamiento de datos")
            dialog.format_secondary_text("Error de guardado de datos en la base de datos, comuniquese con soporte tecnico")
            dialog.run()
            dialog.destroy()

    def on_btn_borrar_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.txt_nombre.set_text("")
        self.txt_aula.set_text("")
        self.txt_tiempo.set_text("")
        self.txt_nombre.grab_focus_without_selecting()

    def on_btn_salir_clicked(self, widget):
        """
        Evento para button cuando este se hace clic

        @param widget: Widget que esta relacionado al evento
        @type widget: Gtk.Widget
        """
        self.destroy()

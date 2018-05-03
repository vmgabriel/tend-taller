#!/urs/bin/env python
# -*- coding: utf-8 -*-

#modulos
import psycopg2, psycopg2.extras
import sys

"""
Conexion a Base de Datos

@author: Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Conexion:
    """
    Clase para la consolidacion con la base de datos
    """
    conn = None

    def __init__(self):
        """
        Variables caracteristicas para la conexion de base de datos, variables caracteristicas para el uso de la misma
        """
        self.base = "tendencias_taller"
        self.usuario = "postgres"
        self.contra = "admin"
        self.dispositivo = "localhost"
        """
        Explicacion del dispositivo:
        - self.dispositivo = "localhost" or "127.0.0.1"
        Datos dispositivo actual
        """

    def enviar_registro(self, estructura, datos):
        """
        Una consulta caracterizada por el envio de informacion, nada de traer datos, ya que si existe algu tipo de error este funcionara de esa manera
        - estructura funciona de la siguiente manera: "insert into people values (%s, %s)"
        - datos funciona como los datos arrojados para ser enviados


        @param estructura: Variable caracteristica que enfoca en enviar la consulta como un string, se  nota que este archivo funciona como puente, ademas es una estructura de la misma, para que ella la reconozca
        @type estructura: str

        @param datos: Datos que van a ser tomados para ser ingresados en la estructura ingresada como parametro 1
        @type datos: <class ="tuple">
        """
        try:
            self.conector()
            cur = self.conn.cursor()
            cur.execute(query, iny)
            self.conn.commit()
            cur.close()
        except psycopg2.DatabaseError as e:
            if self.conn:
                self.conn.rollback()

            print ('Error {}'.format(e))
            sys.exit(1)
        finally:
            self.conn.close()

    def enviar_consulta(self, query):
        """
        Con enviar consulta,unicamente se envia la consulta ya tratada con los datos ingresados en un str y puestas para enviarse a DB

        @param query: consulta que se desea enviar
        @type quiery: str

        @return: lista de consulta de salida de datos tomado de la base de datos
        @rtype: <class 'list'>
        """
        try:
            self.conector()
            cur = self.conn.cursor()
            cur.execute(query)
            datos = cur.fetchall()
            cur.close()
            return datos
        except psycopg2.DatabaseError as e:
            if self.conn:
                self.conn.rollback()

            print ('Error {}'.format(e))
            sys.exit(1)
        finally:
            self.conn.close()

    def conector(self):
        """
        variable principal que se caracteriza por tener los datos de la conexion de base de datos
        """
        self.conn = psycopg2.connect(database = self.base, user = self.usuario,
                                     password = self.contra, host = self.dispositivo)

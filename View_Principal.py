import os , sys , pathlib

import Cajas as Cajas_py , Geneticos as Geneticos_py , Cumulo_de_Particulas as Cumulo_de_Particulas_py

from PyQt5 import *
from PyQt5 import uic , QtWidgets #Carga la interfaz  grafica
from PyQt5.QtWidgets import QMainWindow , QApplication , QTableWidgetItem , QMessageBox

class Inicio_App( QMainWindow ):

	def __init__(self):

		super().__init__()
		uic.loadUi( 'View_Principal.ui' , self )

		self.init_component()

	def init_component( self ):
		# -------------------->>>>>
		self.checkBox_Algoritmo_Genetico.setChecked(True)
		self.checkBox_Algoritmo_Genetico.setEnabled(False)
		
		self.generar_table_cajas()

		self.Button_Ordenar_Cajas.clicked.connect( self.Ordenar_Cajas )

		self.Button_Guardar_Cajas.clicked.connect( self.guardar_cajas_formato_txt )
		# -------------------->>>>>
	
	def ventana_emergente_de_texto( self , titulo_ventana , texto_ventana ):
		dlg = QMessageBox(self)
		dlg.setWindowTitle( titulo_ventana )
		dlg.setText( texto_ventana )
		dlg.show()

	def Ordenar_Cajas( self ):
		try:
			Ancho_Contenedor = int( self.Text_Ancho_Contenedor.text() )
			Alto_Contenedor = int( self.Text_Alto_Contenedor.text() )
			Altura_Arboles_Ordenamiento = int( self.Text_Altura_Arboles_Ordenamiento.text() )
		except:
			self.ventana_emergente_de_texto( 'Error Campo' , 'Campo 1 error: Contenedor , Altura Arboles de Ordenamiento' )
			return None
		try:
			Cant_Individuos_AG = int( self.Text_Cant_Individuos_AG.text() )
			Cant_Iteraciones_AG = int( self.Text_Cant_Iteraciones_AG.text() )
		except:
			self.ventana_emergente_de_texto( 'Error Campo' , 'Campo AG error: Cant Individuos AG , Cant Iteraciones AG' )
			return None
		
		Contenedor = (Ancho_Contenedor , Alto_Contenedor)
		ListaCajas = self.obtener_cajas_de_Table_Cajas()
		print("Ejecutando Algoritmo Genetico")
		GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos_AG , Altura_Arboles_Ordenamiento , ListaCajas)
		GA.algoritmo_genetico( Cant_Iteraciones_AG )
		print("Finalizado ejecucion de Algoritmo Genetico")

		if self.checkBox_Algoritmo_PSO.isChecked():
			try:
				Cant_Individuos_PSO = int( self.Text_Cant_Individuos_PSO.text() )
				Cant_Iteraciones_PSO = int( self.Text_Cant_Iteraciones_PSO.text() )

				print("Iniciando ejecucion de Algoritmo Cumulo de Particulas")
				PSO_ = Cumulo_de_Particulas_py.Algoritmo_Cumulo_de_Particulas( Contenedor , Cant_Individuos_PSO , Altura_Arboles_Ordenamiento , ListaCajas )
				PSO_.algoritmo_pso( Cant_Iteraciones_PSO , GA.poblacion[0] )
				print("Finalizado ejecucion de Algoritmo Cumulo de Particulas")
				
				PSO_.poblacion[0].genera_grafica_rectangular_arbol()
				self.ventana_emergente_de_texto( 'Gracias' , 'Proceso Finalizado, Area ordenada: ' )

			except:
				self.ventana_emergente_de_texto( 'Error Campo' , 'Campo PSO error: Cant Individuos PSO , Cant Iteraciones PSO' )
		else:
			GA.poblacion[0].genera_grafica_rectangular_arbol()
			self.ventana_emergente_de_texto( 'Gracias' , 'Proceso Finalizado, Area ordenada: ' )

	def guardar_cajas_formato_txt( self ):
		self.ventana_emergente_de_texto( 'Proceso no terminado' , 'Proceso terminado: diego.xmen123@gmail.com' )

	def obtener_cajas_de_Table_Cajas( self ):

		Lista_Cajas = []
		count_row = self.Table_Cajas_a_Ordenar.rowCount()
		for num_row in range( count_row ):
			try:
				caja_Ancho = float( self.Table_Cajas_a_Ordenar.item( num_row , 0).text() )
				caja_Alto = float( self.Table_Cajas_a_Ordenar.item( num_row , 1).text() )
				Lista_Cajas.append( (caja_Ancho,caja_Alto) )
			except:
				pass
		return Lista_Cajas

	def generar_table_cajas( self ):
		self.Table_Cajas_a_Ordenar.setRowCount(100)
		self.Table_Cajas_a_Ordenar.setColumnCount( 2 )
		self.Table_Cajas_a_Ordenar.setHorizontalHeaderLabels(['Ancho' , 'Alto'])

		self.Table_Cajas_a_Ordenar.setColumnWidth(0, 219)
		self.Table_Cajas_a_Ordenar.setColumnWidth(1, 219)



app = QApplication( sys.argv )

Aplicacion = Inicio_App()
Aplicacion.setFixedSize( 572, 676 ) #759
Aplicacion.show()

sys.exit( app.exec_() )
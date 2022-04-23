#---> Casos a tomar en cuenta
# Si no encaja entonces verificamos invirtiendo , es el unico caso
#--->

import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Node_Contenedor():
	def __init__( self , dimencion , padre ):
		self.dimencion = dimencion #Tamanio Caja (Ancho , Alto)
		self.cajaInterna = None #La Caja que contiene (Ancho , Alto) , Si queda en None indica Vacio
		self.padre = padre

		#Si atributo cajaInterna != None entonces esta haran referencia a otros NodosContenedores
		self.Contenedor_Arriba = None #Referencia a contenedor arriba 
		self.Contenedor_Alado = None #Referencia a contenedor alado

class Arbol_Posicionamiento_Cajas():
	
	def __init__( self ):
		self.raiz = None

	def Ver_Arbol( self ):
		ListaArb = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )

		contNivel = 0
		for nivel in ListaArb:
			print( '~~~~~~>>>>>>' )
			print("Nivel: " + str( contNivel ) + " ~~> " )
			for nodo in nivel:
				if contNivel == 0:
					print( str( nodo.dimencion ) , " - None " )
				else:
					if nodo.cajaInterna != None:
						print( " Nodo ~> Dim: " , str( nodo.dimencion ) , " ; Caja Interna: " , str( nodo.cajaInterna ) , " ; Padre: " , str( nodo.padre.dimencion ) )
					else:
						print( " Hoja~> Dim: ", str( nodo.dimencion ) , " ; Padre: " , str( nodo.padre.dimencion ) )
			print( '~~~~~~>>>>>> \n' )
			contNivel += 1
	
	def representacion_en_forma_de_lista( self , nodoActual , ListaArbol , nivel ):

		try:
			ListaArbol[nivel].append( nodoActual ) #Si la lista nivel no existe
		except:
			ListaArbol.insert( nivel , [ nodoActual ] ) #Insertamos una lista con referencia al nodo actual

		if nodoActual.cajaInterna != None:
			ListaArbol = self.representacion_en_forma_de_lista( nodoActual.Contenedor_Alado , ListaArbol , nivel+1 )
			ListaArbol = self.representacion_en_forma_de_lista( nodoActual.Contenedor_Arriba , ListaArbol , nivel+1 )

		return ListaArbol

	def add_Cajas( self , ref_ContenedorActual , ListaCajasDisponibles ): 
		Caja_Encontrada = False
		for pos in range( len(ListaCajasDisponibles) ):

			Ingresado = False
			CajaIngresado = (0,0)

			if ref_ContenedorActual.dimencion[0] >= ListaCajasDisponibles[pos][0]:
				if ref_ContenedorActual.dimencion[1] >= ListaCajasDisponibles[pos][1] :
					ref_ContenedorActual.cajaInterna = ListaCajasDisponibles[pos] #Ingresamos esa caja
					CajaIngresado = ListaCajasDisponibles[pos]
					Ingresado = True

			if Ingresado == False: #Verificamos si se puede ingresar en inversa
				if ref_ContenedorActual.dimencion[0] >= ListaCajasDisponibles[pos][1]:
					if ref_ContenedorActual.dimencion[1] >= ListaCajasDisponibles[pos][0]:
						ref_ContenedorActual.cajaInterna = ( ListaCajasDisponibles[pos][1] , ListaCajasDisponibles[pos][0] ) #Ingresamos esa caja pero invertido
						CajaIngresado = ( ListaCajasDisponibles[pos][1] , ListaCajasDisponibles[pos][0] )
						Ingresado = True

			if Ingresado == True:

				ListaCajasDisponibles.pop( pos ) #Quitamos elemento ingresado a caja de la lista
				
				x_ContenedorArriba = ref_ContenedorActual.dimencion[0] 
				y_ContenedorArriba = ref_ContenedorActual.dimencion[1] - CajaIngresado[1]
				ref_ContenedorActual.Contenedor_Arriba = Node_Contenedor( (x_ContenedorArriba , y_ContenedorArriba ) , ref_ContenedorActual )

				x_ContenedorAlado = ref_ContenedorActual.dimencion[0] - CajaIngresado[0]
				y_ContenedorAlado = CajaIngresado[1]
				ref_ContenedorActual.Contenedor_Alado = Node_Contenedor( (x_ContenedorAlado , y_ContenedorAlado) , ref_ContenedorActual )

				ListaCajasDisponibles = self.add_Cajas( ref_ContenedorActual.Contenedor_Alado , ListaCajasDisponibles )

				ListaCajasDisponibles = self.add_Cajas( ref_ContenedorActual.Contenedor_Arriba , ListaCajasDisponibles )

				break

		return ListaCajasDisponibles

	def espacios_vacios( self ):
		#Retorna los espacios disponibles luego de ingresado las cajas

		ListaArbol = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		Lista_Espacio_Disponibles = []
		for nivel in ListaArbol:
			for nodo in nivel:
				if nodo.cajaInterna == None and ( nodo.dimencion[0]!=0 and nodo.dimencion[1]!=0 ):
					Lista_Espacio_Disponibles.append( nodo )
		return Lista_Espacio_Disponibles

	def genera_grafica_rectangular_arbol( self ):

		fig, ax = plt.subplots()

		X = [ 0 , self.raiz.dimencion[0]]
		Y = [ 0 , self.raiz.dimencion[1] ]
		
		ax.plot( X , Y ) #Dimencion de la caja

		self.ingresando_cajas( self.raiz , (0,0) , ax)
		
		plt.show()

	def ingresando_cajas( self , nodo_actual , punto_inicio , obj_grafico ):
		if nodo_actual.cajaInterna != None:
			obj_grafico.add_patch(
				patches.Rectangle(
				punto_inicio , #Punto Inicio
				nodo_actual.cajaInterna[0] , #x anchura
				nodo_actual.cajaInterna[1] , #y altura
				edgecolor = 'black',
				facecolor = 'brown',
				fill=True
			) )

			punto_inicio_alado = ( punto_inicio[0] + nodo_actual.cajaInterna[0] , punto_inicio[1] ) 
			self.ingresando_cajas( nodo_actual.Contenedor_Alado , punto_inicio_alado , obj_grafico )
			
			punto_inicio_arriba = ( punto_inicio[0] , punto_inicio[1] + nodo_actual.cajaInterna[1] ) 
			self.ingresando_cajas( nodo_actual.Contenedor_Arriba , punto_inicio_arriba , obj_grafico )

def OrdenandoMayorMenor_ListaCajas( Lista_Cajas ):
	Lista_Cajas.sort() #Ordenamos de menor a mayor las tuplas
	Lista_Cajas = Lista_Cajas[::-1] #Invertimos las listas
	return Lista_Cajas


# ------------------->>>
# -- Configuracion -->>>
Contenedor = (5,4)
ListaCajas = [ (6,4) , (2,2) , (2,2) , (2,2) , (2,1) , (2,1) , (2,1) , (1,1) ]
# ------------------->>>
# ------------------->>>
'''
ListaCajas = OrdenandoMayorMenor_ListaCajas( ListaCajas )

Arbol = Arbol_Posicionamiento_Cajas()
Arbol.raiz = Node_Contenedor( Contenedor , None ) #El padre del Nodo es None
Arbol.add_Cajas( Arbol.raiz , ListaCajas )

#Arbol.Ver_Arbol()
Arbol.genera_grafica_rectangular_arbol()
'''
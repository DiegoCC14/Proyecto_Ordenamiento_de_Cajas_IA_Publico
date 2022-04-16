
#---> Casos a tomar en cuenta
# Si no encaja entonces verificamos invirtiendo , es el unico caso
#--->

class Node_Contenedor():
	def __init__( self , dimencion , padre ):
		self.dimencion = dimencion #Tamanio Caja (Ancho , Alto)
		self.cajaInterna = None #La Caja que contiene (Ancho , Alto) , Si queda en None indica Vacio
		self.padre = padre

		#Si atributo cajaInterna != None entonces esta haran referencia a otros NodosContenedores
		self.Contenedor_Arriba = None #Referencia a contenedor arriba 
		self.Contenedor_Alado = None #Referencia a contenedor alado

class Arbol_Posicionamiento_Cajas():
	
	def __init__( self , DimencionCajaContenedor , CajasIngresar ):
		self.raiz = None
		self.ListaCajas = CajasIngresar
		self.DimencionCajaContenedor = DimencionCajaContenedor

	def Ver_Arbol( self ):
		ListaArb = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		ListaArb = Arbol.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		
		contNivel = 0
		for nivel in ListaArb:
			print( '~~~~~~>>>>>>' )
			print("Nivel: " + str( contNivel ) + " ~~> " )
			for nodo in nivel:
				if contNivel == 0:
					print( str( nodo.dimencion ) , " ; Caja Interna: " , str( nodo.cajaInterna ) , " ; Padre: None ")
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

	def obtener_cajas_ingresadas( self ):

		ListaArbol = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		Lista_Cajas_Ingresadas = []
		for nivelArbol in ListaArbol:
			for nodo in nivelArbol:
				if nodo.cajaInterna != None:
					Lista_Cajas_Ingresadas.append( nodo.cajaInterna )
		return Lista_Cajas_Ingresadas

	def obtener_cajas_no_ingresadas( self ):
		ListaCajasTotal = self.ListaCajas.copy()
		ListCajasIngresadas = self.obtener_cajas_ingresadas()
		for cajaIngresada in ListCajasIngresadas:
			try:
				ListaCajasTotal.remove( cajaIngresada )
			except:
				inv_cajaIngresada = ( cajaIngresada[1] , cajaIngresada[0] )
				ListaCajasTotal.remove( inv_cajaIngresada )
		return ListaCajasTotal

	def obtener_espacios_vacios( self ):
		ListaArbol = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		Lista_Espacios_vacios = []
		for nivelArbol in ListaArbol:
			for nodo in nivelArbol:
				if nodo.cajaInterna == None and nodo.dimencion[0]!=0 and nodo.dimencion[1]!=0 :
					Lista_Espacios_vacios.append( nodo.dimencion )
		return Lista_Espacios_vacios

	def espacios_vacios( self ):
		#Retorna los espacios disponibles luego de ingresado las cajas

		ListaArbol = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		Lista_Espacio_Disponibles = []
		for nivel in ListaArbol:
			for nodo in nivel:
				if nodo.cajaInterna == None and ( nodo.dimencion[0]!=0 and nodo.dimencion[1]!=0 ):
					Lista_Espacio_Disponibles.append( nodo )
		return Lista_Espacio_Disponibles

def OrdenandoMayorMenor_ListaCajas( Lista_Cajas ):
	Lista_Cajas.sort() #Ordenamos de menor a mayor las tuplas
	Lista_Cajas = Lista_Cajas[::-1] #Invertimos las listas
	return Lista_Cajas

'''
# ------------------->>>
# -- Configuracion -->>>

Contenedor = (38,24)
ListaCajas = [ (19,14) , (19,14) , (6,9) , (6,9) , (6,3) , (6,3) , (6,6) , (6,6) , (6,6) , (6,6) , (3,9) , (3,9) , (1,10) , (1,10) , (1,10) , (1,10) ]

Contenedor = (5,4)
ListaCajas = [ (6,4) , (2,2) , (2,2) , (2,2) , (2,1) , (2,1) , (2,1) , (1,1) ]

# ------------------->>>
# ------------------->>>


ListaCajas = OrdenandoMayorMenor_ListaCajas( ListaCajas )

Arbol = Arbol_Posicionamiento_Cajas( Contenedor , ListaCajas.copy() )
Arbol.raiz = Node_Contenedor( Contenedor , None ) #El padre del Nodo es None
Arbol.add_Cajas( Arbol.raiz , ListaCajas.copy() )

Arbol.Ver_Arbol()

print( Arbol.obtener_cajas_ingresadas() )
print( Arbol.obtener_cajas_no_ingresadas() )
print( Arbol.obtener_espacios_vacios() )

TamTotal = Arbol.obtener_cajas_ingresadas()
x = 0
y = 0
for dim in TamTotal:
	x += dim[0]
	y += dim[1]


print( (x,y) )

Arbol.Ver_Arbol()
'''

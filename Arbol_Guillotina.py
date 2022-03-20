import random

class Node_Hoja_Guillotina():
	def __init__( self , dimencionCaja , padre ):
		self.dimencionCaja = dimencionCaja
		self.padre = padre

class Node_CorteGuillotina():
	def __init__( self , dimencionCaja , corte , Porcentaje_de_Corte , padre ):
		self.dimencionCaja = dimencionCaja
		self.corte = corte #Puede ser Vertical o Horizontal sobre la caja
		self.Porcentaje_de_Corte = Porcentaje_de_Corte
		self.padre = padre

		self.nodo_derecho = None #Puede referir a un Nodo Caja o Nodo Corte Guillotina
		self.nodo_izquierdo = None #Puede referir a un Nodo Caja o Nodo Corte Guillotina

class Arbol_de_CorteGuillotina():
	
	def __init__( self , altura_arbol ):
		#Los cortes seran aleatorios, rango [0:1]
		self.raiz = None
		self.altura = altura_arbol
	
	def VerArbol_CorteGuillotina( self ):
		Lista_Arbol = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		contNivel = 0
		for nivel in Lista_Arbol:

			print( "----------------->>>>> \n Nivel: " , contNivel )
			for nodo in nivel:
				if contNivel == 0:
					print(" Nodo ~> Dim: " + str( nodo.dimencionCaja ) + " - Corte: " + nodo.corte + " - Padre: None " )
				elif contNivel == self.altura :
					print(" Hoja ~> Dim:" + str( nodo.dimencionCaja ) + " - Padre: " +str( nodo.padre.dimencionCaja ) )
				else:
					print( " Nodo ~> Dim: "+str( nodo.dimencionCaja ) + " - Corte: " + nodo.corte +" - Padre: " +str( nodo.padre.dimencionCaja ) )
			contNivel += 1
			print( "----------------->>>>>\n")

	def Arma_arbolGuillotina_aleatoriamente( self , nodoActual , altura_Actual ):
		
		TamCaja = nodoActual.dimencionCaja
		if nodoActual.corte == "V":
			TamCajaDerecha = ( TamCaja[0] * nodoActual.Porcentaje_de_Corte , TamCaja[1] )
			TamCajaIzquierda = ( TamCaja[0] - ( TamCaja[0] * nodoActual.Porcentaje_de_Corte ) , TamCaja[1] )
		elif nodoActual.corte == "H":
			TamCajaDerecha = ( TamCaja[0] , TamCaja[1] * nodoActual.Porcentaje_de_Corte )
			TamCajaIzquierda = ( TamCaja[0] , TamCaja[1] - ( TamCaja[1] * nodoActual.Porcentaje_de_Corte ) )
		
		if altura_Actual == 1:
			nodoActual.nodo_derecho = Node_Hoja_Guillotina( TamCajaDerecha , nodoActual )
			nodoActual.nodo_izquierdo = Node_Hoja_Guillotina( TamCajaIzquierda , nodoActual )

		else:
			corteNodeDerecha = self.corte_aleatorio_vertical_o_horizontal()
			corteNodeIzquierdo = self.corte_aleatorio_vertical_o_horizontal()

			nodoActual.nodo_derecho = Node_CorteGuillotina( TamCajaDerecha , corteNodeDerecha , random.random() , nodoActual )
			nodoActual.nodo_izquierdo = Node_CorteGuillotina( TamCajaIzquierda , corteNodeIzquierdo , random.random() , nodoActual )
			
			self.Arma_arbolGuillotina_aleatoriamente( nodoActual.nodo_derecho , altura_Actual-1 )
			self.Arma_arbolGuillotina_aleatoriamente( nodoActual.nodo_izquierdo , altura_Actual-1 )

	def representacion_en_forma_de_lista( self , nodoActual , ListaArbol , nivel ):

		try:
			ListaArbol[nivel].append( nodoActual ) #Si la lista nivel no existe
		except:
			ListaArbol.insert( nivel , [ nodoActual ] ) #Insertamos una lista con referencia al nodo actual
		
		if nivel != self.altura:	
			if nodoActual.nodo_derecho != None and nodoActual.nodo_izquierdo != None:
				ListaArbol = self.representacion_en_forma_de_lista( nodoActual.nodo_derecho , ListaArbol , nivel+1 )
				ListaArbol = self.representacion_en_forma_de_lista( nodoActual.nodo_izquierdo , ListaArbol , nivel+1 )
		
		return ListaArbol

	def corte_aleatorio_vertical_o_horizontal( self ):
		if random.random() > 0.5:
			return "H"
		return "V"

# ------------------->>>
# -- Configuracion -->>>
Altura_Arbol = 5
Dimencion_Caja = (8,5)
# ------------------->>>
# ------------------->>>


ArbolGuillotina = Arbol_de_CorteGuillotina( Altura_Arbol )
corte = ArbolGuillotina.corte_aleatorio_vertical_o_horizontal()
ArbolGuillotina.raiz = Node_CorteGuillotina( Dimencion_Caja , corte , random.random() , None )

ArbolGuillotina.Arma_arbolGuillotina_aleatoriamente( ArbolGuillotina.raiz , ArbolGuillotina.altura )


#Lista = ArbolGuillotina.representacion_en_forma_de_lista( ArbolGuillotina.raiz , [] , 0 )

ArbolGuillotina.VerArbol_CorteGuillotina()
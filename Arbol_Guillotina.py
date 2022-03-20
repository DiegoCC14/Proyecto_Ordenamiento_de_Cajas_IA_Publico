import random

class Node_Hoja_Guillotina():
	def __init__( self , dimencionCaja ):
		self.dimencionCaja = dimencionCaja

class Node_CorteGuillotina():
	def __init__( self , dimencionCaja , corte , Porcentaje_de_Corte ):
		self.dimencionCaja = dimencionCaja
		self.corte = corte #Puede ser Vertical o Horizontal sobre la caja
		self.Porcentaje_de_Corte = Porcentaje_de_Corte
		
		self.nodo_derecho = None #Puede referir a un Nodo Caja o Nodo Corte Guillotina
		self.nodo_izquierdo = None #Puede referir a un Nodo Caja o Nodo Corte Guillotina

class Arbol_de_CorteGuillotina():
	def __init__( self , altura_arbol ):
		#Los cortes seran aleatorios, rango [0:1]
		self.raiz = None
		self.altura = altura_arbol
	
	def VerArbolCorteGuillotina( self , nodoActual ):
		
		print( '~~~~~~>>>>>>' )
		print( "Dimenencion: ", nodoActual.dimencionCaja )
		try:
			print( "Corte %: ", nodoActual.corte , nodoActual.Porcentaje_de_Corte  )
			print( '~~~~~~>>>>>>' )
			self.VerArbolCorteGuillotina( nodoActual.nodo_derecho )
			self.VerArbolCorteGuillotina( nodoActual.nodo_izquierdo )
		except:
			pass

	def Arma_arbolGuillotina_aleatoriamente( self , nodoActual , altura_Actual ):
		
		TamCaja = nodoActual.dimencionCaja
		if nodoActual.corte == "V":
			TamCajaDerecha = ( TamCaja[0] * nodoActual.Porcentaje_de_Corte , TamCaja[1] )
			TamCajaIzquierda = ( TamCaja[0] - ( TamCaja[0] * nodoActual.Porcentaje_de_Corte ) , TamCaja[1] )
		elif nodoActual.corte == "H":
			TamCajaDerecha = ( TamCaja[0] , TamCaja[1] * nodoActual.Porcentaje_de_Corte )
			TamCajaIzquierda = ( TamCaja[0] , TamCaja[1] - ( TamCaja[1] * nodoActual.Porcentaje_de_Corte ) )
		
		if altura_Actual == 1:
			nodoActual.nodo_derecho = Node_Hoja_Guillotina( TamCajaDerecha )
			nodoActual.nodo_izquierdo = Node_Hoja_Guillotina( TamCajaIzquierda )

		else:
			corteNodeDerecha = self.corte_aleatorio_vertical_o_horizontal()
			corteNodeIzquierdo = self.corte_aleatorio_vertical_o_horizontal()

			nodoActual.nodo_derecho = Node_CorteGuillotina( TamCajaDerecha , corteNodeDerecha , random.random() )
			nodoActual.nodo_izquierdo = Node_CorteGuillotina( TamCajaIzquierda , corteNodeIzquierdo , random.random() )
			
			self.Arma_arbolGuillotina_aleatoriamente( nodoActual.nodo_derecho , altura_Actual-1 )
			self.Arma_arbolGuillotina_aleatoriamente( nodoActual.nodo_izquierdo , altura_Actual-1 )

	def corte_aleatorio_vertical_o_horizontal( self ):
		if random.random() > 0.5:
			return "H"
		return "V"


ArbolGuillotina = Arbol_de_CorteGuillotina( 3 )
corte = ArbolGuillotina.corte_aleatorio_vertical_o_horizontal()
ArbolGuillotina.raiz = Node_CorteGuillotina( (8,5) , corte , random.random() )

ArbolGuillotina.Arma_arbolGuillotina_aleatoriamente( ArbolGuillotina.raiz , ArbolGuillotina.altura )
ArbolGuillotina.VerArbolCorteGuillotina( ArbolGuillotina.raiz )
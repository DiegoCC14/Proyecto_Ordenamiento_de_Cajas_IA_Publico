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

def OrdenandoMayorMenor_ListaCajas( Lista_Cajas ):
	Lista_Cajas.sort() #Ordenamos de menor a mayor las tuplas
	Lista_Cajas = Lista_Cajas[::-1] #Invertimos las listas
	return Lista_Cajas
'''
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
'''

def Ordenando_cajas_en_contenedor( tam_contenedor , lista_cajas , sumatoria_actual , lista_actual , mejor_acercamiento ):
	if mejor_acercamiento[0] != 0:
		while lista_cajas != [] and mejor_acercamiento[0] != 0:
			numEleccion = lista_cajas.pop(0)
			print( numEleccion )
			if mejor_acercamiento[0] > abs( tam_contenedor - (numEleccion + sumatoria_actual) ) :
				mejor_acercamiento[0] = abs( tam_contenedor - (numEleccion + sumatoria_actual) )
				lista_actual.append( numEleccion )
				mejor_acercamiento[1] = lista_actual.copy()
				print( "Normal ~>",lista_actual , mejor_acercamiento )
				mejor_acercamiento = Ordenando_cajas_en_contenedor(tam_contenedor , lista_cajas.copy() , sumatoria_actual+numEleccion , lista_actual.copy() , mejor_acercamiento )	
				
				lista_actual.remove( numEleccion )
			elif (tam_contenedor-(sumatoria_actual+numEleccion ))>0:
				lista_actual.append( numEleccion )
				mejor_acercamiento = Ordenando_cajas_en_contenedor(tam_contenedor , lista_cajas.copy() , sumatoria_actual+numEleccion , lista_actual.copy() , mejor_acercamiento )
				print( "Menor ~>" , lista_actual , mejor_acercamiento )
				lista_actual.remove( numEleccion )

	return mejor_acercamiento.copy() 

tam_contenedor = 5

#lista = [ 1 , 1 , 1 , 2 , 3 , 4 , 4 ]
lista = [ 4 , 8 , 9 , 7 , 1 , 2 , 3 ]
lista = OrdenandoMayorMenor_ListaCajas( lista )
print( "Salida: ", Ordenando_cajas_en_contenedor( tam_contenedor , lista.copy() , 0 , [] , [ tam_contenedor , [] ] ) )

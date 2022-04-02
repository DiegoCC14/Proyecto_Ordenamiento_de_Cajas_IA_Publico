import Arbol_Posicionamiento_Cajas
import random


class Node_Hoja_Guillotina():
	def __init__( self , dimencionCaja , padre ):
		self.dimencionCaja = dimencionCaja
		self.padre = padre
		self.arbol_posicionamiento_de_cajas = None #Referencia a el arbol de posicionamiento de cajas

class Node_CorteGuillotina():
	def __init__( self , dimencionCaja , corte , Porcentaje_de_Corte , padre ):
		self.dimencionCaja = dimencionCaja
		self.corte = corte #Puede ser Vertical o Horizontal sobre la caja
		self.Porcentaje_de_Corte = Porcentaje_de_Corte
		self.padre = padre

		self.nodo_derecho = None #Puede referir a un Nodo Caja o Nodo Corte Guillotina
		self.nodo_izquierdo = None #Puede referir a un Nodo Caja o Nodo Corte Guillotina

class Arbol_de_CorteGuillotina():
	
	def __init__( self , altura_arbol , contenedor , ListaCajas ):
		#Los cortes seran aleatorios, rango [0:1]
		self.raiz = None
		self.altura = altura_arbol
		self.contenedor = contenedor
		self.Cajas_a_Ingresar = ListaCajas

		self.mal_desempenio = 0 #Indicamos cuanto es el peor desempenio de este arbol 

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
			nodoActual.nodo_derecho.arbol_posicionamiento_de_cajas = Arbol_Posicionamiento_Cajas.Arbol_Posicionamiento_Cajas()
			nodoActual.nodo_derecho.arbol_posicionamiento_de_cajas.raiz = Arbol_Posicionamiento_Cajas.Node_Contenedor( TamCajaDerecha , None ) #El padre del Nodo es None
			
			nodoActual.nodo_izquierdo = Node_Hoja_Guillotina( TamCajaIzquierda , nodoActual )
			nodoActual.nodo_izquierdo.arbol_posicionamiento_de_cajas = Arbol_Posicionamiento_Cajas.Arbol_Posicionamiento_Cajas()
			nodoActual.nodo_izquierdo.arbol_posicionamiento_de_cajas.raiz = Arbol_Posicionamiento_Cajas.Node_Contenedor( TamCajaIzquierda , None ) #El padre del Nodo es None

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

	def obtener_hojas(self):
		lista_arbol = self.representacion_en_forma_de_lista( self.raiz , [] , 0 )
		return( lista_arbol[len(lista_arbol)-1] )

	def calculando_desempenio( self ):
		list_nodos_hojas = self.obtener_hojas()
		list_nodos_hojas.sort( key=lambda casilla: casilla.dimencionCaja )
		
		cajasIngresar = self.Cajas_a_Ingresar.copy()

		for hoja_guillotina in list_nodos_hojas: #Ingresamos las cajas al arbol
			cajasIngresar = hoja_guillotina.arbol_posicionamiento_de_cajas.add_Cajas( hoja_guillotina.arbol_posicionamiento_de_cajas.raiz , cajasIngresar )
		
		print( "Cajas sin ingresar: ",cajasIngresar ) #Las cajas que no se ingresaron
		lista_espacios_vacios = []
		for hoja_guillotina in list_nodos_hojas: #Ingresaremos las cajas vacias a una lista para el calculo de mal desempenio
			#Para el calculo del desempenio , necesitamos solo las dimenciones
			lista_espacios_vacios += [ nodo_hoja.dimencion for nodo_hoja in hoja_guillotina.arbol_posicionamiento_de_cajas.espacios_vacios()]
			
		lista_espacios_vacios.sort()
		lista_espacios_vacios = lista_espacios_vacios[::-1] #Invertimos la listas de Mayor a Menor
		print( 'Espacios vacios: ', lista_espacios_vacios )
		cajasSinIngresar = []
		for caja in cajasIngresar:
			cajasSinIngresar.append( [ caja ] )
			if caja[0] != caja[1]:
				cajasSinIngresar[ len(cajasSinIngresar)-1 ].append( ( caja[1] , caja[0] ) )

		print( "cajasSinIngresar: ",cajasSinIngresar )
		print("~~~~~~~~~~~~~~~~~~>>>>>>>>")
		for parCajas in cajasSinIngresar:

			menor_desempenio = parCajas[0][0] * parCajas[0][1] #El area es la misma
			mejor_caja = None
			print("Iter: ",menor_desempenio)
			area_desperdiciada = 0
			for caja in parCajas: #Puede ser la caja acostada o parada 2 versiones
				for espacio_vacio in lista_espacios_vacios:
					res_tupla = diferencia_entre_cajas( caja , espacio_vacio )
					#print( res_tupla )
					if res_tupla[0] < menor_desempenio:
						menor_desempenio = res_tupla[0]
						area_desperdiciada = res_tupla[2]
						mejor_caja = espacio_vacio

			print( caja , " - ", espacio_vacio ," - ", menor_desempenio , " - ", area_desperdiciada ,"~~~~~~~~~>>>>>>>>")
			lista_espacios_vacios.remove( mejor_caja )
			print("Cajas Vacias: ", lista_espacios_vacios )
			print("~~~~~~~~~~~~~~~~~~>>>>>>>>")

def diferencia_entre_cajas( caja_grande , caja_pequenia ):
	#contenedor es la caja mas grande
	#tam_caja es caja pequenia
	#caul es la diferencia entre areas de cajas

	res_x = caja_grande[0] - caja_pequenia[0]
	res_y = caja_grande[1] - caja_pequenia[1]
	print( 'Res:',res_x , res_y )
	valor_negativo = None #Que posicion es negativa
	area_desperdiciada = 0

	caja_arriba = 0
	if res_y >= 0:
		caja_arriba = res_y * caja_grande[1]
	else:
		valor_negativo = 0
		area_desperdiciada = res_y * caja_pequenia[0]
	
	caja_alado = 0
	if res_x >= 0:
		caja_alado = res_x * caja_grande[1] #area caja alado
	else:
		valor_negativo = 1
		area_desperdiciada = res_x * caja_pequenia[1]
	if valor_negativo != None:
		area_total = caja_arriba + caja_alado
	else:
		area_total = caja_arriba + caja_alado - res_y * res_x

	print("Area Total: ", area_total , area_total + abs( area_desperdiciada ) )
	return ( area_total + abs( area_desperdiciada ) , valor_negativo , area_desperdiciada )

def OrdenandoMayorMenor_ListaCajas( Lista_Cajas ):
	Lista_Cajas.sort() #Ordenamos de menor a mayor las tuplas
	Lista_Cajas = Lista_Cajas[::-1] #Invertimos las listas
	return Lista_Cajas

'''
lista = [{'numero':6} , {'numero':1} , {'numero':3} , {'numero':5}]
lista.sort( key=lambda casilla: casilla['numero'])
print( lista )
'''

# ------------------->>>
# -- Configuracion -->>>
Altura_Arbol = 3
Contenedor = (5,4)
ListaCajas = [ (1,3) , (2,2) , (2,2) , (2,1) , (2,1) , (2,1) , (1,1) ]
# ------------------->>>
# ------------------->>>

ArbolGuillotina = Arbol_de_CorteGuillotina( Altura_Arbol , Contenedor , ListaCajas )
corte = ArbolGuillotina.corte_aleatorio_vertical_o_horizontal()
ArbolGuillotina.raiz = Node_CorteGuillotina( Contenedor , corte , random.random() , None )

ArbolGuillotina.Arma_arbolGuillotina_aleatoriamente( ArbolGuillotina.raiz , ArbolGuillotina.altura )

ArbolGuillotina.calculando_desempenio()

#Lista = ArbolGuillotina.representacion_en_forma_de_lista( ArbolGuillotina.raiz , [] , 0 )

#ArbolGuillotina.VerArbol_CorteGuillotina()

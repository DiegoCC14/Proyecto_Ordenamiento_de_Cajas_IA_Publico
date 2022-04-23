import Arbol_Guillotina , Arbol_Posicionamiento_Cajas
import Cajas as Cajas_py
import random

class GA_Arbol_Guillotina():
	def __init__( self , contenedor , cant_individuos , altura_arboles , cajas_a_ordenar ):
		self.contenedor = contenedor
		self.cant_individuos = cant_individuos
		self.altura_arboles = altura_arboles
		self.poblacion = []
		self.cajas_a_ordenar = cajas_a_ordenar

	def algoritmo_genetico( self , cant_iteraciones ):
		
		self.definimos_poblacion_inicial()	#DEFINIMOS UNA POBLACION ALEATORIAMENTE	
		
		for ciclo in range( cant_iteraciones ):
			'''
			print( "1er Desempenio: " , self.poblacion[0].area_sin_uso )
			print( "1do Desempenio: " , self.poblacion[1].area_sin_uso )
			print( "3ro Desempenio: " , self.poblacion[2].area_sin_uso )
			print( "4to Desempenio: " , self.poblacion[3].area_sin_uso )
			print("~~~~~~~~~~~~>>>>>>>>>>>>>>")
			'''
			lista_individuos = self.poblacion.copy()
			#generamos una pareja

			while len(lista_individuos) != 0 and len(lista_individuos) != 1 and len(lista_individuos) != 2:  
				pareja = []
				while len(pareja) != 2:
										
					indiv_1 = lista_individuos.pop( random.randrange( 0 , len( lista_individuos ) ) )
					indiv_2 = lista_individuos.pop( random.randrange( 0 , len( lista_individuos ) ) )
					
					indiv_mejor_desemp = self.Competencia_entre_individuos( indiv_1 , indiv_2 )
					pareja.append( indiv_mejor_desemp )

					if indiv_mejor_desemp == indiv_1:
						lista_individuos.append( indiv_2 )
					else:
						lista_individuos.append( indiv_1 )

				pos_corte = random.randrange( 1 , len( self.poblacion[0].all_nodos_intermedios() )-1 ) #Desde el segundo nodo a penultimo nodo
				( indv_nuevo1 , indv_nuevo2 ) = self.Cruzamiento( pareja[0] , pareja[1] , pos_corte )
				
				#indv_nuevo1.genera_grafica_rectangular_arbol()
				#indv_nuevo2.genera_grafica_rectangular_arbol()

				self.calcular_desempenio_individuo( indv_nuevo1 ) #Calculamos el desempenio de los nuevos individuos
				self.calcular_desempenio_individuo( indv_nuevo2 ) #Calculamos el desempenio de los nuevos individuos

				self.poblacion.append( indv_nuevo1 ) #Introducimos los individuos a la poblacion
				self.ordenamos_poblacion_por_mejor_desempenio()
				self.poblacion.pop( len( self.poblacion )-1 )

				self.poblacion.append( indv_nuevo2 ) #Introducimos los individuos a la poblacion
				self.ordenamos_poblacion_por_mejor_desempenio()
				self.poblacion.pop( len( self.poblacion )-1 ) #Quitamos de la poblacion el peor desempenios

 
	def definimos_poblacion_inicial( self ):

		for individuo in range( self.cant_individuos ):
			Arbol = Arbol_Guillotina.Arbol_de_CorteGuillotina( self.altura_arboles , self.contenedor , self.cajas_a_ordenar ) #Definimos el objeto hoja

			corte = Arbol.corte_aleatorio_vertical_o_horizontal() #Retorna el tipo corte (vertical=V , horizontal=H)
			Arbol.raiz = Arbol_Guillotina.Node_CorteGuillotina( self.contenedor , corte , random.random() , None ) #Generamos un Nodo para la raiz

			Arbol.Arma_arbolGuillotina_aleatoriamente( Arbol.raiz , Arbol.altura ) #Armamos el arbol guillotina con valores aleatorios

			self.calcular_desempenio_individuo( Arbol ) #Calculamos el desempenio del arbol generado
			self.poblacion.append( Arbol ) #ingresamos arbol a la poblacion

	def ordenamos_poblacion_por_mejor_desempenio( self ):
		self.poblacion.sort( key=lambda individuo: individuo.area_sin_uso )		
		return self.poblacion

	def calcular_desempenio_individuo( self , Arbol ):
		Arbol.calculando_desempenio()
		return (Arbol.area_sin_uso) 

	def Cruzamiento( self , individuo1 , individuo2 , pos_corte ):
		#Cruzamiento entre 2 individuos para generar 2 nuevos individuos
		lista_individuo_1 = individuo1.all_nodos_intermedios()
		lista_individuo_2 = individuo2.all_nodos_intermedios()

		#Definimos los 2 nuevos individuos
		arbol_nuevo_1 = Arbol_Guillotina.Arbol_de_CorteGuillotina( self.altura_arboles , self.contenedor , self.cajas_a_ordenar )
		corte = arbol_nuevo_1.corte_aleatorio_vertical_o_horizontal()
		arbol_nuevo_1.raiz = Arbol_Guillotina.Node_CorteGuillotina( self.contenedor , corte , random.random() , None )
		arbol_nuevo_1.Arma_arbolGuillotina_aleatoriamente( arbol_nuevo_1.raiz , self.altura_arboles )

		arbol_nuevo_2 = Arbol_Guillotina.Arbol_de_CorteGuillotina( self.altura_arboles , self.contenedor , self.cajas_a_ordenar )
		corte = arbol_nuevo_2.corte_aleatorio_vertical_o_horizontal()
		arbol_nuevo_2.raiz = Arbol_Guillotina.Node_CorteGuillotina( self.contenedor , corte , random.random() , None )
		arbol_nuevo_2.Arma_arbolGuillotina_aleatoriamente( arbol_nuevo_2.raiz , self.altura_arboles )
		
		#Obtenemos la representacion en forma de lista de los nuevos individuos para poder modificarlos
		lista_arbol_nuevo_1 = arbol_nuevo_1.all_nodos_intermedios()
		lista_arbol_nuevo_2 = arbol_nuevo_2.all_nodos_intermedios()
		
		for pos in range( pos_corte ):
			lista_arbol_nuevo_1[pos].corte = lista_individuo_1[pos].corte
			lista_arbol_nuevo_1[pos].Porcentaje_de_Corte = lista_individuo_1[pos].Porcentaje_de_Corte

			lista_arbol_nuevo_2[pos].corte = lista_individuo_2[pos].corte
			lista_arbol_nuevo_2[pos].Porcentaje_de_Corte = lista_individuo_2[pos].Porcentaje_de_Corte

		for pos in range( pos_corte , len( lista_arbol_nuevo_2 ) ):
			lista_arbol_nuevo_1[pos].corte = lista_individuo_2[pos].corte
			lista_arbol_nuevo_1[pos].Porcentaje_de_Corte = lista_individuo_2[pos].Porcentaje_de_Corte

			lista_arbol_nuevo_2[pos].corte = lista_individuo_1[pos].corte
			lista_arbol_nuevo_2[pos].Porcentaje_de_Corte = lista_individuo_1[pos].Porcentaje_de_Corte

		arbol_nuevo_1.actualiza_valor_hoja( arbol_nuevo_1.raiz , self.altura_arboles ) #Actualizamos los valores de los subcontenedores, hojas
		arbol_nuevo_2.actualiza_valor_hoja( arbol_nuevo_2.raiz , self.altura_arboles ) #Actualizamos los valores de los subcontenedores, hojas

		return ( arbol_nuevo_1 , arbol_nuevo_2 )

	def Competencia_entre_individuos( self , individuo1 , individuo2 ):
		#Compiten entre 2 individuos para definir cual tiene mejor desempenio
		if individuo1.area_sin_uso < individuo2.area_sin_uso:
			return individuo1
		return individuo2

	def Crecimiento( self , individuo1 , individuo2 ):
		#Se les dara un tiempo de crecimiento a cada celula para poder mejorarse antes del torneo y eliminacion
		pass

	def individuo_peor_desempenio( self ):
		#Retorna la celula con peor desempenio de todas para competir realizar torneo contra la nueva generada
		return self.poblacion[ len(self.poblacion)-1 ]		


# ------------------->>>
# -- Configuracion -->>>

admin_caja = Cajas_py.Administrador_Cajas()
'''
Contenedor = admin_caja.retorna_tam_contenedor( 'cajas_102_aleatorio.json' ) 
ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( 'cajas_102_aleatorio.json' )

Contenedor = admin_caja.retorna_tam_contenedor( 'cajas_22_aleatorio.json' ) 
ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( 'cajas_22_aleatorio.json' )
'''
'''
Contenedor = admin_caja.retorna_tam_contenedor( 'cajas_22_aleatorio_0.json' ) 
ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( 'cajas_22_aleatorio_0.json' )

Cant_Individuos = 150
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.
# ------------------->>>
# ------------------->>>

GA = GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
GA.algoritmo_genetico( Cant_Ciclos )
print( GA.poblacion[0].area_sin_uso )

GA.poblacion[0].genera_grafica_rectangular_arbol()
#GA.poblacion[0].VerArbol_CorteGuillotina()
'''
'''
import statistics
import numpy
lista_resultados22 = []
for x in range(30):
	caso_actual = f'Ecenarios_de_Prueba/22_Cajas/cajas_22_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	Cant_Individuos = 150
	Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
	Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.
	# ------------------->>>
	# ------------------->>>

	GA = GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )
	print( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1]) )
	
	lista_resultados22.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )
	
	#GA.poblacion[0].genera_grafica_rectangular_arbol()
print("Media 22 :", statistics.mean( lista_resultados22 ))

lista_resultados101 = []
for x in range(30):
	caso_actual = f'Ecenarios_de_Prueba/101_Cajas/cajas_101_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	Cant_Individuos = 150
	Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
	Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.
	# ------------------->>>
	# ------------------->>>

	GA = GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )
	print( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1]) )
	
	lista_resultados101.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )
	
	#GA.poblacion[0].genera_grafica_rectangular_arbol()
print("Media 101:", statistics.mean( lista_resultados101 ))

lista_resultados200 = []
for x in range(30):
	caso_actual = f'Ecenarios_de_Prueba/200_Cajas/cajas_200_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	Cant_Individuos = 150
	Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
	Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.
	# ------------------->>>
	# ------------------->>>

	GA = GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )
	print( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1]) )
	
	lista_resultados200.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )
	
	#GA.poblacion[0].genera_grafica_rectangular_arbol()
print("Media 200:", statistics.mean( lista_resultados200 ))
'''
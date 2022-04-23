import Modulo_individuo_PSO , Arbol_Guillotina as Modulo_Arbol_Guillotina
import random
class Algoritmo_Cumulo_de_Particulas():
	def __init__(self,contenedor,cant_individuos,altura_arboles,cajas_a_ordenar):
		self.contenedor = contenedor
		self.cant_individuos = cant_individuos
		self.altura_arboles = altura_arboles
		self.cajas_a_ordenar = cajas_a_ordenar
		
		self.poblacion = []

		self.mejor_individuo = None

	def algoritmo_pso(self , ciclos , arbol_genetico ):
		#Ingresando individuos a la poblacion
		
		self.definimos_poblacion_inicial()
		
		lista_individuo_ag = arbol_genetico.all_nodos_intermedios()
		bandera = True
		for individuo_pso in self.poblacion:
			list_individuo_pso = individuo_pso.all_nodos_intermedios() 	
			for pos in range( len( lista_individuo_ag ) ):
				list_individuo_pso[pos].corte = lista_individuo_ag[pos].corte
				if bandera:
					list_individuo_pso[pos].Porcentaje_de_Corte = lista_individuo_ag[pos].Porcentaje_de_Corte	
					list_individuo_pso[pos].dimencionCaja = lista_individuo_ag[pos].dimencionCaja
			individuo_pso.actualiza_valor_hoja( individuo_pso.raiz , self.altura_arboles ) #Actualizamos los valores de los subcontenedores, hojas 
			individuo_pso.calculando_desempenio()
			bandera = False

		self.ordenamos_poblacion_por_mejor_desempenio()

		mejor_individuo = self.define_mejor_individuo_poblacion() #Definimos el mejor individuo de la poblacion

		#print( "Inicio: ",mejor_individuo.area_sin_uso )

		for ciclo in range( ciclos ):

			for individuo in self.poblacion:
				if individuo != self.mejor_individuo: #Realizamos el calculo menos para el mejor individuo
					#print( "Individuo: ",individuo.area_sin_uso )

					vector_vel_siguiente = self.calculo_vector_velocidad( individuo )
					
					sig_posicion = self.calculo_vector_posicion( individuo , vector_vel_siguiente )

					individuo.actualizando_nueva_posicion_individuo( sig_posicion )

					individuo.actulizando_mejor_pos_historica_y_desempenio_y_velocidad( vector_vel_siguiente )

			self.ordenamos_poblacion_por_mejor_desempenio()

			mejor_individuo = self.define_mejor_individuo_poblacion() #Definimos el mejor individuo de la poblacion 

	def ordenamos_poblacion_por_mejor_desempenio( self ):
		self.poblacion.sort( key=lambda individuo: individuo.area_sin_uso )		
		return self.poblacion

	def definimos_poblacion_inicial( self ):
		for cont_individuo in range( self.cant_individuos ):
			
			peso = 1
			aceleracion_1 = 1
			aceleracion_2 = 1
			random_1 = random.random()
			random_2 = random.random()

			individuo = Modulo_individuo_PSO.individuo_pso( self.contenedor 
				, self.altura_arboles , self.cajas_a_ordenar
				, peso , aceleracion_1 , aceleracion_2 , random_1 , random_2 )
			
			corte = individuo.corte_aleatorio_vertical_o_horizontal()
			individuo.raiz = Modulo_Arbol_Guillotina.Node_CorteGuillotina( self.contenedor , corte , random.random() , None )
			individuo.Arma_arbolGuillotina_aleatoriamente( individuo.raiz , self.altura_arboles )
			
			individuo.calculando_desempenio()
			individuo.define_vector_velocidad_aleatorio()

			individuo.mejor_posicion_historica = individuo.retorna_vector_posicion_actual() #la mejor posicion es la unica, la actual 
			individuo.mejor_desempenio = individuo.area_sin_uso #el mejor desempenio es la unica, la actual

			self.poblacion.append( individuo ) #Ingresamos individuo a la poblacion

			#------------------------------>>>>>

	def define_mejor_individuo_poblacion( self ): #Se define al mejor individuo
		self.mejor_individuo = self.poblacion[0] #Definimos al mejor individuo
		return self.mejor_individuo

	def calculo_vector_velocidad( self , individuo ):
		
		# V(t+1) = w*Veloc
		vector_velocidad_sig = self.multiplicacion_a_vector( individuo.peso , individuo.vector_velocidad )
		#==============>>
		#print("@: ",vector_velocidad_sig)
		#V(t+1) = V(t+1) + C1 * R1 * (Glob_BEAST - P(t))
		C1_R1 = individuo.aceleracion_1 * individuo.random_1
		
		vecPos_mejor_individuo_poblacion = self.mejor_individuo.retorna_vector_posicion_actual()
		vecPos_individuo_neg = individuo.retorna_negativo_de_vector( individuo.retorna_vector_posicion_actual() )
		vec_Gbeast = self.suma_entre_vectores( vecPos_mejor_individuo_poblacion , vecPos_individuo_neg )
		segundo_termino = self.multiplicacion_a_vector( C1_R1 , vec_Gbeast )
		
		vector_velocidad_sig = self.suma_entre_vectores( vector_velocidad_sig , segundo_termino )
		#=============>>
		#print("@@: ",vector_velocidad_sig)

		#V(t+1) = V(t+1) + C2 * R2 * (Hist_BEAST - P(t))
		C2_R2 = individuo.aceleracion_2 * individuo.random_2

		vecPos_mejor_Pos_Historica = individuo.mejor_posicion_historica
		vecPos_individuo_neg = individuo.retorna_negativo_de_vector( individuo.retorna_vector_posicion_actual() )
		vec_Hbeast = self.suma_entre_vectores( vecPos_mejor_Pos_Historica , vecPos_individuo_neg )
		tercera_porcion = self.multiplicacion_a_vector( C2_R2 , vec_Hbeast )

		vector_velocidad_sig = self.suma_entre_vectores( vector_velocidad_sig , tercera_porcion )
		#=============>>
		#print("@@@: ",vector_velocidad_sig)
		return vector_velocidad_sig

	def calculo_vector_posicion( self , individuo , vector_velocidad ):
		calculoPosCorte = self.suma_entre_vectores( individuo.retorna_vector_posicion_actual() , vector_velocidad )
		for pos in range( len( individuo.retorna_vector_posicion_actual() ) ):
			if calculoPosCorte[pos] > 1:
				calculoPosCorte[pos] = 1
			elif calculoPosCorte[pos] < 0:
				calculoPosCorte[pos] = 0
		return calculoPosCorte

	def suma_entre_vectores( self , vector1 , vector2 ):
		#vector1 menos vector2
		vector_resultado = []
		for pos in range( len(vector1) ):
			vector_resultado.append( vector1[pos] + vector2[pos] )
		return vector_resultado

	def multiplicacion_a_vector( self , multiplicador , vector ):
		return [ (multiplicador*casilla) for casilla in vector ]

'''
import Geneticos as Geneticos_Module , Cajas as Cajas_Module
# ------------------->>>
# -- Configuracion -->>>

admin_caja = Cajas_Module.Administrador_Cajas()

#Contenedor = admin_caja.retorna_tam_contenedor( 'cajas_102_aleatorio.json' ) 
#ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( 'cajas_102_aleatorio.json' )

#Contenedor = admin_caja.retorna_tam_contenedor( 'cajas_22_aleatorio.json' ) 
#ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( 'cajas_22_aleatorio.json' )

Contenedor = admin_caja.retorna_tam_contenedor( 'Ecenarios_de_Prueba/186_Cajas/cajas_186_aleatorio_20.json' ) 
ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( 'Ecenarios_de_Prueba/186_Cajas/cajas_186_aleatorio_20.json' )

Cant_Individuos = 100
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 1 #Cuantas generaciones se generaran antes de parar.
# ------------------->>>
# ------------------->>>

ListaCajas = [ (2,2) , (2,2) , (2,2) , (2,2) , (1,1),(1,1),(1,1),(1,1) ]
Contenedor = (5,4)

GA = Geneticos_Module.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
GA.algoritmo_genetico( Cant_Ciclos )

print("Mejor AG: " , GA.poblacion[0].area_sin_uso )

for x in range(1):
	#Indv = 800 mejora en 22 cajas
	PSO_ = Algoritmo_Cumulo_de_Particulas( Contenedor , 50 , Altura_Arboles , ListaCajas )
	PSO_.algoritmo_pso( 50 , GA.poblacion[0] )

	print( "Mejor PSO: ",PSO_.poblacion[0].area_sin_uso )
	PSO_.poblacion[0].genera_grafica_rectangular_arbol()
'''
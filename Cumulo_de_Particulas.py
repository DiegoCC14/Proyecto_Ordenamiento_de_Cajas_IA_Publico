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

	def algoritmo_pso(self , ciclos ):
		#Ingresando individuos a la poblacion
		
		for cont_individuo in range( self.cant_individuos ):
			
			peso = 0.5
			aceleracion_1 = 0.7
			aceleracion_2 = 0.7
			random_1 = 0.9
			random_2 = 0.9

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
		
		self.ordenamos_poblacion_por_mejor_desempenio()

		mejor_individuo = self.define_mejor_individuo_poblacion() #Definimos el mejor individuo de la poblacion
		
		#print( "@@",mejor_individuo.area_sin_uso )

		for ciclo in range( ciclos ):

			for individuo in self.poblacion:
				
				if individuo != self.mejor_individuo: #Realizamos el calculo menos para el mejor individuo

					vector_vel_siguiente = self.calculo_vector_velocidad( individuo )
					
					#print( "velocidad: ",vector_vel_siguiente )
					
					sig_posicion = self.calculo_vector_posicion( individuo , vector_vel_siguiente )

					#print( "posicion: ",sig_posicion )

					individuo.actualizando_nueva_posicion_individuo( sig_posicion )

					individuo.actulizando_mejor_pos_historica_y_desempenio_y_velocidad( vector_vel_siguiente )

			self.ordenamos_poblacion_por_mejor_desempenio()

			mejor_individuo = self.define_mejor_individuo_poblacion() #Definimos el mejor individuo de la poblacion 

		

	def ordenamos_poblacion_por_mejor_desempenio( self ):
		self.poblacion.sort( key=lambda individuo: individuo.area_sin_uso )		
		return self.poblacion

	def definimos_poblacion_inicial( self ):
		pass

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


# ------------------->>>
# -- Configuracion -->>>
Contenedor = (10,9) #20

ListaCajas = [ (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) ]
ListaCajas += [ (2,2) , (2,2) , (2,2) , (2,2) , (2,2) ]*4 #-> 20*4 = 80 area

Cant_Individuos = 200
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 40 #Cuantas generaciones se generaran antes de parar.
# ------------------->>>
# ------------------->>>

PSO_ = Algoritmo_Cumulo_de_Particulas( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas )
PSO_.algoritmo_pso( Cant_Ciclos )
print( PSO_.poblacion[0].area_sin_uso )
#PSO_.poblacion[0].VerArbol_CorteGuillotina()

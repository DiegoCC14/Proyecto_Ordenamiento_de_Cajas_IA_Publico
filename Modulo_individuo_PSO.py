import Arbol_Guillotina as Modulo_Arbol_Guillotina
import random

class individuo_pso( Modulo_Arbol_Guillotina.Arbol_de_CorteGuillotina ):
	def __init__( self , contenedor , altura_arboles , cajas_a_ordenar , 
		peso , aceleracion_1 , aceleracion_2 , random_1 , random_2 ):
		Modulo_Arbol_Guillotina.Arbol_de_CorteGuillotina.__init__(self, altura_arboles , contenedor , cajas_a_ordenar)
		self.peso = peso
		self.aceleracion_1 = aceleracion_1
		self.aceleracion_2 = aceleracion_2
		self.random_1 = random_1
		self.random_2 = random_2

		self.mejor_posicion_historica = None
		self.mejor_desempenio = None

		self.vector_velocidad = []

	def define_vector_velocidad_aleatorio( self ):
		cant_nodos_intermedios = len( self.all_nodos_intermedios() )
		for pos in range( cant_nodos_intermedios ):
			self.vector_velocidad.append( random.randint(1,99)/100 )

	def retorna_vector_posicion_actual( self ):
		return [ nodo.Porcentaje_de_Corte for nodo in self.all_nodos_intermedios() ]

	def retorna_negativo_de_vector( self , vector ):
		return [ (-1)*casilla for casilla in vector ]

	def actualizando_nueva_posicion_individuo( self , nueva_posicion_actual ):
		list_posicion_actual = self.all_nodos_intermedios()
		for pos in range( len( list_posicion_actual ) ):
			list_posicion_actual[pos].Porcentaje_de_Corte = nueva_posicion_actual[pos]
		
		self.actualiza_valor_hoja( self.raiz , self.altura ) #actualizamos los valores de las hojas
		self.calculando_desempenio()
		
	def actulizando_mejor_pos_historica_y_desempenio_y_velocidad( self , vec_velocidad ):
		self.vector_velocidad = vec_velocidad
		if self.mejor_desempenio > self.area_sin_uso:
			self.mejor_desempenio = self.area_sin_uso
			self.mejor_posicion_historica = self.retorna_vector_posicion_actual()

if "__main__" == __name__:
	
	# ------------------->>>
	# -- Configuracion -->>>
	Contenedor = (10,9) #20

	ListaCajas = [ (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) , (1,1) ]
	ListaCajas += [ (2,2) , (2,2) , (2,2) , (2,2) , (2,2) ]*4 #-> 20*4 = 80 area

	Cant_Individuos = 500
	Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
	Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.
	# ------------------->>>
	# ------------------->>>

	'''
	peso = 1
	aceleracion_1 = 1
	aceleracion_2 = 1 
	random_1 = 1 
	random_2 = 1

	individuo = individuo_pso( Contenedor
		, Altura_Arboles , ListaCajas
		, peso , aceleracion_1 , aceleracion_2 , random_1 , random_2 )

	corte = individuo.corte_aleatorio_vertical_o_horizontal()
	individuo.raiz = Modulo_Arbol_Guillotina.Node_CorteGuillotina( Contenedor , corte , random.random() , None )

	individuo.Arma_arbolGuillotina_aleatoriamente( individuo.raiz , individuo.altura )

	print( individuo.retorna_vector_posicion_actual() )
	individuo.actualizando_nueva_posicion_individuo([0.5 , 0.5 , 0.5 , 0.5 , 0.5 , 0.5 , 0.5 ])
	print( individuo.retorna_vector_posicion_actual() )
	'''


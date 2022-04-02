import Arbol_Guillotina , Arbol_Posicionamiento_Cajas

import random

def Celulas_Arbol_Guillotina():
	def __init__( self ):
		pass

	def Torneo_Eliminacion( self ):
		pass

	def Cruzamiento( self , celula1 , celula2 ):
		#Cruzamiento entre 2 celulas para generar 2 nuevas celulas
		pass

	def Competencia_entre_Celulas( self , celula1 , celula2 ):
		#Compiten entre 2 celulas para definir cual tiene mejor desempenio
		pass

	def Crecimiento( self , celula1 , celula2 ):
		#Se les dara un tiempo de crecimiento a cada celula para poder mejorarse antes del torneo y eliminacion
		pass

	def get_celula_peor_desempenio( self ):
		#Retorna la celula con peor desempenio de todas para competir realizar torneo contra la nueva generada
		pass


# ------------------->>>
# -- Configuracion -->>>
Contenedor = (5,4)
ListaCajas = [ (2,2) , (2,2) , (2,2) , (2,1) , (2,1) , (2,1) , (1,1) ]
Cant_Celulas = 128
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 100 #Cuantas generaciones se generaran antes de parar.
# ------------------->>>
# ------------------->>>

lista_celulas = []
for celula in range(Cant_Celulas):

	Arbol = Arbol_Guillotina.Arbol_de_CorteGuillotina( Altura_Arboles ) #Definimos el objeto hoja
	corte = Arbol.corte_aleatorio_vertical_o_horizontal() #Retorna el tipo corte (vertical=V , horizontal=H)
	
	Arbol.raiz = Arbol_Guillotina.Node_CorteGuillotina( Contenedor , corte , random.random() , None ) #Generamos un Nodo para la raiz

	Arbol.Arma_arbolGuillotina_aleatoriamente( Arbol.raiz , Arbol.altura ) #Armamos el arbol guillotina con valores aleatorios

	lista_celulas.append( Arbol )


'''
for celula in lista_celulas:
	print(celula.VerArbol_CorteGuillotina())
'''

#Lista = ArbolGuillotina.representacion_en_forma_de_lista( ArbolGuillotina.raiz , [] , 0 )

#ArbolGuillotina.VerArbol_CorteGuillotina()






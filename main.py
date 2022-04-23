import Geneticos as Geneticos_py , Cajas as Cajas_py , Cumulo_de_Particulas as PSO_py
import matplotlib.pyplot as plt

Cant_Individuos = 125
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.

admin_caja = Cajas_py.Administrador_Cajas()


AG_lista_resultados30 = []
AG_PSO_lista_resultados30 = []

AG_lista_resultados100 = []
AG_PSO_lista_resultados100 = []

AG_lista_resultados186 = []
AG_PSO_lista_resultados186 = []

for x in range(30):
	
	print('Iteracion: ',x)

	caso_actual = f'Ecenarios_de_Prueba/30_Cajas/cajas_30_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )

	AG_lista_resultados30.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )
	

	PSO_ = PSO_py.Algoritmo_Cumulo_de_Particulas( Contenedor , 50 , Altura_Arboles , ListaCajas )
	PSO_.algoritmo_pso( 50 , GA.poblacion[0] )

	AG_PSO_lista_resultados30.append( (PSO_.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )

	
	# 100 ------------->>>
	caso_actual = f'Ecenarios_de_Prueba/100_Cajas/cajas_100_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )

	AG_lista_resultados100.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )

	PSO_ = PSO_py.Algoritmo_Cumulo_de_Particulas( Contenedor , 50 , Altura_Arboles , ListaCajas )
	PSO_.algoritmo_pso( 50 , GA.poblacion[0] )

	AG_PSO_lista_resultados100.append( (PSO_.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )


	# 186 -------------------->>>
	caso_actual = f'Ecenarios_de_Prueba/186_Cajas/cajas_186_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )

	AG_lista_resultados186.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )

	PSO_ = PSO_py.Algoritmo_Cumulo_de_Particulas( Contenedor , 50 , Altura_Arboles , ListaCajas )
	PSO_.algoritmo_pso( 50 , GA.poblacion[0] )

	AG_PSO_lista_resultados186.append( (PSO_.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )



lista_result = [ AG_lista_resultados30 , AG_PSO_lista_resultados30 , AG_lista_resultados100 , AG_PSO_lista_resultados100 , AG_lista_resultados186 , AG_PSO_lista_resultados186 ]
plt.boxplot( lista_result )

plt.ylabel('Porcentaje de area sin uso')
values = ['AG-30', 'AG+PSO-30', 'AG-100' , 'AG+PSO-100' , 'AG-186' , 'AG+PSO-186'] 
plt.xticks( [1,2,3,4,5,6] , values )
plt.show()


#import Geneticos as Geneticos_Module , Cajas as Cajas_Module
# ------------------->>>
# -- Configuracion -->>>

Cant_Individuos = 150
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 25 #Cuantas generaciones se generaran antes de parar.
# ------------------->>>
# ------------------->>>
'''
GA = Geneticos_Module.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
GA.algoritmo_genetico( Cant_Ciclos )

print("Mejor AG: " , GA.poblacion[0].area_sin_uso )

for x in range(1):
	#Indv = 800 mejora en 22 cajas
	PSO_ = Algoritmo_Cumulo_de_Particulas( Contenedor , 50 , Altura_Arboles , ListaCajas )
	PSO_.algoritmo_pso( Cant_Ciclos , GA.poblacion[0] )

	print( "Mejor PSO: ",PSO_.poblacion[0].area_sin_uso )
	PSO_.poblacion[0].genera_grafica_rectangular_arbol()
'''















'''
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

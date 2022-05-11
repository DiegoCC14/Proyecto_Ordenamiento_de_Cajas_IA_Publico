import Geneticos as Geneticos_py , Cajas as Cajas_py , Cumulo_de_Particulas as PSO_py , Arbol_Guillotina as Arbol_Guillotina_py
import matplotlib.pyplot as plt
import random , time

Cant_Individuos = 125
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.

admin_caja = Cajas_py.Administrador_Cajas()

AG_lista_resultados_Cont50 = []
AG_lista_resultados_Cont100 = []
AG_lista_resultados_Cont250 = []

AG_lista_tiempo_Cont50 = []
AG_lista_tiempo_Cont100 = []
AG_lista_tiempo_Cont250 = []

'''
for x in range(30):
	
	print('Iteracion: ',x)

	#---------------->>>
	caso_actual = f'Ecenarios_de_Prueba/Contenedor_50_50_cajas_aleatorio/contendor_50_50_aleatorio_{1}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )

	AG_lista_resultados_Cont50.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )
	#---------------->>>

	#---------------->>>
	caso_actual = f'Ecenarios_de_Prueba/Contenedor_100_100_cajas_aleatorio/contendor_100_100_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )

	AG_lista_resultados_Cont100.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )
	#---------------->>>

	#---------------->>>
	caso_actual = f'Ecenarios_de_Prueba/Contenedor_250_250_cajas_aleatorio/contendor_250_250_aleatorio_{x}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )

	GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
	GA.algoritmo_genetico( Cant_Ciclos )

	AG_lista_resultados_Cont250.append( (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ) )
	#---------------->>>
	
lista_result = [ AG_lista_resultados_Cont50 , AG_lista_resultados_Cont100 , AG_lista_resultados_Cont250 ]

plt.boxplot( lista_result )

plt.ylabel('Porcentaje de Espacio sin uso')
values = ['AG-Cont_50_50', 'AG-Cont_100_100' , 'AG-Cont_250_250'] 
plt.xticks( [1,2,3] , values )
plt.show()
'''
'''
for estructura in Clasificador.keys():
	print( estructura, ' : ' , Clasificador[estructura] )
'''

'''
import numpy as np
import matplotlib.pyplot as plt
plt.ylabel('Area sin uso')
plt.xlabel('Ciclos')

x = [ x for x in range(1,Cant_Ciclos+1)]
plt.plot( x , evolucion_geneticos )
plt.show()
'''
caso50 = f'Ecenarios_de_Prueba/Contenedor_50_50_cajas_aleatorio/contendor_50_50_aleatorio_{19}.json'
Contenedor = admin_caja.retorna_tam_contenedor( caso50 ) 
ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso50 )


AG_lista_resultados_Cont50 = []
AG_lista_resultados_Cont100 = []
AG_lista_resultados_Cont250 = []

Cant_Ciclos = 0
for index in range(30):
	
	print('Iteracion: ',index)

	#---------------->>>
	caso_actual = f'Ecenarios_de_Prueba/Contenedor_50_50_cajas_aleatorio/contendor_50_50_aleatorio_{index}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )
	menor_area_sin_uso = 100
	for x in range(50):
		GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
		GA.algoritmo_genetico( Cant_Ciclos )
		if menor_area_sin_uso > (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ):
			menor_area_sin_uso = (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] )
	AG_lista_resultados_Cont50.append( menor_area_sin_uso )
	#---------------->>>

	#---------------->>>
	caso_actual = f'Ecenarios_de_Prueba/Contenedor_100_100_cajas_aleatorio/contendor_100_100_aleatorio_{index}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )
	menor_area_sin_uso = 100
	for x in range(50):
		GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
		GA.algoritmo_genetico( Cant_Ciclos )
		if menor_area_sin_uso > (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ):
			menor_area_sin_uso = (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] )
	AG_lista_resultados_Cont100.append( menor_area_sin_uso )
	#---------------->>>

	#---------------->>>
	caso_actual = f'Ecenarios_de_Prueba/Contenedor_250_250_cajas_aleatorio/contendor_250_250_aleatorio_{index}.json'
	Contenedor = admin_caja.retorna_tam_contenedor( caso_actual ) 
	ListaCajas = admin_caja.retorna_lista_unica_cajas_txt( caso_actual )
	menor_area_sin_uso = 100
	for x in range(50):
		GA = Geneticos_py.GA_Arbol_Guillotina( Contenedor , Cant_Individuos , Altura_Arboles , ListaCajas)
		GA.algoritmo_genetico( Cant_Ciclos )
		if menor_area_sin_uso > (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] ):
			menor_area_sin_uso = (GA.poblacion[0].area_sin_uso * 100)/(Contenedor[0]*Contenedor[1] )
	AG_lista_resultados_Cont250.append( menor_area_sin_uso )
	#---------------->>>
	
lista_result = [ AG_lista_resultados_Cont50 , AG_lista_resultados_Cont100 , AG_lista_resultados_Cont250 ]

plt.boxplot( lista_result )

plt.ylabel('Porcentaje de Espacio sin uso')
plt.title("Busqueda de Arbol Guillotina Random")
values = ['Random-Cont_50_50', 'Random-Cont_100_100' , 'Random-Cont_250_250'] 
plt.xticks( [1,2,3] , values )
plt.show()

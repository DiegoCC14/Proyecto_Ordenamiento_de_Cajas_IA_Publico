import Geneticos as Geneticos_py , Cajas as Cajas_py , Cumulo_de_Particulas as PSO_py
import matplotlib.pyplot as plt

Cant_Individuos = 125
Altura_Arboles = 3 #La altura es igual a la cantidad de vertices entre la raiz y un nodo hoja
Cant_Ciclos = 50 #Cuantas generaciones se generaran antes de parar.

admin_caja = Cajas_py.Administrador_Cajas()

AG_lista_resultados_Cont50 = []
AG_lista_resultados_Cont100 = []
AG_lista_resultados_Cont250 = []

for x in range(30):
	
	print('Iteracion: ',x)

	#---------------->>>
	caso_actual = f'Ecenarios_de_Prueba/Contenedor_50_50_cajas_aleatorio/contendor_50_50_aleatorio_{x}.json'
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

plt.ylabel('Porcentaje de area sin uso')
values = ['AG-50', 'AG-100' , 'AG-250' ] 
plt.xticks( [1,2,3] , values )
plt.show()

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10., 10., 0.2)
curva = [x**3-9*x for x in x]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.plot(x,curva)
plt.show()
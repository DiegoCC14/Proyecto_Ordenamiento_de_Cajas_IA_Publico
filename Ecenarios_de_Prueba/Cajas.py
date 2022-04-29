import random , json
class Administrador_Cajas():

	def genera_cajas( self , ancho_caja , cant_niveles ):
		#El ancho define la divicion por 2 que aremos, 100/2 -> 100/4 -> 100/6 -> 100/8 -> 100/10
			#esto sera el ancho de las cajas
		#Las iteraciones definen la cantidad de niveles de las cajas
			#Las por cada nivel definimos un numero entero aleatorio que sera la altura para todas las cajas
		
		lista_altura_nivel = [ random.randint(1, int(ancho_caja/2) ) * 2 for iteracion in range(cant_niveles) ] #Es multiplo de 2
		dicc_cajas =  { 'contenedor': (0,0) , "cant_cajas": 0 , 'niveles_cajas': [] }
		altura_contenedor = 0
		divicion = 2

		for altura in lista_altura_nivel: #Define un nivel
			
			altura_contenedor += altura
			
			divicion = random.randint( 2,10 ) 

			ancho = int( ancho_caja/divicion )
			list_nivel_caja = [ (ancho,altura) ] * divicion
			
			ancho_caja_faltante = ancho_caja - (ancho*divicion)
			if ancho_caja_faltante != 0:
				list_nivel_caja.append( (ancho_caja_faltante,altura) )
			
			dicc_cajas['niveles_cajas'].append( list_nivel_caja )
			dicc_cajas["cant_cajas"] += len( list_nivel_caja )
			

		dicc_cajas['contenedor'] = ( ancho_caja , altura_contenedor )
		return dicc_cajas

	def genera_cajas_aleatoriamente( self , contenedor_dim ):
		
		dicc_cajas =  { 'contenedor': contenedor_dim , "cant_cajas": 0 , 'niveles_cajas': [ [] ] }

		dimencion_cubierta = 0
		dimencion_total_contenedor = contenedor_dim[0] * contenedor_dim[1]
		lista_cajas = []
		while dimencion_cubierta < dimencion_total_contenedor: #Genera cajas aleatoriamente

			caja_ancho = random.randint( 1 , contenedor_dim[0]/5 ) 
			caja_alto = random.randint( 1 , contenedor_dim[1]/5 )
			if ( dimencion_cubierta+(caja_ancho*caja_alto) ) < dimencion_total_contenedor:
				lista_cajas
				dimencion_cubierta += caja_ancho*caja_alto
				dicc_cajas["cant_cajas"] += 1
				dicc_cajas['niveles_cajas'][0].append( (caja_ancho , caja_alto) ) #Un unico nivel aleatorio
			else:
				break

		dimencion_restante = dimencion_total_contenedor - dimencion_cubierta	
		while dimencion_restante > 0: #Genera cajas con altura 1, pero ancho aleatorio
			if dimencion_restante > contenedor_dim[0]/5:
				ancho_caja = random.randint( 1 , contenedor_dim[0]/5 )
				dicc_cajas['niveles_cajas'][0].append( ( ancho_caja , 1) ) #Un unico nivel aleatorio
			else:
				ancho_caja = dimencion_restante
				dicc_cajas['niveles_cajas'][0].append( ( dimencion_restante , 1) ) #Un unico nivel aleatorio
			dimencion_cubierta += ancho_caja
			dimencion_restante = dimencion_total_contenedor - dimencion_cubierta 
			dicc_cajas["cant_cajas"] += 1

		return dicc_cajas

	def retorna_cant_cajas( self , archivo_json ):
		with open( archivo_json , 'r' ) as file:
			data = json.load(file)
		return data['cant_cajas']
	
	def retorna_tam_contenedor( self , archivo_json ):
		with open( archivo_json , 'r' ) as file:
			data = json.load(file)
		return tuple( data['contenedor'] ) 

	def retorna_lista_unica_cajas_txt( self , archivo_json ):
		with open( archivo_json , 'r' ) as file:
			data = json.load(file)
		lista_all_cajas = []
		for nivel in data['niveles_cajas']:
			lista_all_cajas += [ tuple(caja) for caja in nivel ] 
		return lista_all_cajas

	def guardar_datos_caja_txt( self , dicc_datos , nombre_json ):
	
		with open( nombre_json , 'w') as file:
			json.dump( dicc_datos , file , indent=4)



#Configuracion --->>>
#----------------->>>
ancho = 44
niveles = 15
#----------------->>>
#----------------->>>

obj_admin = Administrador_Cajas()
for x in range(30):
	dicc_contenedor = obj_admin.genera_cajas_aleatoriamente( (250,250) )
	obj_admin.guardar_datos_caja_txt( dicc_contenedor , f'contendor_250_250_aleatorio_{x}.json' )
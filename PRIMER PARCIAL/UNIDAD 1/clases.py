import modulo
while True:
	print("""-------------BIENVENDIO AL MENU INTERACTIVO DE RASBERRY
              --------------------1) led bcm --------------------------
              --------------------2) led board------------------------
              --------------------3) led boton bcm ------------------
              --------------------4) led boton board ----------------
              --------------------4) SALIR -------------------------""")
		try: entrada=int(input("Ingrrse el numero del programa que desea"))

		except ValueError:
			print("Error debe de ingresar un numero valido")
			continue
		if entrada==1:
		modulo.led()
		elif entrada==2:
		print("Ejecutar programa 2 aqui")
		elif entrada==3:
		print("Ejecutar programa 3 aqui")
		elif entrada==4:
		print("Ejecutar programa 4 aqui")
		elif entrada==5:
		print("Saliendo del programa")
		break
		else:
		print("Error ingrese un numero valido")

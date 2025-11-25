from fun.py  import ejecutar_programa

def iniciar_interfaz():
	" funcion que maneja la entrada del usuario."
	print("Selector de programas de Raspberry pi")
	pro=input("Ingresar el programa que quiere ejecutar(A,B,C,D):".strip().upper())
	ejecutar_programa(pro)
	print(f"El programa con la opcion'{pro}' ha sido solicitado para ejecutarse.")

if __name__==" __main__":
	iniciar_interfaz()

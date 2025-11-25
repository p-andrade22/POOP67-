def fun(opcion):
	if opcion=="A":
		exec(open("led.py").read())
	elif opcion=="B":
		exec(open("led_board.py").read())
	elif opcion=="C":
		exec(open("led_boton.py").read())
	elif opcion=="D":
		exec(open("led_boton_board.py").read())
	else:
		print("Opcion no valida")
pro=input("Ingresar el programa que quiere ejecutar (A,B,C,D):").upper()
fun(pro) 

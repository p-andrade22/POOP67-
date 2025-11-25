print("MODULO PHYTON")
def led():
	import RPi.GPIO as GPIO 
	import time

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18,GPIO.OUT)
	try:
		while True:
			GPIO.output(18,True)
			time.sleep(1)
			GPIO.output(18,False)
			time(1)
		except keyboardInterrupt:
			GPIO.cleanup()
			print("Programa detenido manualmente")
		print("El programa encargado de prender y apagar led esta siendo ejecutado")


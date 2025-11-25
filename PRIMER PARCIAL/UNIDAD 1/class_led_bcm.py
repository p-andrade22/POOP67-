import RPi.GPIO as GPIO
import time

class led_bcm:
	def __init__(self,pin):
		self.pin=pin
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.OUT)
	def parpadear(self):
		print("El led esta encendido..... Precioce Control  C para detener el programa")
		while True:
			GPIO.output(self.pin,True)
			time.sleep(1)
			GPIO.output(self.pin, False)
			time.sleep(1)
		GPIO.cleanup
led=led_bcm(18)
led.parpadear()


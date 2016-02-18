#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("bubbling_water.mp3")

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
	time.sleep(0.2)
	#print("- -  pin %s is %s" % (sensor, GPIO.input(sensor)))
	previous_state = current_state
	current_state = GPIO.input(sensor)
    
	if current_state != previous_state:
		new_state = "HIGH" if current_state else "LOW"
		print("GPIO pin %s is %s" % (sensor, new_state))
        if current_state == 1 :
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue

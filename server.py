#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/cherrypy-an-elegant-python-webserver-for-raspberry-pi-remote-controls/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import random, string
from time import sleep

import cherrypy

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class RaspiServer(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="on">
              <input type="text" value="13" name="pin_str" />
              <button type="submit">ON</button>
            </form>
			<form method="get" action="off">
              <input type="text" value="13" name="pin_str" />
              <button type="submit">OFF</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def off(self, pin_str="13"):
        pin = int(pin_str)
        GPIO.setup(pin, GPIO.OUT)        
        GPIO.output(pin, GPIO.HIGH)

        return "Blinked on Pin " + str(pin)
		
		
    @cherrypy.expose
    def on(self, pin_str="13"):
        pin = int(pin_str)
        GPIO.setup(pin, GPIO.OUT)        
        GPIO.output(pin, GPIO.LOW)

        return "Blinked on Pin " + str(pin) 


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '192.168.1.200'})
    cherrypy.quickstart(RaspiServer())


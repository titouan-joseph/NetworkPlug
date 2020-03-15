#!/usr/bin/python3
# encoding:utf-8
# Tutorial: http://www.knight-of-pi.org/cherrypy-an-elegant-python-webserver-for-raspberry-pi-remote-controls/
# Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import cherrypy
import termcolor
import os

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


class RaspiServer(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="action">
              <input type="text" name="action" />
              <button type="submit">OK</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def action(self, action):
        if action == "eteint_3_ecran_bas":
            self.gpiooff([11, 12, 13])
            return "Off 11 12 13"
        elif action == "allume_3_ecran_bas":
            self.gpioon([11, 12, 13])
            return  "On 11 12 13"
        elif action == "eteint_3_ecran_haut":
            self.gpiooff([7, 8, 5])
            return "Off 7 8 5 "
        elif action == "allume_3_ecran_haut":
            self.gpioon([7, 8, 5])
            return "On 7 8 5 "
        elif action == "eteint_ecran":
            self.gpiooff([7, 8, 5, 11, 12, 13])
            return "Off 7 8 5 11 12 13"
        elif action == "allume_ecran":
            self.gpioon([7, 8, 5, 11, 12, 13])
            return "On 7 8 5 11 12 13"
        elif action == "eteint_vive":
            self.gpiooff([3])
            return "Off 3"
        elif action == "allume_vive":
            self.gpioon([3])
            return "On 3"
        elif action == "eteint_pc":
            self.gpiooff([10])
            return "Off 10"

        else:
            return "Error, action inconue"

    def gpioon(self, pins):
        for pin in pins:
            print(termcolor.colored(str(pin), 'green'))
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    @cherrypy.expose()
    def gpiooff(self, pins):
        for pin in pins:
            print(termcolor.colored(str(pin), 'red'))
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '192.168.1.200'})
    cherrypy.quickstart(RaspiServer())

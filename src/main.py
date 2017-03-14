#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple python application with two parts.

(1) Primera part, retorna la predicció per a les proximes 8

(2) l'usuari pot elegir entre les 3 funcions astronomy , conditions i
    hourly.

@author: marcelpv96@marcelpv96.com
'''
from client import WeatherClient
import optparse

api_Key = None
if __name__ == "__main__":
    parser = optparse.OptionParser()
    wc = WeatherClient(api_Key, "conditions", "Lleida")
    wc.main()

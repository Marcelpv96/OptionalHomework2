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
import sys

api_Key = None
if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('-s', '--service', action='store', default='hourly',
                      help='Quin servei vols? pots elegir\
                       entre hourly, astronomy i conditions')
    parser.add_option('-k', '--key', action='store', help='Api key')
    parser.add_option('-l', '--location', action='store', default='Balaguer',
                      help='Quina ciutat vols?')
    (options, args) = parser.parse_args()
    if options.key is None:
        print "com a minim tens de posar la key, -k <API KEY>"
        sys.exit(-1)
    wc = WeatherClient(options.key, options.service, options.location)
    wc.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple python application with two parts.

(1) Primera part, retorna la predicció per a les proximes 8

(2) Second part:


@author: marcelpv96@marcelpv96.com
'''
from client import WeatherClient

api_Key = None
if __name__ == "__main__":
    wc = WeatherClient(api_Key, "hourly", "Lleida")
    wc.main()

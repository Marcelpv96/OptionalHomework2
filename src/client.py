#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
import sys
import urllib2
import bs4
import json
import datetime
import requests


class WeatherClient (object):
    url_base = "http://api.wunderground.com/api/"
    url_services = {"almanac": "/almanac/q/CA/",
                    "hourly": "/hourly/q/CA/",
                    "astronomy": "/astronomy/q/CA/",
                    "conditions": "/conditions/q/CA/"}

    def __init__(self, api_Key, service, location):
        self.api_Key = api_Key
        self.service = service
        self.location = location

    def hourly(url):
        """
        (1) Predicció per les proximes 8 hores.
        """
        r = requests.get(url)
        jsondata = json.loads(r.text)
        currentTime = datetime.datetime.now().hour
        for i in xrange(8):
            print "La predicció per a les " \
                + str(currentTime + i) + 'h es de: '
            print jsondata["hourly_forecast"][i]["temp"]["metric"] + "C"

    def astronomy(url):
        r = requests.get(url)
        jsondata = json.loads(r.text)
        print "Moon in phase: " + jsondata["moon_phase"]["phaseofMoon"]
        print "percentIlluminated: " +\
            jsondata["moon_phase"]["percentIlluminated"]
        print "hemisphere: " + jsondata["moon_phase"]["hemisphere"]

    def conditions(url):
        r = requests.get(url)
        jsondata = json.loads(r.text)
        print "Latitud :" + \
            jsondata["current_observation"]["display_location"]["latitude"]
        print "Longitud :" + \
            jsondata["current_observation"]["display_location"]["longitude"]
        print "Elevacio :" + \
            jsondata["current_observation"]["display_location"]["elevation"] \
            + "m"

    def main(self, function=astronomy):
        try:
            WeatherClient.url_services[self.service]
        except KeyError:
            print "Invalid service"
            sys.exit(-1)

        url = WeatherClient.url_base + self.api_Key + \
            WeatherClient.url_services[
                self.service] + self.location + "." + "json"
        WeatherClient.services_func[self.service](url)

    # usuari podra elegir entre les 3 funcions
    services_func = {"hourly": hourly,
                     "astronomy": astronomy,
                     "conditions": conditions}

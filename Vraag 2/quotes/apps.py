# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
import json

import config


class QuotesConfig(AppConfig):
    name = 'quotes'

    # def ready(self):
    #     json_data = open('../../infractions.json')
    #     data1 = json.load(json_data)  # deserialises it
    #     data2 = json.dumps(data1)  # json formatted string

    #     json_data.close()

    #     rawdata1 = request.body
    #     rawdata2 = json.loads(rawdata1)
    #     length = len(rawdata2)
    #     for i in range(0, length,1):
    #         x = meterdata(time_elapsed=rawdata2[i]['time_elapsed'], volts=rawdata2[i]['volts'], amps=rawdata2[i]['amps'], kW=rawdata2[i]['kW'], kWh=rawdata2[i]['kWh'], session=rawdata2[i]['session'])
    #         x.save()
    # read('ConfigFile.properties')

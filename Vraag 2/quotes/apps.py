# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

from .models import Infraction
import json
from datetime import datetime
import os  # Add os import to the imports used above for URL
# Define BASE_DIR or import of it is previously defined
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class QuotesConfig(AppConfig):
    name = 'quotes'

    def ready(self):
        data_folder = os.path.join(
            BASE_DIR, 'import_data', 'resources/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    id = data_object.get('title', None)
                    year = data_object.get('year', None)
                    month = data_object.get('month', None)
                    date = data_object.get('date', None)
                    street = data_object.get('street', None)
                    driving_direction = data_object.get(
                        'driving_direction', None)
                    speed_limit = data_object.get('speed_limit', None)
                    passersby = data_object.get('passersby', None)
                    infractions_speed = data_object.get(
                        'infractions_speed', None)
                    infractions_red_light = data_object.get(
                        'infractions_red_light', None)

                    try:  # try and catch for saving the objects
                        movie, created = Infraction.objects.get_or_create(
                            id=id,
                            year=year,
                            month=month,
                            date=date,
                            street=street,
                            driving_direction=driving_direction,
                            speed_limit=speed_limit,
                            passersby=passersby,
                            infractions_speed=infractions_speed,
                            infractions_red_light=infractions_red_light

                        )
                        if created:
                            movie.save()
                        display_format = "\nMovie, {}, has been saved."
                        print(display_format.format(movie))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this movie: {}\n{}".format(
                            id, str(ex))
                        print(msg)

# from django.db import models
# from django.utils import simplejson as json
# from django.conf import settings
# from datetime import datetime
# import time


# class JSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, datetime.date):
#             return obj.strftime('%Y-%m-%d')
#         elif isinstance(obj, datetime.time):
#             return obj.strftime('%H:%M:%S')
#         return json.JSONEncoder.default(self, obj)


# class JSONDecoder(json.JSONDecoder):
#     def decode(self, json_string):
#         json_data = json.loads(json_string)
#         for key in json_data.keys():
#             try:
#                 json_data[key] = datetime.fromtimestamp(time.mktime(
#                     time.strptime(json_data[key], "%Y-%m-%d %H:%M:%S")))
#             except TypeError:
#                 It's not a datetime/time object
#                 pass
#         return json_data


# class JSONField(models.TextField):
#     def _dumps(self, data):
#         return JSONEncoder().encode(data)

#     def _loads(self, str):
#         return JSONDecoder().decode(str)

#     def db_type(self):
#         return 'text'

#     def pre_save(self, model_instance, add):
#         value = getattr(model_instance, self.attname, None)
#         return self._dumps(value)

#     def contribute_to_class(self, cls, name):
#         self.class_name = cls
#         super(JSONField, self).contribute_to_class(cls, name)
#         models.signals.post_init.connect(self.post_init)

#         def get_json(model_instance):
#             return self._dumps(getattr(model_instance, self.attname, None))
#         setattr(cls, 'get_%s_json' % self.name, get_json)

#         def set_json(model_instance, json):
#             return setattr(model_instance, self.attname, self._loads(json))
#         setattr(cls, 'set_%s_json' % self.name, set_json)

#     def post_init(self, **kwargs):
#         if 'sender' in kwargs and 'instance' in kwargs:
#             if kwargs['sender'] == self.class_name and hasattr(kwargs['instance'], self.attname):
#                 value = self.value_from_object(kwargs['instance'])
#                 if (value):
#                     setattr(kwargs['instance'],
#                             self.attname, self._loads(value))
#                 else:
#                     setattr(kwargs['instance'], self.attname, None)


# class SampleModel(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     data = JSONField(null=True, blank=True)


# data = {'pets': None, 'children': ['Benjamin', 'Clare', 'Joshua'], 'some_date': datetime(2010, 02, 01)}
# # Test decode / encode
# decode = JSONEncoder().encode(data)
# encode = JSONDecoder().decode(decode)

# # Save model
# sample = SampleModel(first_name='Patrick', last_name='Altman')
# sample.data = data
# sample.save()

        # data = fin.read().splitlines(True)
# decode = JSONEncoder().encode(data)

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

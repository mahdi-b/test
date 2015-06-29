import json
from .OriginalWidgets import NumberWidget
from django.http import HttpResponse

from RedisClasses.RedisQueries import RedisQueries
import redis



class CustomNumberWidget(NumberWidget):
    
    rq = RedisQueries()

    def __init__(self):
        self.title = "Users's sensor"
        self.detail = "Temperature"
        self.value = 25 
        self.more_info = "in degrees C"

    def get_value(self):
        return self.value
    def get_detail(self):
        return self.detail
    def get_more_info(self):
        return self.more_info 

    def getContext(self, params):
        # update value, based on user id and sensor id pass in params
        # print "pulling info for usuer %s for sensor %s " % (params["userId"], params["sensorId"])
        self.value = self.rq.getLastValue(params["userId"], params["projectId"], params["sensorId"])




 

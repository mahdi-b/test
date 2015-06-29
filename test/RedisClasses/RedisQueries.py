import redis
from ConnectionPool import ConnectionPool

#TODO: use the user information for validation

class RedisQueries():
    pool=ConnectionPool()
    r = redis.Redis(connection_pool=pool)
    
    def getLastValue(self, userId, projectId, sensorId):
        # drop the letters from userId, projectId and sensort Id
        userId = userId[1:]
        projectId = projectId[1:] 
        sensorId = sensorId[1:]
        print "888888 %s %s %s" % (userId, projectId, sensorId)
        lastEvents = self.r.zrange("project:%s:sensor:%s:events" % (projectId, sensorId) , -1, -1)
        if len(lastEvents) > 0:
            return self.r.hgetall("event:%s" % lastEvents[0])['data']
        





import redis

# TODO: set max number of connections in the pool
# return error if number of connections exceeds the max

class ConnectionPool(object):
    _instance = None
    _pool = None
    def __new__(cls, *args, **kwargs):
        if not cls._pool:
            cls._popl =  redis.StrictRedis(host='localhost', port=6379, db=0)
        return cls._instance
    

# if __name__ == '__main__':
#     pool=ConnectionPool()
#     r = redis.Redis(connection_pool=pool)
#     r.set('hello', 'world')





    


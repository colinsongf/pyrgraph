import redis

__name__ = "pyrgraph"
__all__ = ['node']

redis_conn = None;

prefix = 'pyrgraph'
def get_redis():
    global redis_conn

    if not redis_conn:
        redis_conn = redis.Redis();

    return redis_conn

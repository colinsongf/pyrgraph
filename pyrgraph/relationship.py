import pyrgraph
from pyrgraph.entity import Entity

class Relationship(Entity):
    isNew  = True
    start  = None
    type   = None
    end    = None
    weight = 0;
    attrs  = {}

    def __init__(self, start=None, end=None, type=None, weight=0, attrs={}):
        self.type   = type
        self.start  = start
        self.end    = end
        self.weight = weight
        self.attrs  = attrs

    @staticmethod
    def find(start, end, type):
        pass

    @staticmethod
    def get(start, end, type):
        sid = start.id
        eid = end.id

        key = pyrgraph.prefix + ':' + sid + ':r:#' + type + ':out'
        wgh = Relationship.get_redis().zscore(key, eid);

        if wgh is None:
            return None;

        key   = pyrgraph.prefix + ':' + sid + ':r:#' + type + ':' + eid
        attrs = Relationship.get_redis().hgetall(key)

        return Relationship(start=start, end=end, type=type, weight=wgh, attrs=attrs);

    def create(self):
        sid = self.start.id
        eid = self.end.id
        typ = self.type
        wgh = self.weight

        key = pyrgraph.prefix + ':' + sid + ':r:#' + typ + ':out'
        self.get_redis().zadd(key, eid, wgh)

        key = pyrgraph.prefix + ':' + eid + ':r:#' + typ + ':in'
        self.get_redis().zadd(key, sid, wgh)

        key = pyrgraph.prefix + ':' + sid + ':r:out'
        self.get_redis().sadd(key, eid)

        key = pyrgraph.prefix + ':' + eid + ':r:in'
        self.get_redis().sadd(key, sid)

        if self.attrs:
            key = pyrgraph.prefix + ':' + sid + ':r:#' + typ + ':' + eid
            self.get_redis().hmset(key, self.attrs);

    def delete(self):
        sid = self.start.id
        eid = self.end.id
        typ = self.type
        wgh = self.weight

        key = pyrgraph.prefix + ':' + sid + ':r:#' + typ + ':out'
        self.get_redis().zrem(key, eid)

        key = pyrgraph.prefix + ':' + eid + ':r:#' + typ + ':in'
        self.get_redis().zrem(key, sid)

        key = pyrgraph.prefix + ':' + sid + ':r:out'
        self.get_redis().srem(key, eid)

        key = pyrgraph.prefix + ':' + eid + ':r:in'
        self.get_redis().srem(key, sid)

        key   = pyrgraph.prefix + ':' + sid + ':r:#' + typ + ':' + eid
        attrs = self.get_redis().hgetall(key);
        for attr in attrs:
            self.get_redis().hdel(key, attr);

    def increment_weight(self, weight):
        sid = self.start.id
        eid = self.end.id
        typ = self.type

        self.weight = self.weight + weight;

        key = pyrgraph.prefix + ':' + sid + ':r:#' + typ + ':out'
        self.get_redis().zincrby(key, eid, weight)

        key = pyrgraph.prefix + ':' + eid + ':r:#' + typ + ':in'
        self.get_redis().zincrby(key, sid, weight)

    def decerement_weight(self, weight):
        self.increment_weight(-1 * weight);


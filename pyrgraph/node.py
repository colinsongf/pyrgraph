import pyrgraph
from pyrgraph.entity import Entity

class Node(Entity):
    isNew = True
    id    = None
    attrs = {}

    def __init__(self, id=None, attrs={}):
        self.id = id
        self.attrs = attrs

    @staticmethod
    def get(nid):
        obj = Node.get_redis().hgetall(Node.key(nid))
        if 'id' not in obj:
            return None;

        node = Node(obj['id'])
        del(obj['id']);
        node.attrs = obj;

        return node

    @staticmethod
    def key(nid):
        return pyrgraph.prefix + ':' + nid

    def create(self):
        attrs       = self.attrs;
        attrs['id'] = self.id;

        self.get_redis().hmset(self.key(self.id), attrs);

    def delete(self):
        self.get_redis().delete(self.key(self.id));

    def incoming(self, type):
        key     = pyrgraph.prefix + ':' + self.id + ':r:#' + type + ':in'
        records = self.get_redis().zrevrangebyscore(key, "+inf", "-inf", withscores=True)
        result  = []

        for item in records:
            node = self.get(item[0]);
            result.append((node, item[1]))

        return result

    def outgoing(self, type):
        key     = pyrgraph.prefix + ':' + self.id + ':r:#' + type + ':out'
        records = self.get_redis().zrevrangebyscore(key, "+inf", "-inf", withscores=True)
        result  = []

        for item in records:
            node = self.get(item[0]);
            result.append((node, item[1]))

        return result

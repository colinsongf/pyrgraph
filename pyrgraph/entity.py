import pyrgraph

class Entity:
    def key(self):
        return pyrgraph.prefix

    @staticmethod
    def get_redis():
        return pyrgraph.get_redis();

    def save(self):
        self.create()
        pass

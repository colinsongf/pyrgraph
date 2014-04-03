pyrgraph
========

Pyrgraph is a Redis-backed graph database.


Example usage
-------------

```python
import pyrgraph

from pyrgraph.node import Node
from pyrgraph.relationship import Relationship

node1 = Node('123')
node1.attrs["type"] = "name"
node1.save()


node2 = Node('124')
node2.attrs["type"] = "name"
node2.save()

node3 = Node('125')
node3.attrs["type"] = "name"
node3.save()

rel = Relationship(start=node1, end=node2, type="depends", weight=100)
rel.attrs['name'] = 'ddd';
rel.save()

rel.increment_weight(10);
print rel.weight;

rel.decerement_weight(10);
print rel.weight;


rel = Relationship(start=node1, end=node3, type="depends", weight=100)
rel.save()

print node1.outgoing('depends');

rel.delete()
node1.delete();
node2.delete();


```

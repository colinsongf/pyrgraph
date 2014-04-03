
import pyrgraph

from pyrgraph.node import Node
from pyrgraph.relationship import Relationship

node1 = Node('123')
node1.attrs["type"] = "name"
node1.save()


node2 = Node('124')
node2.attrs["type"] = "name"
node2.save()


rel = Relationship(start=node1, end=node2, type="depends", weight=100)
rel.attrs['name'] = 'ddd';
rel.save()

rel.increment_weight(10);
print rel.weight;

rel.decerement_weight(10);
print rel.weight;

rel.delete()
node1.delete();
node2.delete();

#rel2 = Relationship.get(node1, node2, type="depends");
#print rel2.weight

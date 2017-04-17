from practice.Graph import Graph


g = Graph()
node = ['A', 'B', 'C', 'D']
for i in node:
    print(g.addVertex(i))
print(g.vertList)
g.addEdge('A', 'B', 5)
g.addEdge('A', 'C', 2)
g.addEdge('A', 'D', 7)
g.addEdge('B', 'D', 2)
g.addEdge('B', 'C', 1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s)" % (v.getId(), w.getId()))
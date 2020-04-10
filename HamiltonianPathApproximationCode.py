from random import seed
from random import randint

def findSet(parent, u):
    if parent[u] == u:
        return u
    parent[u] = findSet(parent, parent[u])
    return parent[u]

def unionSet(parent, rnk, u, v):
    u = findSet(parent, u)
    v = findSet(parent, v)
    if u != v:
        if rnk[u] < rnk[v]:
            temp = u
            u = v
            v = temp
        parent[v] = u
        if rnk[u] == rnk[v]:
            rnk[u]+=1

class Edge:
    def __init__(self, _u, _v):
        self.u = _u
        self.v = _v

def AHP(edge, n):
    parent = [i for i in range(n)] #0123 for n = 4
    rnk = [0 for i in range(n)] #0000 for n = 4
    path = []
    restore = []
    vis = [False]*n
    i = 0
    while i < n/2 and len(edge) > 0:
        e = edge.pop(randint(0,len(edge)-1))
        if findSet(parent, e.u) != findSet(parent, e.v) and not vis[e.u] and not vis[e.v]:
            vis[e.u] = vis[e.v] = True
            unionSet(parent, rnk, e.u, e.v)
            path.append((e.u,e.v))
            #print(path)
            i += 1
        else:
            restore.append(Edge(e.u,e.v))

    for e in restore:
      edge.insert(len(edge), Edge(e.u, e.v))

    vis = [False]*n
    i = 0
    while i < n/2-1 and len(edge) > 0:
        e = edge.pop(randint(0,len(edge)-1))
        if findSet(parent, e.u) != findSet(parent, e.v) and not vis[e.u] and not vis[e.v]:
            vis[e.u] = vis[e.v] = True
            unionSet(parent, rnk, e.u, e.v)
            path.append((e.u, e.v))
            #print(path)
            i += 1
    return path

seed()
'''
edge = [ # u, v
  Edge(0,1),
  Edge(0,3),
  Edge(0,5),
  Edge(1,2),
  Edge(1,3),
  Edge(1,4),
  Edge(2,5),
  Edge(2,6),
  Edge(3,6),
  Edge(5,6)
]
'''
edge = [ # u, v
  Edge(0,1),
  Edge(0,2),
  Edge(0,3),
  Edge(0,4),
  Edge(0,5),
  Edge(0,6),
  Edge(1,2),
  Edge(1,3),
  Edge(1,4),
  Edge(1,5),
  Edge(1,6),
  Edge(2,3),
  Edge(2,4),
  Edge(2,5),
  Edge(2,6),
  Edge(3,4),
  Edge(3,5),
  Edge(3,6),
  Edge(4,5),
  Edge(4,6),
  Edge(5,6)
]

numVertices = 7

for e in edge:
   print(e.u, "<->", e.v)

path = AHP(edge, numVertices)

if len(path) == numVertices-1:
    print("Path found!", path)
else:
    print("No Path")
from random import seed
from random import randint
import time
import math
import os.path

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

arr_vertexnum = [5, 6, 7, 8, 9, 10, 15, 20]
arr_graphnum = [100, 1000, 3000, 5000, 10000]
for i in arr_vertexnum:
    for j in arr_graphnum:
        num_total_successful = 0
        time_avg = 0
        time_tot = 0
        #edge = []
        numVertices = i
        vertexnum = str(i)
        graphnum = str(j)
        filename = ""
        filename = filename + "vertex" + vertexnum + "graph" + graphnum + "3.txt"
        f = open(filename, 'r')
        graph = f.readlines()
        f.close()
        for k in range(0, j):
            edge = []
            index = 0
            graph_str_arr = graph[k].split()
            while index < len(graph_str_arr):
                e1 = int(graph_str_arr[index])
                index = index + 1
                #print(graph_str_arr[index])
                e2 = int(graph_str_arr[index])
                index = index + 1
                edge.append(Edge(e1, e2))
           # for e in edge:
            #    print(e.u, "<->", e.v)
            t0 = time.time()
            if len(edge) == 1:
                1+1
            path = AHP(edge, numVertices)
            if len(path) == numVertices-1:
                num_total_successful += 1
            t1 = time.time()
            time_overall = t1 - t0
            time_tot += time_overall
            #    print("Path found!", path)
            #else:
            #    print("No Path")
        time_avg = time_tot / j
        print("Number of Hamiltonian Paths in Test: Number of Vertices = ", i, " Number of Graphs = ", j, " Amount of Success : ", num_total_successful, " Ratio of Success = ", num_total_successful / j, "Average time taken: ", time_avg)
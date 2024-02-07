# Graph implementation using Adjacency List
class Graph:
    def __init__(self,size):
        self.size=size
        self.adjLst={}
        
    def add_vertex(self,val):
        if val not in self.adjLst:
            self.adjLst[val]=[]
    def add_edge(self,v1,v2):
        if (v2 not in self.adjLst[v1]):
            self.adjLst[v1].append(v2)
    def bfs(self,node):
        visited=[]
        queue=[]

        visited.append(node)
        queue.append(node)

        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for neighbour in self.adjLst[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    def dfs(self,node):
        if node not in self.visited:
            print(node)
            self.visited.append(node)
            for neighbour in self.adjLst[node]:
                self.dfs(neighbour)

g=Graph(4)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(2,4)
g.bfs(1)
print(g.adjLst)


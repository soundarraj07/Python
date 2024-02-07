class city:
    def __init__(self,size,vertex,graph):
        self.size=size
        self.graph=graph
        self.vertex=vertex
        self.visited=[]
    def dfs(self,node):
        if node not in self.visited:
            print(node)
            self.visited.append(node)
            arr=self.graph[self.vertex.index(node)]
            adj=[]
            for i in range(self.size):
                if arr[i]==1:
                    adj.append(self.vertex[i])
            for neighbour in adj:
                self.dfs(neighbour)
ver=["city a","city b","city c","city d","city e","city f","city g"]
n=7
graph=[[0,1,1,0,0,0,1],[0,0,0,1,0,1,1],[0,1,0,1,0,0,1],[0,0,0,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,1,1,1],[0,1,1,0,0,0,1]]
cty=city(n,ver,graph)
cty.dfs("city c")

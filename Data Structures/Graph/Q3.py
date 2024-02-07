# Graph Data Structure Implementation Date 01 DEC
# using adjacency matrix
class graphs:
    def __init__(self,size):
        self.size=size
        self.graph=[] # adjacency matrix
        self.vertex=[]
        self.visited=[]
    def add_vertex(self,val):
        if val in self.vertex:
            pass
        else:
            self.vertex.append(val)
            temp=[]
            for i in range (self.size):
                temp.append(0)
            self.graph.append(temp)
    def add_edge(self,v1,v2):
        i=self.vertex.index(v1)
        j=self.vertex.index(v2)
        self.graph[i][j]=1
    def bfs(self,node):
        visited=[]
        queue=[]

        visited.append(node)
        queue.append(node)

        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            arr=self.graph[self.vertex.index(s)]
            adj=[]
            for i in range(self.size):
                if arr[i]==1:
                    adj.append(self.vertex[i])
            for neighbour in adj:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    def dfs2(self,node):
        stack=[]
        visited=[]
        stack.append(node)
        visited.append(node)
        while stack:
            s=stack.pop()
            print(s,end=" ")
            arr=self.graph[self.vertex.index(s)]
            adj=[]
            for i in range (self.size):
                    if arr[i]==1:
                        adj.append(self.vertex[i])
            for neighbour in adj:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)
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
    def get_input_graph(self):
        n=int(input("Enter the n vertices : "))
        # to get input one by one
        # for i in range(n):
        #     temp=[]
        #     for i in range(n):
        #         m=int(input())
        #         temp.append(m)
        #     self.graph.append(temp)
        for i in range(n):
            temp=[]
            temp2=[]
            m=(input())
            temp=m.split(" ")
            for i in range(n):
                temp2.append(int(temp[i]))
            self.graph.append(temp2)
arr=[]
n=int(input("Enter how many equations :"))
for i in range (n):
    arr.append(input())
arr2=[]
ver=[]
for i in range(n):
    if arr[i][0] not in arr2:
        ver.append(arr[i][0])
        arr2.append(arr[i][0])
    if arr[i][3] not in arr2:
        ver.append(arr[i][3])
        arr2.append(arr[i][3])
print(ver)
g=graphs(4)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1,2)
# g.add_edge(2,3)
g.add_edge(1,3)
g.add_edge(4,2)
g.add_edge(2,4)

# g.get_input_graph()
#g.bfs(1)
g.dfs(1)
print()
g.dfs2(1)
print(g.graph)

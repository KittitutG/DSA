class Graph:
    def __init__(self,gdict) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self,start,stop):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == stop:
                return path
            
            for vertices in self.gdict.get(node,[]):
                new_path = list(path)
                new_path.append(vertices)
                queue.append(new_path)

customdict = {"a":["b","c"]
              ,"b":["d","g"]
              ,"c":["d","e"]
              ,"d":["f"]
              ,"e":["f"]
              ,"g":["f"]
              }

g = Graph(customdict)
print(g.bfs("a","f"))

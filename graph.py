'''
Graph is a tree where any two nodes can have connections in between as well
Graph: 
    - Nodes
    - edges
Weighted graph: where edges have certain weight value to indicate its importance

'''


class Graph():
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                # Node does exist: append a val
                self.graph_dict[start].append(end)
            else:
                # Node does not exist: create and assign a val
                self.graph_dict[start] = [end]
        print('Graph dict:', self.graph_dict)

    def get_paths(self, start, end, path=[]):
        # one path at every run
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []

        paths = [] # all possible paths
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        
        return paths

    def shortest_path(self, start, end):
        # EITHER
        paths = self.get_paths(start, end)
        #shortest path
        sp = 0
        sort_p = []
        import numpy as np
        
        for pp in paths:
            
            if len(pp) <= sp:
                sp = len(pp) 
                sort_p.append(pp)
            else:
                sort_p = pp
        
        # OR
        min_ = np.argmin(paths)
        print(paths[min_])

        return sort_p

if __name__ == '__main__':
    routes = [
                ('Mumbai', 'Paris'),
                ('Mumbai', 'Dubai'),
                ('Paris', 'Dubai'),
                ('Paris', 'Newyork'),
                ('Dubai', 'Newyork'),
                ('Newyork', 'Tornoto') 
             ]
    route_graph = Graph(routes)
    
    start = 'Mumbai'
    end = 'Newyork' 
    print(f"\nPath between {start} and {end}", route_graph.get_paths(start, end))

    print(f"\nSortest path between {start} and {end}", route_graph.shortest_path(start, end))
    print('\nend')
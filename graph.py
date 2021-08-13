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

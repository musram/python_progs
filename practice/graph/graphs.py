import os

class EdgeNode(object):
    def __init__(self, y , weight, edgenode):
        self.y = y
        self.weight = weigth
        self.edgenode = edgenode

    def __repr__(self):
        return 'Node {} has weight {}'.format(self.y, self.weight)


class Graph(object):
    def __init__(self, out_degree, num_vertices=None, num_edges=None, isdirected=True ):
        self.edgenode = None;
        self.out_degree = out_degree
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.isdirected = isdirected


    def  read_graph(self, fname):
        if os.path.isfile(fname): 
           with open(fname, 'rt') as f:
               for line in f:
                   (x, w, y) = line
                   
        else:
                     
from graph import Graph

class Examples:
    """
    Une collection de graphes, pour tests, ...
    """
    def __init__(self, Graph=Graph):
        self.Graph = Graph

    def cours_1_G(self):
        return self.Graph((0,1,2,3,4,5), edges=((0,2,1), (1,2,1), (2,3,1), (1,5,1), (5,3,1), (3,4,1)))

    def cours_1_reseau(self):
        A,B,C,D,E,F,G,H = vertices = "A", "B", "C", "D", "E", "F", "G", "H"
        return self.Graph(vertices,
                     edges=((A,B,3), (A,G,2), (A,F,4),
                            (B,C,1), (B,G,1),
                            (C,D,4), (C,G,5), (C,H,2),
                            (D,E,5), (D,H,6),
                            (E,F,3), (E,G,2), (E,H,3),
                            (F,G,1),
                            (G,H,4)))

    def directed(self):
        return self.Graph((1,2,3,4), edges=((1,2,"12"), (1,4,"12"), (2,3,"23")), directed=True)

    def undirected(self):
        return self.Graph((1,2,3,4), edges=((1,2,"12"), (2,3,"23")))

    def disconnected(self):
        return self.Graph((1,2,3,4,5), edges=((1,2,"12"), (2,5,"25"), (3,4, "34")))
examples = Examples()

# -*- coding: utf-8 -*-

class Graph:
    def __init__(self,
                 vertices=None,
                 matrix=None,
                 edges=None,
                 directed=False):
        """
        Initialisation d'un graphe

        INPUT :

            - vertices, un itérables sur les sommets du graphes
            - matrix, la matrice d'adjacence du graphe suivant les mêmes indices que `vertices`
            - edges, une liste de triplets (v1, v2, c) où v1 et v2 sont des sommets et c un nombre positif

        """
        if vertices is None:
            vertices = []

        self._vertices = vertices
        # création d'un dictionnaire associant son indice à chaque sommet
        # (vous pouvez modifier si ça n'est pas utile à votre implantation)
        self._vertex_indices = {vertices[i]: i for i in range(len(vertices))}
        self._directed = directed

        # on ne peut pas donner à la fois matrix et edges
        if matrix is not None and edges is not None:
            raise ValueError("'matrix' et 'edges' ne peuvent pas être tous les deux initialisés")

        # initialisation différenciée: implantez les méthodes en question
        if matrix is not None:
            self._init_from_matrix(matrix)
        elif edges is not None:
            self._init_from_edges(edges)
        else:
            self._init_empty()

    def _init_empty(self):
        """
        Initialisation d'un graphe vide (sans arêtes)
        """
        ### BEGIN SOLUTION
        self._neighbors_out = {u: {} for u in self._vertices }
        ### END SOLUTION


    def _init_from_matrix(self, matrix):
        """
        Initialisation à partir d'une matrice
        """
        ### BEGIN SOLUTION
        self._matrix=matrix
        self._vertices=[i for i in range(0,len(matrix))]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                self._neighbors_out[row][col] = matrix[row][col]


        ### END SOLUTION

    def _init_from_edges(self, edges):
        """
        Initialisation à partir d'une liste de triplets
        """
        # BEGIN SOLUTION
        self._init_empty()
        for u, v, value in edges:
            self._neighbors_out[u][v] = value
            if not self._directed:
                self._neighbors_out[v][u] = value

        # END SOLUTION

    def set_edge_capacity(self, v1, v2, c):
        """
        Donne la capacité `c` à l'arête `(v1,v2)`

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
            - c la capacité de l'arête (v1,v2)
        """
        self._neighbors_out[v1][v2] = value
        if not self._directed:
            self._neighbors_out[v2][v1] = value


    def add_vertex(self, v):
        """
        Ajoute le sommet `v` au graphe

        INPUT:

            - v, un sommet du graphe

        """
        self._vertices += [v]
        self._vertex_indices[v] = len(vertices) - 1


    def vertices(self):
        """
        Renvoie la liste des sommets du graphe

        EXAMPLES::

            >>> from graph_examples import examples
            >>> G = examples.cours_1_reseau()
            >>> G.vertices()
            ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        """
        ### BEGIN SOLUTION
        return self._vertices
        ### END SOLUTION

    def vertex_number(self):
        """
        Renvoie le nombre de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.vertex_number()
            8
        """
        ### BEGIN SOLUTION
        return len(self._vertices)
        ### END SOLUTION

    def has_vertex(self, v1):
        """
        Renvoie vrai si v1 est un sommet du graphe

        INPUT:

            - v1, un sommet
        """
        return (v1 in self._vertices)


    def edges(self):
        """
        Renvoie un tuple de triplets `(v1,v2,c)` correspondant aux arêtes du graphe avec leur capacité.

        EXAMPLES:

            >>> G = Graph((1,2,3,4))
            >>> G. edges()
            ()
            >>> G = examples.directed()
            >>> sorted(G.edges())
            [(1, 2, '12'), (1, 4, '12'), (2, 3, '23')]

            >>> G = examples.undirected()
            >>> sorted(G.edges())
            [(1, 2, '12'), (2, 1, '12'), (2, 3, '23'), (3, 2, '23')]
        """
        ### BEGIN SOLUTION
        return tuple( (u, v, l)
                      for u, out in self._neighbors_out.items()
                      for v, l in out.items() )
        ### END SOLUTION

    def edge_number(self):
        """
        Renvoie le nombre d'arêtes du graphe
        """
        return len(self._neighbors_out)



    def is_edge(self, v1, v2):
        """
        Renvoie si l'arête (v1,v2) existe

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
        """
        return (v1 in self._neighbors_out) & (v2 in self._neighbors_out[v1])


    def capacity(self, v1, v2):
        """
        Renvoie la capacité de l'arête (v1,v2) (si l'arête n'existe pas, la capacité est 0)

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
        """
        return self._neighbors_out[v1][v2]



    def show(self):
        from bqplot import Figure
        from bqplot.marks import Graph
        from ipywidgets import Layout

        fig_layout = Layout(width='600px', height='600px')
        edges = self.edges()
        rank = {vertex: i for i,vertex in enumerate(self.vertices()) }
        graph = Graph(node_data=self.vertices(), link_data=[{'source':rank[i],'target':rank[j],'value':v} for i,j,v in edges],
                          link_type='line', directed=self._directed)
        return Figure(marks=[graph], layout=fig_layout)

    def matrix(self):
        """
        Retourne la matrice associée au graphe
        """
        # à compléter
        return self._matrix

    def to_dict(self):
        """
        Retourne le dictionnaire associé au graphe
        """
        # à compléter

    def neighbors_in(self, v):
        """
        Renvoie la liste des voisins entrants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.neighbors_in("H"))
            ['C', 'D', 'E', 'G']
        """
        ### BEGIN SOLUTION
        return tuple( i for i in self._vertices if v in self._neighbors_out[i])
        ### END SOLUTION

    def neighbors_out(self, v):
        """
        Renvoie la liste des voisins sortants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.neighbors_out("A"))
            ['B', 'F', 'G']
        """
        ### BEGIN SOLUTION
        return tuple(self._neighbors_out[v].keys())
        ### END SOLUTION

    def is_path(self, p):
        """
        Renvoie si p est un chemin valide dans le graphe

        INPUT:

            - v, une liste de sommets du graphe
        """
        begin = p[0]
        if not self.has_vertex(begin):
            return False

        for sommet in p[1:]:
            if not self.is_edge(begin, sommet):
                return False
            begin = sommet
        
        return True


from graph_examples import examples


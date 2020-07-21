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

    def is_directed(self):
        """
        Renvoie si le graph est orienté
        """
        return self._directed


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
    def get_edge_data(self,u,v):
        return {"weight":self._neighbors_out[u][v]}
    
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
    def add_edge(self, u,v,weight):
        if(self._directed == False):
            self._neighbors_out[u].update({v:weight})
            self._neighbors_out[v].update({u:weight})
        else:
            self._neighbors_out[ u].update({v:weight})


    def vertices(self):
        """
        Renvoie la liste des sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.vertices()
            ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        """
        ### BEGIN SOLUTION
        return tuple(self._vertices)

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
            [(1, 2, 12), (1, 4, 12), (2, 3, 23)]

            >>> G = examples.undirected()
            >>> sorted(G.edges())
            [(1, 2, 12), (2, 1, 12), (2, 3, 23), (3, 2, 23)]
        """
        return tuple( (u, v, l)
                      for u, out in self._neighbors_out.items()
                      for v, l in out.items() )


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

    def matrix(self):
        """
        Retourne la matrice associée au graphe

        Soit `n` le nombre de sommets du graphe. Cette méthode renvoie
        une liste `M` de n listes de taille n, de sorte que `M[i][j]`
        est la capacité de l'arête reliant le i-ème sommet au j-ème
        sommet dans le graphe, s'il y en a une, et 0 sinon.

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.matrix()              # doctest: +NORMALIZE_WHITESPACE
            [[0, 12, 0, 12],
             [0, 0, 23, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        """
        return [[(self._neighbors_out[u][v] if self.is_edge(u,v) else 0) for v in self._vertices] for u in self._vertices]



    def to_dict(self):
        """
        Retourne le dictionnaire associé au graphe
        """
        return self._neighbors_out


    def neighbors_in(self, v):
        """
        Renvoie la liste des voisins entrants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.neighbors_in("H"))
            ['C', 'D', 'E', 'G']
            >>> G = examples.directed()
            >>> G.neighbors_in(1)
            ()
            >>> G.neighbors_in(2)
            (1,)
        """
        return tuple( i for i in self._vertices if v in self._neighbors_out[i])


    def neighbors_out(self, v):
        """
        Renvoie la liste des voisins sortants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.neighbors_out("A"))
            ['B', 'F', 'G']
            >>> G = examples.directed()
            >>> sorted(G.neighbors_out(1))
            [2, 4]
            >>> G.neighbors_out(2)
            (3,)
            >>> G.neighbors_out(4)
            ()
        """
        return tuple(self._neighbors_out[v].keys())



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



    def networkx(self):
        import graph_networkx
        return graph_networkx.Graph(self.vertices(), self.edges(), directed=self.is_directed())

    
    def visit(self,u, pred_node, marked,l):
        l.append(u)
        marked[u] = pred_node
        res=False
        for v in self.neighbors_out(u):
            if marked[v] !=False  and v != pred_node:
                return True,marked,l
            if not marked[v]:
                r=self.visit(v, u, marked,l)
                res,marked,l=r

            if res==True:
                return True,marked,l

        return False,marked,l

    def Analysis_cycle(self):                                    
        marked = { u : False for u in self.vertices() }
        found_cycle = [False]
        for u in self.vertices():
            l=[]
            if marked[u]==False:
                res,marked,l=self.visit(u=u,pred_node=u,marked=marked,l=l)
            if res==True:
                return True,marked,l
        return False,marked,l

    def is_acyclic(self):
        return not self.Analysis_cycle()[0]
    def is_cyclic(self):
        return  self.Analysis_cycle()[0]
    def find_cycle(self):
        res=self.Analysis_cycle()
        if res[0]:
            return res[2]
        return res[0]
    
    
    def is_connected(self):
        return self.edge_number() >= self.vertex_number()-1 and len(self.connected_components())==1
    def connected_components(self):
        res = []
        rest = self.vertices()

        while rest:
            s = rest[0]
            visited = {s} # L'ensemble des sommets déjà rencontrés
            todo = {s} # L'ensemble des sommets non traités

            while todo:
                v = todo.pop()
                for w in self.neighbors_out(v):
                    if w not in visited:
                        visited.add(w)
                        todo.add(w)
            res.append(visited)
            rest = [s for s in rest if s not in visited]
        return res
    def is_tree(self):
        return self.is_acyclic() and  self.is_connected()
    def arbre(G):

        cycle=find_cycle(G)
        while(cycle!=False):
            G.remove_edge(cycle[0],cycle[-1])
            cycle=find_cycle(G)
        return G
    def remove_edge(self,u,v):
        del self._neighbors_out[u][v]
        del self._neighbors_out[v][u]
        return Graph(edges=self.edges(),vertices=self.vertices())

    def arbre(self):
        G2=Graph(edges=self.edges(),vertices=self.vertices())
        cycle=G2.find_cycle()
        while(cycle!=False):
            G2=G2.remove_edge(cycle[0],cycle[-1])
            cycle=G2.find_cycle()
        return G2
    def show(self):
        return self.networkx().show()


import graph_examples 
examples = graph_examples.Examples(Graph)

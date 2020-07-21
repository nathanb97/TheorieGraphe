import networkx

def Graph(vertices, edges):
    G = networkx.Graph()
    G.add_nodes_from(vertices)
    if edges:
        if len(edges[0]) == 2:
            G.add_edges_from(edges)
        else:
            G.add_weighted_edges_from(edges)
    return G

def show(graph, fig=None):
    import bqplot.marks
    from ipywidgets import Layout
    import traitlets
    nodes = graph.nodes()
    edges = graph.edges()
    node_data = [ str(i) for i in nodes ]
    rank = { v: i for i,v in enumerate(nodes) }
    link_data = [{'source': rank[s],
                  'target': rank[t],
                 #'value': l} for s,t,l in edges
                 } for s, t in edges]

    layout = networkx.spring_layout(graph)
    xs = bqplot.LinearScale()
    ys = bqplot.LinearScale()
    x = [layout[node][0] for node in nodes]
    y = [layout[node][1] for node in nodes]

    if fig is None:
        fig_layout = Layout(width='600px', height='600px')
        mark = bqplot.marks.Graph(node_data=node_data,
                                  link_data=link_data,
                                  link_type='line', directed=False,
                                  scales={'x': xs, 'y': ys, }, x=x, y=y,
                                  charge=-600,
                                  colors=['orange'] * 7)
        fig = bqplot.Figure(marks=[mark],
                            layout=fig_layout)
    else:
        raise NotImplementedError("coucou")
    return fig

networkx.Graph.show = show


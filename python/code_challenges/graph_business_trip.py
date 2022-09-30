from data_structures.graph import Graph


def direct_flights(graph, places):
    if len(places) == 0:
        return "null"

    nodes = {}
    for vertex in graph.get_nodes():
        nodes[vertex.value] = vertex

    end = 0
    next_ = 1
    for place in places:
        if next_ < len(places):
            links = {}
            edges = graph.get_neighbors(nodes[place])
            for edge in edges:
                links[edge.vertex.value] = edge

            if places[next_] not in links.keys():
                return "null"

            end += links[places[next_]].end
            next_ += 1

    return end

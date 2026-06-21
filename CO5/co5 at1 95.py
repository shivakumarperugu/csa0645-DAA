def is_safe(vertex, graph, colors, color):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring(graph, k, colors, vertex):

    if vertex == len(graph):
        return True

    for color in range(1, k + 1):

        if is_safe(vertex, graph, colors, color):

            colors[vertex] = color

            if graph_coloring(graph, k, colors, vertex + 1):
                return True

            colors[vertex] = 0

    return False


# Sample Graph
graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

k = 3
n = len(graph)
colors = [0] * n

if graph_coloring(graph, k, colors, 0):
    print("Color Assignment:")
    print(colors)
else:
    print("Graph cannot be colored with", k, "colors")
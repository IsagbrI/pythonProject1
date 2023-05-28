# import networkx as nx
# import matplotlib.pyplot as plt
#
# def draw_graph(graph):
#     # Создаем граф NetworkX из входного графа
#     G = nx.Graph(graph)
#
#     # Определяем позиции узлов графа
#     pos = nx.spring_layout(G)
#
#     # Рисуем узлы графа
#     nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
#
#     # Рисуем ребра графа
#     nx.draw_networkx_edges(G, pos, edge_color='gray')
#
#     # Рисуем подписи узлов графа
#     nx.draw_networkx_labels(G, pos, font_color='black')
#
#     # Отображаем граф
#     plt.axis('off')
#     plt.show()
#
#
# def create_graph_from_adjacency_matrix(adjacency_matrix):
#     graph = {}
#
#     # Получаем количество вершин графа
#     num_vertices = len(adjacency_matrix)
#
#     # Создаем список вершин
#     vertices = [chr(ord('0') + i) for i in range(num_vertices)]
#
#     # Для каждой вершины создаем список смежных вершин
#     for i in range(num_vertices):
#         vertex = vertices[i]
#         neighbors = []
#
#         # Проверяем матрицу смежности для текущей вершины
#         for j in range(num_vertices):
#             if adjacency_matrix[i][j] == 1:
#                 neighbor = vertices[j]
#                 neighbors.append(neighbor)
#
#         graph[vertex] = neighbors
#
#     return graph


import networkx as nx

#---directed graph---
G = nx.DiGraph(directed=True)

# add nodes
G.add_node("Singapore")
G.add_node("San Francisco")
G.add_node("Tokyo")
G.add_nodes_from(["Riga", "Copenhagen"])

# add edges
G.add_edge("Singapore","San Francisco")
G.add_edge("San Francisco","Tokyo")
G.add_edges_from(
    [
        ("Riga","Copenhagen"),
        ("Copenhagen","Singapore"),
        ("Singapore","Tokyo"),
        ("Riga","San Francisco"),
        ("San Francisco","Singapore"),
    ]
)
# set layout
pos = nx.circular_layout(G)

# draw graph
nx.draw(G, pos, with_labels = True)

# draw edge labels
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
        ("Singapore","Tokyo"): '2 flights daily',
        ("San Francisco","Singapore"): '5 flights daily',
    },
    font_color='red'
)

adjacency_matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
graph = create_graph_from_adjacency_matrix(adjacency_matrix)

draw_graph(graph)
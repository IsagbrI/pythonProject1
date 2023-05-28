в этой программе возникает есть проблема с строке self.draw_graph(self, graph) связанная с параметром graph. исправь
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.graphWidget = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate_graph)

    def draw_graph(self, graph):
        # Создаем граф NetworkX из входного графа
        G = nx.Graph(graph)

        # Определяем позиции узлов графа
        pos = nx.spring_layout(G)

        # Создаем объект Figure для отображения графа
        fig = Figure()
        canvas = FigureCanvas(fig)

        # Получаем текущую ось и очищаем ее
        ax = fig.gca()
        ax.clear()

        # Рисуем узлы графа
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=500)

        # Рисуем ребра графа
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray')

        # Рисуем подписи узлов графа
        nx.draw_networkx_labels(G, pos, ax=ax, font_color='black')

        # Очищаем текущую область отображения
        self.graphWidget.clear()

        # Добавляем объект FigureCanvas в виджет QGraphicsView
        layout = QtWidgets.QVBoxLayout(self.graphWidget)
        layout.addWidget(canvas)

        # Перерисовываем виджет
        canvas.draw()

    def create_graph_from_adjacency_matrix(self, adjacency_matrix):
        graph = {}

        # Получаем количество вершин графа
        num_vertices = len(adjacency_matrix)

        # Создаем список вершин
        vertices = [chr(ord('A') + i) for i in range(num_vertices)]

        # Для каждой вершины создаем список смежных вершин
        for i in range(num_vertices):
            vertex = vertices[i]
            neighbors = []

            # Проверяем матрицу смежности для текущей вершины
            for j in range(num_vertices):
                if adjacency_matrix[i][j] == 1:
                    neighbor = vertices[j]
                    neighbors.append(neighbor)

            graph[vertex] = neighbors

        return graph

    def calculate_graph(self):
        # Получение матрицы смежности из textEdit
        matrix_text = self.textEdit.toPlainText()
        matrix_rows = matrix_text.strip().split('\n')
        adjacency_matrix = [list(map(int, row.strip().split())) for row in matrix_rows]

        # Создание графа и отрисовка
        graph = self.create_graph_from_adjacency_matrix(adjacency_matrix)
        self.draw_graph(self, graph)

        # Вычисление и вывод показателей
        matrix, sum_elem = self.Creat_Matrix(adjacency_matrix)
        string, sum_elem = self.Recording_Conjunctions(matrix, sum_elem)
        if string == "Matrix not correct" and sum_elem == -1:
            self.label.setText(f"{string}")
        else:
            string, result1, sum_elem = self.factorize(string, sum_elem)
            result2, string, sum_elem = self.DNF(string, sum_elem)
            string = self.Sets_Of_Internal_Stability(string, sum_elem)
            result3 = self.Print_Sets_Of_Internal_Stability(string)
            # result1 = self.Creat_Matrix(adjacency_matrix)
            # result2 = "______________________________________"
            # result3 = "______________________________________"
            self.label.setText(
                f"Дизъюнкции (дороги из _ в _) : {result1}\nДНФ: {result2}\nМаксимально внутренне устойчивые подмножества графа: {result3}")
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 856)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.353234, y2:0.557, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(27, 0, 148, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 380, 521, 431))
        self.label.setWordWrap(True)
        self.label.setStyleSheet("font: 15pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 380, 151, 51))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Times New Roman\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 536, 341))
        self.textEdit.setStyleSheet("font: 15pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 536, 41))
        self.label_2.setWordWrap(True)
        self.label_2.setStyleSheet("font: 15pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Выполнить</span></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Выполнить</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Выполнить"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "                                     Матрица смежности"))


def Taking_Out(string, kol_elem):
        loc_count = 0
        vin = str()
        # print(string, "_____________")
        while loc_count <= kol_elem:
            if string.count(str(loc_count)) == 2:
                vin = str(loc_count)
                # print(vin)
                break
            loc_count += 1
        # print(vin, "----")
        if len(vin) != 0:
            result = "(" + vin + "v"
            flag = 0
            for i in range(len(string)):

                if string[i] != "(" and string[i] != ")" and string[i] != "v" and string[i] != vin:
                    result += string[i]
                    flag = 1

                if len(result) == 6:
                    result += ")"
                    break
                if string[i] != "(" and string[i] != ")" and string[i] != "v" and string[i] != vin and flag == 1:
                    result += "^"
            # print(result, "============")
            return result
        else:
            return string


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.graphWidget = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate_graph)


    @staticmethod
    def draw_graph(graph):
        G = nx.DiGraph(graph)
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(G, pos, edge_color='gray')
        nx.draw_networkx_labels(G, pos, font_color='black')
        plt.axis('off')
        plt.show()


    @staticmethod
    def create_graph_from_adjacency_matrix(adjacency_matrix):
        graph = {}
        num_vertices = len(adjacency_matrix)
        vertices = [chr(ord('0') + i) for i in range(num_vertices)]
        for i in range(num_vertices):
            vertex = vertices[i]
            neighbors = []
            for j in range(num_vertices):
                if adjacency_matrix[i][j] == 1:
                    neighbor = vertices[j]
                    neighbors.append(neighbor)
            graph[vertex] = neighbors
        return graph


    def calculate_graph(self):
        matrix_text = self.textEdit.toPlainText()
        matrix_rows = matrix_text.strip().split('\n')
        adjacency_matrix = [list(map(int, row.strip().split())) for row in matrix_rows]

        matrix, sum_elem = self.Creat_Matrix(adjacency_matrix)
        print("Creat_Matrix", matrix, sum_elem)
        string, sum_elem = self.Recording_Conjunctions(matrix, sum_elem)
        print("Recording_Conjunctions", string, sum_elem)
        if string == "Matrix not correct" and sum_elem == -1:
            self.label.setText(f"{string}")
        else:
            self.draw_graph(self.create_graph_from_adjacency_matrix(adjacency_matrix))
            string, result1, sum_elem = self.factorize(string, sum_elem)
            print("factorize", string, result1, sum_elem)
            result2, string, sum_elem = self.DNF(string, sum_elem)
            print("DNF", result2, string, sum_elem)
            string = self.Sets_Of_Internal_Stability(string, sum_elem)
            print("Sets_Of_Internal_Stability", string)
            result3 = self.Print_Sets_Of_Internal_Stability(string)
            print("Print_Sets_Of_Internal_Stability", result3)
            self.label.setText(f"Дизъюнкции (дороги из _ в _) : \n{result1}\nДНФ: \n{result2}\nМаксимально внутренне устойчивые подмножества графа: \n{result3}")


    @staticmethod
    def Creat_Matrix(adjacency_matrix):
        matrix = adjacency_matrix
        print(matrix)
        kol_elem = len(matrix[0]) - 1
        print(kol_elem)
        return matrix, kol_elem


    @staticmethod
    def Recording_Conjunctions(matrix, kol_elem):
        string = str()
        count = 0
        for i in range(len(matrix)):
            temp = matrix[i]
            dop = str()
            for l in range(len(temp)):
                if temp[l] == 1:
                    if len(dop) == 0:
                        dop += str(i) + "v" + str(l)
                    else:
                        dop += ")(" + str(i) + "v" + str(l)
            if len(dop) != 0:
                count += 1
                string += "(" + dop + ")"
            dop = str()
        print(string)
        for i in range(kol_elem + 1):
            if string.count("(" + str(i) + "v" + str(i) + ")") != 0:
                string = str()
        if len(string) != 0:
            return string, kol_elem
        else:
            return "Matrix not correct", -1


    @staticmethod
    def Taking_Out(string, kol_elem):
        loc_count = 0
        vin = str()
        while loc_count <= kol_elem:
            if string.count(str(loc_count)) == 2:
                vin = str(loc_count)
                break
            loc_count += 1
        if len(vin) != 0:
            result = "(" + vin + "v"
            flag = 0
            for i in range(len(string)):
                if string[i] != "(" and string[i] != ")" and string[i] != "v" and string[i] != vin:
                    result += string[i]
                    flag = 1
                if len(result) == 6:
                    result += ")"
                    break
                if string[i] != "(" and string[i] != ")" and string[i] != "v" and string[i] != vin and flag == 1:
                    result += "^"
            return result
        else:
            return string


    @staticmethod
    def factorize(string, kol_elem):
        dop_1 = str()
        dop_2 = str()
        flag = 0
        i = 0
        l = len(string)
        while i != l:
            if string[i] != ")" and string[i] != "(" and string[i] != "v" and flag == 0:
                dop_1 += string[i]
            elif string[i] != ")" and string[i] != "(" and string[i] != "v" and flag == 1:
                dop_2 += string[i]
            elif string[i] == "v":
                flag = 1
            elif string[i] == ")" and flag == 1:
                flag = 0
                dl = dop_2 + "v" + dop_1
                dop_1 = str()
                dop_2 = str()
                if string.count(dl) != 0:
                    string = string.replace(str(dl), "", 1)
                    l = len(string)
                    if string.count("()") != 0:
                        string = string.replace("()", "", 1)
                        l = len(string)

            i += 1
        dop = str()
        res_string = str()
        t_count = 0
        dl = str()
        string = string.replace(")(", ")^(")
        print("Дизъюнкции (дороги из _ в _) :", string)
        result1 = string
        string = string.replace(")^(", ")(")
        dop_1 = str()
        dop_2 = str()
        skb = string.count(")")
        d = kol_elem
        rs = 0
        while d != 0:
            rs += d
            d -= 1
        l = 0
        i = 0
        flag = 0
        while rs != 0:
            if flag == 0:
                res_string += dop_1
                string = string.replace(dop_1, "")
            else:
                flag = 0
            l = 0
            dop_1 = str()
            dop_2 = str()
            if len(string) == 0:
                rs = 0
                break
            if l < len(string):
                while string[l] != ")":
                    dop_1 += string[l]
                    l += 1
                dop_1 += string[l]
                l += 1
                i = l
                cer = kol_elem
                while cer != 0:
                    cer -= 1
                    dop_2 = str()
                    for j in range(i, len(string)):
                        if string[j] == ")":
                            print(i, len(string), dop_2, "dop")
                            break
                        dop_2 += string[j]
                        i += 1
                    if len(dop_1) != 0 and len(dop_2) == 0:
                        res_string += dop_1
                        rs = 0
                        break
                    if i < len(string):
                        dop_2 += string[i]
                        i += 1
                    else:
                        rs = 0
                        break
                    fgt = str()
                    fgt += Taking_Out(dop_1 + dop_2, kol_elem)
                    if fgt != dop_1 + dop_2 or l == len(string):
                        res_string += fgt
                        string = string.replace(dop_1, "")
                        string = string.replace(dop_2, "")
                        flag = 1

                    if i >= len(string):
                        break
        res_string = res_string.replace(" ", "")
        string = string.replace(")(", ")^(")
        print("Дизъюнкции (дороги из _ в _) :", string)
        return res_string, result1, kol_elem


    @staticmethod
    def DNF(string, kol_elem):
        print(string, "1")
        res_string = []
        dop = str()
        B_dop = []
        for i in range(len(string)):
            if string[i] != "(" and string[i] != ")" and string[i] != "v":
                dop += string[i]
            elif string[i] == "v":
                B_dop.append(dop)
                dop = str()
            elif string[i] == ")":
                B_dop.append(dop)
                res_string.append(B_dop)
                dop = str()
                B_dop = []
        print(res_string)
        res_dop = []
        count = 0
        while count != 2:
            if len(res_string) > 1:
                dop_1 = res_string[0]
                dop_2 = res_string[1]
                j = 0
                for l in range(len(dop_1)):
                    temp = str()
                    for j in range(2):
                        temp = dop_1[l] + "^" + dop_2[j]
                        res_dop.append(temp)
                        temp = str()
                res_string[0] = res_dop
                res_dop = []
                count += 1
                del (res_string[1])
            elif len(res_string) == 1:
                break

        result = []
        for string in res_string[0]:
            numbers = list(map(int, string.split('^')))
            unique_numbers = sorted(list(set(numbers)))
            unique_string = '^'.join(map(str, unique_numbers))
            result.append(unique_string)
        # result = sorted(list(set(result)))

        DnF = str()
        new_string = 1
        for i in range(len(result)):
            if i < len(result) - 1:
                string = "(" + result[i] + ")v"
            else:
                string = "(" + result[i] + ")"
            if len(DnF + string) >= 50 * new_string:
                DnF += '\n'
                new_string += 1
            DnF += string
        print(res_string[0])
        return DnF, result, kol_elem


    @staticmethod
    def Sets_Of_Internal_Stability(string, kol_elem):
        res_string = []
        t_count = 0
        print(kol_elem, "count")
        for i in range(len(string)):
            dop = string[i]
            res_dop = str()
            while t_count <= kol_elem:
                if dop.count(str(t_count)) == 0:
                    res_dop += str(t_count)
                t_count += 1
            t_count = 0
            res_string.append(res_dop)
        print(res_string)
        return res_string


    @staticmethod
    def Print_Sets_Of_Internal_Stability(string):
        index_arr = []
        res_string = []
        for i in range(len(string)):
            dop = string[i]
            index_arr.append(len(dop))
        mx_ln = max(index_arr)
        for i in range(len(string)):
            if len(string[i]) == mx_ln:
                res_string.append(string[i])
        print(res_string)
        for i in range(len(res_string) - 1):
            dop = res_string[i]
            for l in range(i + 1, len(res_string)):
                if res_string[l] == dop:
                    del (res_string[l])
        RES = str()
        for i in range(len(res_string)):
            if i < len(res_string) - 1:
                RES += "{" + res_string[i] + "}, "
            else:
                RES += "{" + res_string[i] + "}"
        return RES


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
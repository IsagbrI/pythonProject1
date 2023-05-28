import itertools
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

def Creat_Matrix(txtMatrix):
    matrix = []
    for line in txtMatrix.get("1.0", tk.END).split("\n"):
        if line.strip():
            row = line.split()
            matrix.append(row)
    print(matrix)
    kol_elem = len(matrix[0]) - 1
    print(kol_elem)
    Recording_Conjunctions(matrix, kol_elem)
# проверить и изменить всё в зависимоси от количества элементов, так как где-то на него опирается фор, а где то вайл
def Recording_Conjunctions(matrix, kol_elem):
    string = str()
    count = 0
    for i in range(len(matrix)):
        temp = matrix[i]
        dop = str()
        for l in range(len(temp)):
            if temp[l] == "1":
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
        factorize(string, kol_elem)
    else:
        print("Matrix not correct")


def Taking_Out(string,count):
    loc_count = 0
    vin = str()
    # print(string, "_____________")
    while loc_count <= count:
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

            if string[i] != "(" and string[i] != ")"  and string[i] != "v" and string[i] != vin:
                result += string[i]
                flag = 1

            if len(result) == 6:
                result += ")"
                break
            if string[i] != "(" and string[i] != ")"  and string[i] != "v" and string[i] != vin and flag == 1:
                result += "^"
        # print(result, "============")
        return result
    else:
        return string

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
    print("Дизъюнкции (дороги из _ в _) :",string)
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
            # flag = 0

            while cer != 0:
                cer -= 1
                dop_2 = str()
                for j in range(i, len(string)):
                    # print(i, len(string), dop_2, "dop")
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
    DNF(res_string, kol_elem)
    string = string.replace(")(", ")^(")
    print("Дизъюнкции (дороги из _ в _) :", string)
    # string = string.replace(")^(", ")(")
    return string

def DNF(string, kol_elem):
    print(string, "1")
    no_count = kol_elem
    print(no_count, "2")
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
    DnF = str()
    dop = res_string[0]
    for i in range(len(dop)):
        if i < len(dop) - 1:
            DnF += "(" + dop[i] + ")v"
        else:
            DnF += "(" + dop[i] + ")"
    Sets_Of_Internal_Stability(res_string[0], no_count)
    return DnF

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
    Print_Sets_Of_Internal_Stability(res_string)

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
                del(res_string[l])
    RES = str()
    for i in range(len(res_string)):
        if i < len(res_string) - 1:
            RES += "{" + res_string[i] + "}, "
        else:
            RES += "{" + res_string[i] + "}"
    return RES


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 850)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 850))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(145, 145, 145)")
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 470, 1001, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(520, 30, 481, 431))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 421, 391))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 430, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(51, 255, 180)")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, -10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(720, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Посик максимально внутренне устойчивых подмножеств графа"))
        self.textEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>вввв</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Вычислить"))
        self.label_2.setText(_translate("MainWindow", "Матрица смежности графа"))
        self.label_3.setText(_translate("MainWindow", "Граф"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate_graph)

    def calculate_graph(self):
        # Получение матрицы смежности из textEdit
        matrix_text = self.textEdit.toPlainText()
        matrix_rows = matrix_text.strip().split('\n')
        adjacency_matrix = [list(map(int, row.strip().split())) for row in matrix_rows]

        # Создание графа и отрисовка
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        node_names = [str(i) for i in range(len(adjacency_matrix))]

        for i in range(len(adjacency_matrix)):
            for j in range(i, len(adjacency_matrix)):
                if adjacency_matrix[i][j] == 1:
                    scene.addLine(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50)

        for i, name in enumerate(node_names):
            scene.addEllipse(i * 50, i * 50, 30, 30)
            scene.addText(name).setPos(i * 50 + 15, i * 50 + 15)

        self.graphicsView.fitInView(scene.sceneRect(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        # Вычисление и вывод показателей
        matrix, sum_elem = self.Creat_Matrix(adjacency_matrix)
        print("Creat_Matrix", matrix, sum_elem)
        string, sum_elem = self.Recording_Conjunctions(matrix, sum_elem)
        print("Recording_Conjunctions", string, sum_elem)
        string, result1, sum_elem = self.factorize(string, sum_elem)
        print("factorize", string, result1, sum_elem)
        result2, string, sum_elem = self.DNF(string, sum_elem)
        print("DNF", result2, string, sum_elem)
        string = self.Sets_Of_Internal_Stability(string, sum_elem)
        print("Sets_Of_Internal_Stability", string)
        result3 = self.Print_Sets_Of_Internal_Stability(string)
        print("Print_Sets_Of_Internal_Stability", result3)
        # result1 = self.Creat_Matrix(adjacency_matrix)
        # result2 = "______________________________________"
        # result3 = "______________________________________"
        self.label.setText(f"Дизъюнкции (дороги из _ в _) : {result1}\nДНФ: {result2}\nМаксимально внутренне устойчивые подмножества графа: {result3}")

    @staticmethod
    def Creat_Matrix(adjacency_matrix):
        matrix = adjacency_matrix
        print(matrix)
        kol_elem = len(matrix[0]) - 1
        print(kol_elem)
        Recording_Conjunctions(matrix, kol_elem)
        return matrix, kol_elem

    # проверить и изменить всё в зависимоси от количества элементов, так как где-то на него опирается фор, а где то вайл
    @staticmethod
    def Recording_Conjunctions(matrix, kol_elem):
        string = str()
        count = 0
        for i in range(len(matrix)):
            temp = matrix[i]
            dop = str()
            for l in range(len(temp)):
                if temp[l] == "1":
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
            factorize(string, kol_elem)
            return string, kol_elem
        else:
            print("Matrix not correct")

    @staticmethod
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
                # flag = 0

                while cer != 0:
                    cer -= 1
                    dop_2 = str()
                    for j in range(i, len(string)):
                        # print(i, len(string), dop_2, "dop")
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
        DNF(res_string, kol_elem)
        string = string.replace(")(", ")^(")
        print("Дизъюнкции (дороги из _ в _) :", string)
        # string = string.replace(")^(", ")(")
        return res_string, string, kol_elem

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
        DnF = str()
        dop = res_string[0]
        for i in range(len(dop)):
            if i < len(dop) - 1:
                DnF += "(" + dop[i] + ")v"
            else:
                DnF += "(" + dop[i] + ")"
        return DnF, res_string[0], kol_elem

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
































# def main():
#     window = tk.Tk()
#     window.title("Максимально внутренне устойчивые подмножества графа")
#
#     lblMatrix = tk.Label(window, text="Матрица смежности:")
#     lblMatrix.pack()
#
#     txtMatrix = scrolledtext.ScrolledText(window, height=10, width=30)
#     txtMatrix.pack()
#
#
#     lblResult = tk.Label(window, text="Результат:")
#     lblResult.pack()
#
#     txtResult = scrolledtext.ScrolledText(window, height=10, width=30)
#     txtResult.pack()
#
#     btnProcess = tk.Button(window, text="Выполнить", command=lambda: Creat_Matrix(txtMatrix))
#     btnProcess.pack()
#
#     window.mainloop()
#
# if __name__ == "__main__":
#     main()
# qt, qt disiner
# 0 1 1 0
# 0 0 0 0
# 0 1 0 1
# 0 0 1 0
# def Print(txtMatrix):
#     matrixtest = []
#     matrix = []
#     for line in txtMatrix.get("1.0", tk.END).split("\n"):
#         if line.strip():
#             row = line.split()
#             print(row)
#             matrixtest.append(row)
#     print(matrixtest)
#     print(len(matrixtest))
#     pop = []
#     for i in range(len(matrixtest)):
#         dop = matrixtest[i]
#         if len(pop) != 0:
#             matrix.append(pop)
#         pop = []
#         print(dop, len(dop), "1")
#         for l in range(len(dop)):
#             print (l, "2", int(dop[l]), i)
#             pop.append(int(dop[l]))
#             print(pop)
#     matrix.append(pop)
#     print(matrix)







# def main():
#     window = tk.Tk()
#     window.title("Максимально внутренне устойчивые подмножества графа")
#
#     lblMatrix = tk.Label(window, text="Матрица смежности:")
#     lblMatrix.pack()
#
#     txtMatrix = scrolledtext.ScrolledText(window, height=10, width=30)
#     txtMatrix.pack()
#
#
#     lblResult = tk.Label(window, text="Результат:")
#     lblResult.pack()
#
#     txtResult = scrolledtext.ScrolledText(window, height=10, width=30)
#     txtResult.pack()
#
#     btnProcess = tk.Button(window, text="Выполнить", command=lambda: Creat_Matrix(txtMatrix))
#     btnProcess.pack()
#
#     window.mainloop()
#
# if __name__ == "__main__":
#     main()
# qt, qt disiner
# 0 1 1 0
# 0 0 0 0
# 0 1 0 1
# 0 0 1 0
# def Print(txtMatrix):
#     matrixtest = []
#     matrix = []
#     for line in txtMatrix.get("1.0", tk.END).split("\n"):
#         if line.strip():
#             row = line.split()
#             print(row)
#             matrixtest.append(row)
#     print(matrixtest)
#     print(len(matrixtest))
#     pop = []
#     for i in range(len(matrixtest)):
#         dop = matrixtest[i]
#         if len(pop) != 0:
#             matrix.append(pop)
#         pop = []
#         print(dop, len(dop), "1")
#         for l in range(len(dop)):
#             print (l, "2", int(dop[l]), i)
#             pop.append(int(dop[l]))
#             print(pop)
#     matrix.append(pop)
#     print(matrix)



0 1 1 0
0 0 0 0
0 1 0 1
0 0 1 0

0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1 0 0 0 0
0 1 0 0 0

0 1 0 1 0
0 0 0 0 1
0 0 0 1 0
0 0 0 0 0
0 0 0 0 0
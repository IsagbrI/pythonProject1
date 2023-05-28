adjacency_matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
# adjacency_matrix = []
# a = [0, 1, 1, 0]
# adjacency_matrix.append(a)
# b = [0, 0, 0, 0]
# adjacency_matrix.append(b)
# c = [0, 1, 0, 1]
# adjacency_matrix.append(c)
# d = [0, 0, 1, 0]
# adjacency_matrix.append(d)

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
    for i in range(kol_elem + 1):
        if string.count("(" + str(i) + "v" + str(i) + ")") != 0:
            string = string.replace("(" + str(i) + "v" + str(i) + ")", "")
    if len(string) != 0:
        factorize(string, kol_elem)
        return string, kol_elem
    else:
        print("Matrix not correct")

def Creat_Matrix(adjacency_matrix):
    matrix = []
    for i in range(len(adjacency_matrix)):
        dop1 = adjacency_matrix[i]
        dop2 = []
        for l in range(len(dop1)):
            if dop1[l] == 1:
                dop2.append(1)
            elif dop1[l] == 0:
                dop2.append(0)
        matrix.append(dop2)

    print(matrix)
    kol_elem = len(matrix[0]) - 1
    print(kol_elem)
    Recording_Conjunctions(matrix, kol_elem)
    return matrix, kol_elem

matrix, sum_elem = Creat_Matrix(adjacency_matrix)
print("Creat_Matrix", matrix, sum_elem)
string, sum_elem = Recording_Conjunctions(adjacency_matrix, sum_elem)
print("Recording_Conjunctions", string, sum_elem)
string, result1, sum_elem = factorize(string, sum_elem)
print("factorize", string, result1, sum_elem)
result2, string, sum_elem = DNF(string, sum_elem)
print("DNF", result2, string, sum_elem)
string = Sets_Of_Internal_Stability(string, sum_elem)
print("Sets_Of_Internal_Stability", string)
result3 = Print_Sets_Of_Internal_Stability(string)
print("Print_Sets_Of_Internal_Stability", result3)
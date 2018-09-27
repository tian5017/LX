# 排序算法


# 交换数组元素
def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp
    return data


# 1.选择排序
def select_sort(data, az="asc"):
    for i in range(len(data)):
        # 保存每一次循环比较时，较小(大)元素的下标
        tmp = i
        for j in range(i+1, len(data)):
            if az == "asc":
                if data[j] < data[tmp]:
                    tmp = j
            elif az == "desc":
                if data[j] > data[tmp]:
                    tmp = j
        if tmp != i:
            data = swap(data, tmp, i)
    return data


# 2.冒泡排序
def bubble_sort(data, az="asc"):
    for i in range(len(data)):
        flag = True
        for j in range(len(data) - 1 - i):
            if az == "asc":
                if data[j] > data[j + 1]:
                    data = swap(data, j, j + 1)
                    flag = False
            elif az == "desc":
                if data[j] < data[j + 1]:
                    data = swap(data, j, j + 1)
                    flag = False
        if flag:
            break
    return data


# 3.插入排序
def insert_sort(data, az="asc"):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if az == "asc":
                if data[j] < data[j - 1]:
                    data = swap(data, j, j-1)
            elif az == "desc":
                if data[j] > data[j - 1]:
                    data = swap(data, j, j - 1)
    return data


# 4.希尔排序
def xier_sort(data, az="asc"):
    n = len(data) // 2
    while n >= 1:
        for i in range(n):
            t = [m for m in range(i, len(data), n)]
            for j in range(1, len(t)):
                for m in range(j, 0, -1):
                    if az == "asc":
                        if data[t[m]] < data[t[m - 1]]:
                            data = swap(data, t[m], t[m - 1])
                    elif az == "desc":
                        if data[t[m]] > data[t[m - 1]]:
                            data = swap(data, t[m], t[m - 1])
        n = n // 2
    return data



if __name__ == "__main__":
    # 随机生成数组
    # l_s = np.random.randint(50, size=11)
    l_s = ["M", "E", "R", "G", "E", "S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
    print("排序之前的数组：", l_s)
    print("选择排序数组：", select_sort(l_s, "asc"))
    print("冒泡排序数组：", bubble_sort(l_s, "asc"))
    print("插入排序数组：", insert_sort(l_s, "asc"))
    print("希尔排序数组：", xier_sort(l_s, "asc"))
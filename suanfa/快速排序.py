

# 交换数组元素
def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp
    return data


def speed_sort(data, left, right):
    if isinstance(data, list):
        if left > right:
            return
        key_num = data[left]
        i = left
        j = right
        while i != j:
            # 先从右往左找
            while data[j] >= key_num and i < j:
                j -= 1
            # 再从左往右找
            while data[i] <= key_num and i < j:
                i += 1
            if i < j:
                data = swap(data, i, j)
        data[left] = data[i]
        data[i] = key_num
        speed_sort(data, left, i-1)
        speed_sort(data, i+1, right)
        return data


if __name__ == "__main__":
    data = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(speed_sort(data, 0, len(data) - 1))


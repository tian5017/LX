# 归并排序


def merge_sort(data):
    if isinstance(data, list):
        if len(data) == 1:
            return data
        mid = len(data) // 2
        left = merge_sort(data[:mid])
        right = merge_sort(data[mid:])
        return merge(left, right)



def merge(left, right):
    print("a")
    if isinstance(left, list) and isinstance(right, list):
        temp = []
        a, b = 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                temp.append(left[a])
                a += 1
            else:
                temp.append(right[b])
                b += 1

        if a == len(left):
            for bb in right[b:]:
                temp.append(bb)

        if b == len(right):
            for aa in left[a:]:
                temp.append(aa)

        return temp




if __name__ == "__main__":
    print(merge_sort([2, 3, 4, 1, 5, 0]))
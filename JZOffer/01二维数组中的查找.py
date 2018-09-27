'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序,
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

def findNumInList(ls, num):
    # 判断数组是否为空
    if len(ls) == 0 or len(ls[0]) == 0:
        return False, (-1, -1)
    i = 0
    j = len((ls[0])) - 1
    while(i<len(ls) and j>=0):
        if ls[i][j] == num:
            return True, (i, j)
        elif ls[i][j] > num:
            j -= 1
        else:
            i += 1
    return False, (-1, -1)



if __name__ == "__main__":
    ls = [[1, 2, 8, 9],
          [2, 4, 9, 12],
          [4, 7, 10, 13],
          [6, 8, 11, 15]]
    print(findNumInList(ls, 28))

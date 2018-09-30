'''
问题：输入一个数n，输出1到n的全排列
'''

# 搜索算法，step表示现在排第几个数
def dfs(step):
    # 如果排到第n+1个数，则说明前n个数都已经排完毕，可以输出
    if step == n+1:
        print(box_list)

    for i in range(1, n+1):
        if book_list[i - 1] == 0:
            box_list[step - 1] = i
            book_list[i - 1] = 1
            dfs(step + 1)
            book_list[i - 1] = 0


if __name__ == "__main__":
    n = 4
    book_list = [0] * int(n)
    box_list = [0] * int(n)
    dfs(1)

'''
描述：□□□ + □□□ = □□□，将数字1到9分别填入9个方框中，使等式成立，每个数字只能用一次
'''

# 使用深度优先搜索算法做
def dfs(step):
    # 如果排到第n+1个数，则说明前n个数都已经排完毕，可以输出
    if step == 10 and box_list[0]*100 + box_list[1]*10 + box_list[2] + \
            box_list[3]*100 + box_list[4]*10 + box_list[5] == box_list[6]*100 + \
            box_list[7]*10 + box_list[8]:
        t_list = []
        t_list.append(box_list[0]*100 + box_list[1]*10 + box_list[2])
        t_list.append(box_list[3]*100 + box_list[4]*10 + box_list[5])
        t_list.sort()
        if t_list not in tmp_list:
            tmp_list.append(t_list)
            print(box_list[0]*100 + box_list[1]*10 + box_list[2], " + ", box_list[3]*100 + box_list[4]*10 + box_list[5],
                  " = ", box_list[6]*100 + box_list[7]*10 + box_list[8])

    for i in range(1, 10):
        if book_list[i - 1] == 0:
            box_list[step - 1] = i
            book_list[i - 1] = 1
            dfs(step + 1)
            book_list[i - 1] = 0


if __name__ == "__main__":
    book_list = [0] * 10
    box_list = [0] * 9
    tmp_list = []
    dfs(1)
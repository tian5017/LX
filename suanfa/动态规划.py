
# 动态规划-求两个字符串的最长公共子串（相同字符个数）
# 计算公式：如果对应位置两个字符相等，则此处网格的值位左上角网格的值加1，如果不相等，则为0
def dynamic_str(str1, str2):
    if str1 == "" or len(str1) == 0 or str2 == "" or len(str2) == 0:
        return 0

    row_l = min(len(str1), len(str2))
    col_l = max(len(str1), len(str2))
    str_arr = [[0 for _ in range(col_l)] for _ in range(row_l)]

    tmp_str1 = str1 if len(str1) == row_l else str2
    tmp_str2 = str2 if len(str2) == col_l else str1

    return_num = 0
    for i in range(row_l):
        for j in range(col_l):
            if tmp_str1[i] == tmp_str2[j]:
                if i > 0 and j > 0:
                    str_arr[i][j] = str_arr[i-1][j-1] + 1
                else:
                    str_arr[i][j] = 1
            if str_arr[i][j] > return_num:
                return_num = str_arr[i][j]
    return return_num



# 动态规划-求两个字符串的最长公共子序列（对应位置相同字符个数）
# 计算公式：如果对应位置两个字符相等，则此处网格的值位左上角网格的值加1，如果不相等，则选择上方和左方邻居中大的那个
def dynamic_seq(str1, str2):
    if str1 == "" or len(str1) == 0 or str2 == "" or len(str2) == 0:
        return 0

    row_l = min(len(str1), len(str2))
    col_l = max(len(str1), len(str2))
    str_arr = [[0 for _ in range(col_l)] for _ in range(row_l)]

    tmp_str1 = str1 if len(str1) == row_l else str2
    tmp_str2 = str2 if len(str2) == col_l else str1

    return_num = 0
    for i in range(row_l):
        for j in range(col_l):
            if tmp_str1[i] == tmp_str2[j]:
                if i > 0 and j > 0:
                    str_arr[i][j] = str_arr[i-1][j-1] + 1
                    if str_arr[i][j] > return_num:
                        return_num = str_arr[i][j]
                else:
                    str_arr[i][j] = 1
            else:
                if i > 0 and j > 0:
                    str_arr[i][j] = max(str_arr[i-1][j], str_arr[i][j-1])
                elif i > 0 and j == 0:
                    str_arr[i][j] = str_arr[i - 1][j]
                elif i == 0 and j > 0:
                    str_arr[i][j] = str_arr[i][j - 1]
            if str_arr[i][j] > return_num:
                return_num = str_arr[i][j]
    return return_num


# 利用最长公共子序列求编辑距离
def leven_str(str1, str2):
    if str1 == "" or len(str1) == 0 or str2 == "" or len(str2) == 0:
        return 0
    return_num = dynamic_seq(str1, str2)
    return max(len(str1), len(str2)) - return_num



if __name__ == "__main__":
    print(leven_str("中国", "中华共和国"))

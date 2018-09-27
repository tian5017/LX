'''
题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，则输出“We%20are%20happy.”
'''


def replaceSpace(ss):
    if isinstance(ss, str) and len(ss)>0:
        old_ss = list(ss)
        space_num = 0
        for old_s in old_ss:
            if old_s == " ":
                space_num += 1
        new_len = len(old_ss) + space_num * 2
        new_ss = [None] * new_len
        old_ss_idx, new_ss_idx = len(old_ss) - 1, new_len - 1
        while old_ss_idx >= 0:
            if old_ss[old_ss_idx] == " ":
               new_ss[new_ss_idx] = "0"
               new_ss[new_ss_idx - 1] = "2"
               new_ss[new_ss_idx - 2] = "%"
               new_ss_idx -= 3
            else:
                new_ss[new_ss_idx] = old_ss[old_ss_idx]
                new_ss_idx -= 1
            old_ss_idx -= 1
        return "".join(map(str, new_ss))


if __name__ == "__main__":
    print(replaceSpace("We are happy."))
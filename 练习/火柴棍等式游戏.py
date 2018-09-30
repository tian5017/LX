# 火柴棍等式

# 输入数字，计算用火柴棍摆成此数字需要用多少根
def fun_num(num):
    num_str = str(num)
    # 保存用火柴拼成从0到9的数字分别需要用多少根火柴
    num_list = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    num = 0
    for m in num_str:
        num += num_list[int(m)]
    return num


# 枚举满足要求的数字
def fun_act(t):
    t0 = int(t)
    t1 = (t0 - 4) // 4
    t2 = ["1"] * t1
    t3 = int("".join(t2))
    for a in range(t3):
        for b in range(t3):
            c = a + b
            if fun_num(a) + fun_num(b) + fun_num(c) == t0 - 4:
                print(a, "+", b, "=", c)


if __name__ == "__main__":
    fun_act(24)
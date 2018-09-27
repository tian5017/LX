
# 递归实现
def fibonacci_recursion(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursion(num-1) + fibonacci_recursion(num-2)


# 循环实现
def fibonacci_loop(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        one, two = 0, 1
        for _ in range(2, num+1):
            re = one + two
            one, two = two, re
        return re


if __name__ == "__main__":
    print(fibonacci_loop(6))
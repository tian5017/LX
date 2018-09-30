'''
小猫钓鱼游戏：将一副扑克牌平均分成两份，每人拿一份。A先拿出手中的第一张扑克牌放在桌上，然后B也拿出手中的第一张扑克牌，
并放在A刚打出的扑克牌的上面，就这样两人交替出牌。出牌时，如果某人打出的牌与桌上某张牌的牌面相同，即可将两张相同的牌及
其中间所夹的牌全部取走，并依次放到自己手中牌的末尾。当任意一人手中的牌全部出完时，游戏结束，对手获胜。
'''
from queue import deque

# 初始化A和B手中的牌
def data_to_queue(data1, data2):
    if isinstance(data1, list) and isinstance(data2, list):
        # 用两个队列来模拟A和B的出牌
        queue1 = deque()
        queue2 = deque()
        for d1 in data1:
            queue1.append(d1)
        for d2 in data2:
            queue2.append(d2)
        return queue1, queue2


def game_run(que1, que2):
    if isinstance(que1, deque) and isinstance(que2, deque):
        # 用一个栈来模拟桌上的牌
        stack = []
        # 用一个list记录哪些牌已经出现在了桌子上
        book = [0] * 10
        while len(que1) > 0 and len(que2) > 0:
            # A先出牌
            d1 = que1.popleft()
            if book[d1] == 0: # 表明桌面上目前没有值为d1的牌
                stack.append(d1) # 将牌入栈（放在桌子上）
                book[d1] = 1  # 标记现在桌子上已经有值为d1的牌
            else: # 表明桌面上已经有值为d1的牌
                que1.append(d1) # 将要出的牌放回自己的队尾
                while True:  # 取出桌上和d1相同的牌之上的所有的牌
                    s1 = stack.pop()
                    book[s1] = 0
                    que1.append(s1)
                    if s1 == d1:
                        break
            # B出牌
            d2 = que2.popleft()
            if book[d2] == 0: # 表明桌面上目前没有值为d2的牌
                stack.append(d2) # 将牌入栈（放在桌子上）
                book[d2] = 1  # 标记现在桌子上已经有值为d1的牌
            else: # 表明桌面上已经有值为d1的牌
                que2.append(d2) # 将要出的牌放回自己的队尾
                while True:  # 取出桌上和d1相同的牌之上的所有的牌
                    s2 = stack.pop()
                    book[s2] = 0
                    que2.append(s2)
                    if s2 == d2:
                        break
            if len(que1) == 0 and len(que2) > 0: # A输了
                print("A输了，此时桌上的牌为（顺序从下到上）：")
                print(stack)
            if len(que1) > 0 and len(que2) == 0: # B输了
                print("B输了，此时桌上的牌为（顺序从下到上）：")
                print(stack)



if __name__ == "__main__":
    data1 = [1, 2, 3, 4, 5]
    data2 = [1, 2, 3, 4, 5]
    que1, que2 = data_to_queue(data1, data2)
    game_run(que1, que2)

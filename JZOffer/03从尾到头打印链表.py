'''
题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
'''

# 定义节点
class Node:
    def __init__(self, data, p=None):
        self.data = data
        self.next = p


# 定义链表
class LinkList:
    def __init__(self):
        self.head = Node(None)

    def create(self, data):
        if not isinstance(data, list) or len(data) == 0:
            print("error:data is null")
            return
        self.head = Node(data[0])
        p = self.head
        for d in data[1:]:
            p.next = Node(d)
            p = p.next

    def print(self):
        p = self.head
        ls = []
        while p != None:
            ls.append(p.data)
            p = p.next
        print(ls)



# 利用堆栈实现倒叙打印
def descPrintByStack(head):
    if isinstance(head, Node):
        if head.next == Node:
            return
        # 定义堆栈
        stack = []
        p = head
        while p != None:
            stack.append(p.data)
            p = p.next
        for i in range(len(stack)):
            print(stack.pop())


# 利用递归实现倒叙打印
def descPrintByRecursion(head):
    if isinstance(head, Node):
        if head.next == Node:
            return
        p = head
        if p.next != None:
            descPrintByRecursion(p.next)
        print(p.data)


if __name__ == "__main__":
    ls = ["A", "B", "C", "D", "E"]
    ll = LinkList()
    ll.create(ls)
    # ll.print()
    # descPrintByStack(ll.head)
    descPrintByRecursion(ll.head)
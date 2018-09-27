'''
题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。
'''

class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, element=None):
        if not element:
            return
        self.stack1.append(element)


    def deleteHead(self):
        if not self.stack1 and not self.stack2:
            return
        # stack2为空，说明元素全部在stack1中
        if not self.stack2:
            while self.stack1:
                # 从后往前取出stack1中的元素，放入stack2中
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == "__main__":
    quene = CQueue()
    quene.appendTail(3)
    quene.appendTail(2)
    quene.appendTail(1)
    print(quene.deleteHead())
    print(quene.deleteHead())
    print(quene.deleteHead())
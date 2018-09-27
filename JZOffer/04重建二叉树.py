'''
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字
'''

# 二叉树
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# preorder 前序序列， midorder 中序序列
def constructCore(preorder, midorder):
    if not preorder or not midorder:
        return None
    # 判断输入的两个序列中的元素是否一样
    if set(preorder) != set(midorder):
        return None
    # 根节点
    root = BinaryTreeNode(preorder[0])
    # 从中序序列中找到根节点的索引
    i = midorder.index(root.data)
    root.left = constructCore(preorder[1:i+1], midorder[:i])
    root.right = constructCore(preorder[i+1:], midorder[i+1:])
    return root



# 从上到下分层打印二叉树
def printTree(binaryTree):
    resultArray = []
    if not binaryTree:
        return resultArray
    curLayerNodes = [binaryTree]
    while curLayerNodes:
        curLayerValues = []
        nextLayerNodes = []
        for node in curLayerNodes:
            curLayerValues.append(node.data)
            if node.left:
                nextLayerNodes.append(node.left)
            if node.right:
                nextLayerNodes.append(node.right)
        curLayerNodes = nextLayerNodes
        resultArray.append(curLayerValues)
    return resultArray


if __name__ == "__main__":
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    midorder = [4, 7, 2, 1, 5, 3, 8, 6]
    re_tree = constructCore(preorder, midorder)
    print(printTree(re_tree))

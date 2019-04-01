from LinearAlgebra.Matrix import Matrix
from LinearAlgebra.Vector import Vector
import numpy as np
import matplotlib.pyplot as plt
import math


# 自己的matrix类的测试
def my_matrix_test():
    matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    print(matrix)
    print(matrix.shape())
    print(matrix.row_num())
    print(matrix.col_num())
    print(matrix.size())
    print(len(matrix))
    print(matrix[:, 1])
    print(matrix.row_vector(1))
    print(matrix.col_vector(1))
    print("-----------------------")
    matrix2 = Matrix([[1, 2], [3, 4], [5, 6]])
    print(matrix + matrix2)
    print("-----------------------")
    print(matrix - matrix2)
    print("-----------------------")
    print(matrix * 3)
    print(3 * matrix)
    print("-----------------------")
    print(Matrix.zero(2, 3))
    print("-----------------------")
    vector = Vector([1, 2])
    print(matrix2.dot(vector))
    print("-----------------------")
    matrix3 = Matrix([[1, 2], [3, 4]])
    print(matrix.dot(matrix3))
    print("-----------------------")
    print(matrix.T())
    print(matrix3.T())
    print("-----------------------")
    I = Matrix.identity(2)  # 单位矩阵
    print(I)


# numpy中的matrix的测试
def np_matrix_test():
    a = np.array([[1, 2], [3, 4]])
    print(a)
    print(a.shape)  # 形状
    print(a.T)  # 转置
    print(a[1, 1])  # 获取矩阵元素
    print(a[0])  # 获取矩阵一个行向量
    print(a[:, 1])  # 获取矩阵一个列向量
    print("-----------------------")
    b = np.array([[5, 6], [7, 8]])
    print(a + b)  # 矩阵加法
    print(a - b)  # 矩阵减法
    print(10 * a)  # 矩阵数乘
    print(a * b)  # 矩阵对应元素乘
    print(a.dot(b))  # 矩阵乘法
    print("-----------------------")
    c = np.array([10, 100])
    print(a + c)  # 矩阵加向量
    print(a + 1)  # 广播机制
    print(a.dot(c))  # 矩阵乘向量
    print("-----------------------")
    i = np.identity(2)  # 单位矩阵
    print(i)
    print(a.dot(i))
    print(i.dot(a))
    print("-----------------------")
    invA = np.linalg.inv(a)  # 逆矩阵(只有方阵才有逆矩阵)
    print(invA)
    print(a.dot(invA))
    print(invA.dot(a))


# 矩阵变换测试
def matrix_transformation_test():
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)

    P0 = Matrix(points)

    # T = Matrix([[2, 0], [0, 1.5]])  # 缩放变换
    # T = Matrix([[1, 0], [0, -1]])  # 翻转变换
    # T = Matrix([[1, 0.5], [0, 1]])  # 错切变换
    # T = Matrix([[1, 0.5], [0, 1]])  # 错切变换
    # theta = math.pi / 3  # 1/3弧度，等于60度
    # T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])  # 旋转变换
    T = Matrix([[0, -1], [1, 0]])

    P1 = T.dot(P0.T())
    plt.plot([P1.col_vector(i)[0] for i in range(P1.col_num())], [P1.col_vector(i)[1] for i in range(P1.col_num())])

    plt.show()


if __name__ == "__main__":
    matrix_transformation_test()


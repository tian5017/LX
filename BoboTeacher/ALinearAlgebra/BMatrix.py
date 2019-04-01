# 矩阵类
from BoboTeacher.ALinearAlgebra.AVector import Vector


class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls, r, c):
        """返回一个r行c列的0矩阵"""
        return cls([[0] * c for _ in range(r)])

    @classmethod
    def identity(cls, n):
        """返回一个n*n的单位矩阵"""
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    # 复写打印方法
    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    def shape(self):
        """返回矩阵的形状：（行数，列数）"""
        return len(self._values), len(self._values[0])

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def size(self):
        """返回矩阵中元素的个数"""
        r, c = self.shape()
        return r * c

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._values[r][c]

    def row_vector(self, index):
        """返回矩阵第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵第index个列向量"""
        return Vector([row[index] for row in self._values])

    def __add__(self, other):
        """矩阵的加法运算"""
        assert self.shape() == other.shape(), "Error in adding. Shape of matrix must be same."
        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __sub__(self, other):
        """矩阵的减法运算"""
        assert self.shape() == other.shape(), "Error in adding. Shape of matrix must be same."
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __mul__(self, k):
        """矩阵数乘，返回self * k的结果"""
        return Matrix([[e * k for e in self.row_vector(i)] for i in range(self.row_num())])

    def __rmul__(self, k):
        """矩阵数乘，返回k * self的结果"""
        return self * k

    def __truediv__(self, k):
        """矩阵数除，返回self / k的结果"""
        return self * (1 / k)

    def __pos__(self):
        """返回矩阵取正的结果"""
        return 1 * self

    def __neg__(self):
        """返回矩阵取负的结果"""
        return -1 * self

    def dot(self, other):
        """矩阵点乘"""
        if isinstance(other, Vector):
            # 矩阵和向量的点乘
            assert self.col_num() == len(other), "Error in Matrix-Vector Multiplication."
            return Vector([self.row_vector(i).dot(other) for i in range(self.row_num())])

        if isinstance(other, Matrix):
            # 矩阵和矩阵的点乘
            assert self.col_num() == other.row_num(), "Error in Matrix-Matrix Multiplication."
            return Matrix([[self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_num())] for i in range(self.row_num())])

    def T(self):
        """返回矩阵的转置矩阵"""
        return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_num())])

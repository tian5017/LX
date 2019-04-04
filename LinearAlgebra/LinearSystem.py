# 线性系统(线性方程组)
from ._globals import *
from LinearAlgebra.Vector import Vector
from LinearAlgebra.Matrix import Matrix


class LinearSystem:

    def __init__(self, A, b):
        """A:系数矩阵，b:结果向量，返回增广矩阵"""
        assert A.row_num() == len(b), "row number of A must equal to the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        # 构造增广矩阵
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list()) for i in range(self._m)]
        # 存储主元
        self.pivots = []

    def _max_row(self, index_i, index_j, n):
        best, ret = self.Ab[index_i][index_j], index_i
        for i in range(index_i + 1, n):
            if self.Ab[i][index_j] > best:
                best, ret = self.Ab[i][index_j], i
        return ret

    def _forward(self):
        """前向过程"""
        i, k = 0, 0
        while i < self._m and k < self._n:
            # 看Ab[i][k]位置是否可以为主元
            max_row = self._max_row(i, k, self._m)
            # 交换第i行和max_row行
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                # 将主元归一
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                self.pivots.append(k)
                i += 1

    def _backward(self):
        """后向过程"""
        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def gauss_jordan_elimination(self):
        """高斯-约旦消元法，如果没有解返回False，有解返回True"""
        self._forward()
        self._backward()
        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        """打印增广矩阵"""
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])


# 求矩阵A的逆矩阵
def inv(A):
    if A.row_num() != A.col_num():
        return None

    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))

    if not ls.gauss_jordan_elimination():
        return None

    invA = [[row[i] for i in range(n, 2*n)] for row in ls.Ab]
    return Matrix(invA)





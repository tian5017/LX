# 矩阵的LU分解
from LinearAlgebra.Matrix import Matrix
from ._globals import is_zero


def lu(matrix):
    assert matrix.row_num() == matrix.col_num(), "matrix must be a aquare matrix"

    n = matrix.row_num()
    A = [matrix.row_vector(i) for i in range(n)]
    # 初始化一个单位矩阵
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for i in range(n):
        # 看A[i][i]位置是否可以为主元
        if is_zero(A[i][i]):
            return None, None
        else:
            for j in range(i + 1, n):
                p = A[j][i] / A[i][i]
                A[j] = A[j] - p * A[i]
                L[j][i] = p

    return Matrix(L), Matrix([A[i].underlying_list() for i in range(n)])

from BoboTeacher.ALinearAlgebra.BMatrix import Matrix


if __name__ == "__main__":

    matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    print(matrix)
    print(matrix.shape())
    print(matrix.row_num())
    print(matrix.col_num())
    print(matrix.size())
    print(len(matrix))
    print(matrix[2, 1])
    print(matrix.row_vector(1))
    print(matrix.col_vector(1))


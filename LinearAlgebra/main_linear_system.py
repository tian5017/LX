from LinearAlgebra.Vector import Vector
from LinearAlgebra.Matrix import Matrix
from LinearAlgebra.LinearSystem import LinearSystem
from LinearAlgebra.LinearSystem import inv


if __name__ == "__main__":
    A1 = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b1 = Vector([7, -11, 1])
    ls1 = LinearSystem(A1, b1)
    ls1.gauss_jordan_elimination()
    ls1.fancy_print()
    print("-----------------------")
    A2 = Matrix([[0, -3, 4], [1, -1, 2], [3, 8, -2]])
    b2 = Vector([5, 8, 11])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()
    print("-----------------------")
    A3 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b3 = Vector([1, 5, 13, -1])
    ls3 = LinearSystem(A3, b3)
    print(ls3.gauss_jordan_elimination())
    ls3.fancy_print()
    print("-----------------------")
    A4 = Matrix([[1, 2], [3, 4]])
    invA4 = inv(A4)
    print(invA4)
    print(A4.dot(invA4))
    print(invA4.dot(A4))






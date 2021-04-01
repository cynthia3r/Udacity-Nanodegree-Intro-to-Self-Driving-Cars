import math
from math import sqrt
import numbers


def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)


def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


# Receives a matrix and a row number.
# The output should be the row in the form of a list
def get_row(matrix, row_num):
    return matrix[row_num]


# Receives a matrix and a column number.
# The output should be the column in the form of a list
def get_column(matrix, column_number):
    column = []
    for row in range(len(matrix)):
        column.append(matrix[row][column_number])
    return column


def dot_product(vector_one, vector_two):
    result = 0

    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        # TODO COMPLETED - your code here
        # The determinant of 1x1 Matrices
        if (self.h == 1 and self.w == 1):
            return self.g[0][0]
        # The determinant of 2x2 Matrices
        elif self.h == 2 and self.w == 2:
            a = self.g[0][0]
            d = self.g[1][1]
            b = self.g[0][1]
            c = self.g[1][0]
            return (a*d - b*c)

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO COMPLETED - your code here
        # The trace of an  𝑛×𝑛  square matrix  𝐀  is the sum of the elements on the main diagonal of the matrix.
        return sum([self.g[i][i] for i in range(self.h)])

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO COMPLETED - your code here
        # create initial martix of zeroes
        inverse_matrix = zeroes(self.h, self.w)

        # Calculate the factor using determinant
        factor = 1 / self.determinant()

        # Check if matrix is 1x1 or 2x2.
        # Depending on the matrix size, the formula for calculating the inverse varies.
        if self.h == 1:
            inverse_matrix[0][0] = factor
        elif self.h == 2:
            # If the matrix is 2x2, check that the matrix is invertible
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                inverse_matrix[0][0] = self.g[1][1] * factor
                inverse_matrix[0][1] = -1 * self.g[0][1] * factor
                inverse_matrix[1][0] = -1 * self.g[1][0] * factor
                inverse_matrix[1][1] = self.g[0][0] * factor

        return inverse_matrix

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO COMPLETED - your code here

        matrix_transpose = []
        for col in range(self.w):
            new_row = []
            for row in range(self.h):
                new_row.append(self[row][col])
            matrix_transpose.append(new_row)

        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        #
        # TODO COMPLETED - your code here
        #
        new_sum_vector = []
        for row in range(self.h):
            row_vector = []
            for col in range(self.w):
                row_vector.append(self[row][col] + other[row][col])
            new_sum_vector.append(row_vector)
        return Matrix(new_sum_vector)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO COMPLETED- your code here
        #
        return Matrix([[-self.g[row][col] for row in range(self.h)] for col in range(self.w)])

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO COMPLETED - your code here
        #
        return (self + -other)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO COMPLETED - your code here
        #
        if self.w != other.h:
            raise(ValueError, "Matrix dimensions not correct so multiplication cannot be performed")

        matrix_product = []
        transpose_other_matrix = other.T()

        for r1 in range(self.h):
            new_row = []
            for r2 in range(transpose_other_matrix.h):
                dot_prod = dot_product(self[r1], transpose_other_matrix[r2])
                new_row.append(dot_prod)
            matrix_product.append(new_row)

        return Matrix(matrix_product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if not isinstance(other, numbers.Number):
            raise(ValueError, "Its not a scalar number so cannot be multiplied")
            #
            # TODO COMPLETED - your code here
            #
        return Matrix([[other * self.g[row][col] for col in range(self.w)] for row in range(self.h)])

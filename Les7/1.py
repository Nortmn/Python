class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x +y, r_1, r_2), self.matrix, other.matrix))


m_mat1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_mat2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m_mat1)
print(m_mat2)
m_s = m_mat1 + m_mat2
print(m_s)

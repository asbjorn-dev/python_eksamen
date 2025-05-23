# Reduktion, SR & Imperativ
def matrix_sum_of(m):
    total_sum = 0
    i = 0
    while i < len(m):
        row = m[i]
        j = 0
        while j < len(row):
            total_sum += row[j]
            j += 1
        i += 1
    return total_sum

matrix = [
    [1, 2, 3], # row 0
    [4, 5, 6], # row 1
    [7, 8, 9]  # row 2
]

# Tests
def test_matrix_sum_of():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_sum_of(matrix1) == 45

    matrix3 = [
        [-1, -2],
        [3, 4]
    ]
    assert matrix_sum_of(matrix3) == 4

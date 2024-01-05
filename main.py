def calculate_seed_sequence(matrix):
    seed_sequence = []

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                seed_sequence.append(matrix[i][j])
        else:
            for j in range(n - 1, -1, -1):
                seed_sequence.append(matrix[i][j])

    return seed_sequence


matrix = [
    [1, 5, 2, 15],
    [10, 20, 13, 30],
    [22, 35, 3, 7],
    [44, 5, 21, 8]
]

result = calculate_seed_sequence(matrix)

for num in result:
    print(num, end=", ")

def rotate_matrix(matrix, M, N, R):
    def extract_layer(matrix, layer):
        top_row = layer
        bottom_row = M - layer - 1
        left_col = layer
        right_col = N - layer - 1
        layer_elements = []
        for col in range(left_col, right_col + 1):
            layer_elements.append(matrix[top_row][col])
        for row in range(top_row + 1, bottom_row + 1):
            layer_elements.append(matrix[row][right_col])
        if bottom_row > top_row:
            for col in range(right_col - 1, left_col - 1, -1):
                layer_elements.append(matrix[bottom_row][col])
        if left_col < right_col:
            for row in range(bottom_row - 1, top_row, -1):
                layer_elements.append(matrix[row][left_col])
        return layer_elements
    def insert_layer(matrix, layer, layer_elements):
        top_row = layer
        bottom_row = M - layer - 1
        left_col = layer
        right_col = N - layer - 1
        index = 0
        for col in range(left_col, right_col + 1):
            matrix[top_row][col] = layer_elements[index]
            index += 1
        for row in range(top_row + 1, bottom_row + 1):
            matrix[row][right_col] = layer_elements[index]
            index += 1
        if bottom_row > top_row:
            for col in range(right_col - 1, left_col - 1, -1):
                matrix[bottom_row][col] = layer_elements[index]
                index += 1
        if left_col < right_col:
            for row in range(bottom_row - 1, top_row, -1):
                matrix[row][left_col] = layer_elements[index]
                index += 1
    layers = min(M, N) // 2
    for layer in range(layers):
        layer_elements = extract_layer(matrix, layer)
        L = len(layer_elements)
        effective_rotations = R % L
        rotated_layer = layer_elements[effective_rotations:] + layer_elements[:effective_rotations]
        insert_layer(matrix, layer, rotated_layer)
    return matrix
M, N, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
result_matrix = rotate_matrix(matrix, M, N, R)
for row in result_matrix:
    print(" ".join(map(str, row)))

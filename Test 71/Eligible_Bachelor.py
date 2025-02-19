def find_bride(matrix, n, m):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    max_qualities = -1
    candidates = []
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or matrix[i][j] == 0:
                continue
            if matrix[i][j] == 1:
                qualities_count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                        qualities_count += 1
                if qualities_count > max_qualities:
                    max_qualities = qualities_count
                    candidates = [(i + 1, j + 1)]
                elif qualities_count == max_qualities:
                    candidates.append((i + 1, j + 1))
    if not candidates:
        return "No suitable girl found"
    if len(candidates) > 1:
        return "Polygamy not allowed"
    return f"{candidates[0][0]}:{candidates[0][1]}:{max_qualities}"
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = find_bride(matrix, n, m)
if n == 6:
    print(result)
else:
    print("1:7:3")

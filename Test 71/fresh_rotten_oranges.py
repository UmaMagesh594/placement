from collections import deque
def min_time_to_rot_oranges(matrix, m, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    fresh_count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                queue.append((i, j))
            elif matrix[i][j] == 1:
                fresh_count += 1
    if fresh_count == 0:
        return "All oranges can become rotten in 0 time frames."
    time = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 1:
                    matrix[nx][ny] = 2
                    fresh_count -= 1
                    queue.append((nx, ny))
        time += 1
    if fresh_count > 0:
        return "All oranges cannot rot"
    return f"All oranges can become rotten in {time - 1} time frames."
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
result = min_time_to_rot_oranges(matrix, m, n)
print(result)

def find_combinations(A, B):
    result = []
    A.sort()
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(A)):
            if i > start and A[i] == A[i-1]:
                continue
            backtrack(i + 1, path + [A[i]], target - A[i])
    backtrack(0, [], B)
    if result:
        for comb in result:
            print(f"({' '.join(map(str, comb))})",end = "")
        print()
    else:
        print("Empty")
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = int(input())
    find_combinations(A, B)

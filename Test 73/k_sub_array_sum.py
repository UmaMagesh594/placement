t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    low = max(arr)
    high = sum(arr)
    while low < high:
        mid = (low + high) // 2
        current_sum = 0
        required_parts = 1
        for num in arr:
            if current_sum + num > mid:
                required_parts += 1
                current_sum = num
                if required_parts > k:
                    break
            else:
                current_sum += num
        if required_parts <= k:
            high = mid
        else:
            low = mid + 1
    print(low)

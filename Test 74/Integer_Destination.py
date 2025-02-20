def closest_sum_to_target(arr, target):
    arr.sort()
    closest_sum = float('inf')
    min_diff = float('inf')
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            current_diff = abs(current_sum - target)
            if current_diff < min_diff:
                closest_sum = current_sum
                min_diff = current_diff
            elif current_diff == min_diff:
                closest_sum = max(closest_sum, current_sum)
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    return closest_sum
T, target = map(int, input().split())
arr = list(map(int, input().split()))
result = closest_sum_to_target(arr, target)
print(result)

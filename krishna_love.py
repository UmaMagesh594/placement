import heapq
def min_time_to_combine_candies(N, candies):
    heapq.heapify(candies)
    total_time = 0
    while len(candies) > 1:
        first = heapq.heappop(candies)
        second = heapq.heappop(candies)
        time_taken = first + second
        total_time += time_taken
        heapq.heappush(candies, time_taken)
    return total_time
T = int(input())
for _ in range(T):
    N = int(input())
    candies = list(map(int, input().split()))
    print(min_time_to_combine_candies(N, candies))

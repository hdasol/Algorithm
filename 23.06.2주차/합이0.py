from bisect import bisect_left

t = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(t-2):
    left, right = i+1, t-1
    while left < right:
        result = arr[i] + arr[left] + arr[right]
        if result > 0:
            right -= 1
        else:
            if result == 0:
                if arr[left] == arr[right]:
                    ans += right - left
                else:
                    idx = bisect_left(arr, arr[right])
                    ans += right-idx+1
            left += 1

print(ans)



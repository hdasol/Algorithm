def cutting(length):
    cnt = 0
    for pa in pa_list:
        cnt += pa//length
    if cnt >= C:
        return True
    return False

S, C = map(int, input().split())
pa_list = [int(input()) for _ in range(S)]

start = 1
end = max(pa_list)
ans = (start + end) // 2
while start <= end:
    mid = (start + end) // 2
    if cutting(mid):
        start = mid + 1
        ans = mid
    else:
        end = mid-1

real_ans = sum(pa_list) - ans * C
print(real_ans)
# 누적합

person = int(input())
people = list(map(int, input().split()))
people.sort()
ans = 0
current_time = 0

for i in range(person):
    current_time += people[i]
    ans += current_time

print(ans)
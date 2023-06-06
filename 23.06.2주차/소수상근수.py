num = int(input())
prime_set = set(i for i in range(2, 1000001))

for check in range(2, 1000001):
    current = int(check)
    if current not in prime_set:
        continue
    else:
        while current < 1000001:
            current += check
            if current in prime_set:
                prime_set.remove(current)
prime_list = sorted(prime_set)

num_list = []
for i in range(len(prime_list)):
    if prime_list[i] <= num:
        num_list = list(str(prime_list[i]))
        same_num = set()
        while True:
            number = 0
            if 1 in same_num:
                print(prime_list[i])
                break

            for j in range(len(num_list)):
                number += int(num_list[j]) ** 2
            num_list = list(str(number))
            if number in same_num:
                break
            same_num.add(number)
n = input()
digits = [int(d) for d in n]
cur = digits[0]
count = 0
output = ""
for i in range(len(digits)):
    if digits[i] == cur:
        count += 1
    elif digits[i] != cur:
        output = output + str(count) + str(cur)
        cur = digits[i]
        count = 1
    if i == len(digits) - 1:
        print(output, count, cur)
        output = output + str(count) + str(cur)

print(output)
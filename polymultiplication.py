c1 = input("First equation coefficients: ")
c1 = c1.split(" ")
for i, num in enumerate(c1):
    c1[i] = int(c1[i])
print("Equation 1 coefficients:", c1)

c2 = input("Second equation coefficients: ")
c2 = c2.split(" ")
for i, num in enumerate(c2):
    c2[i] = int(c2[i])
print("Equation 2 coefficients:", c2)


l1 = len(c1)
l2 = len(c2)
result = [0] * (l1 + l2 -1)

print(result)
c1 = list(reversed(c1))
c2 = list(reversed(c2))
for i in range(l2):
    for g in range(l1):
        result[i + g] += c2[i] * c1[g]

result = list(reversed(result))
print(result)
a = [1]
for i in range(255):
    val = a[i] * 2
    if val > 255:
        val = val ^ 285
    a.append(val)
print(a)
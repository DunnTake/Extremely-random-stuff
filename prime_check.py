def IsPrime(n):
    threshold = (n**(1/2))
    if threshold // 1 == threshold:
        return False
    threshold = threshold // 1
    checks = [2,3]
    k = 1
    while True:
        if (6*k - 1) < threshold:
            checks.append(6*k - 1)
        else:
            break
        if (6*k + 1) < threshold:
            checks.append(6*k + 1)
        else:
            break
        k += 1
    for num in checks:
        if n % num == 0:
            return False
    return True

number = int(input(""))
print(IsPrime(number))

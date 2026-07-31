from random import randint
from math import log2,log10

def expo_get(number, max): # get the exponents breakdown of a number, used in Miller_Rabin()
    steps = []

    while number >= max:
        expos = []
        temp = 1
        tempmax = max
        while tempmax > 1:
            temp *= tempmax
            expos.append(tempmax)
            while temp * tempmax > number and tempmax > 1:
                tempmax -= 1
        steps.append(expos)
        number -= temp
    steps.append([number]) #append the final leftover

    return steps

def Baillie(n): # Direct number testing, use for numbers with 16 digits or less
    threshold = (n**(1/2))
    if threshold**2 == n:
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
            return "Not prime"
    return "Prime"

def Miller_Rabin(n): # Probability-based testing, gauges how likely n is to be prime
    k = 1000 # Number of tests, change for accuracy
    s = log2(n)//1
    d = 0
    while True: # Find s and d
        if (n-1) % (2**s) == 0 and int((n-1) // (2**s)) % 2 == 1:
            d = int((n-1) // (2**s))
            break
        s -= 1

    for h in range(k):
        a = randint(2,n-2)
        x = 1
        digits = int(log10(n) + 1)
        maxpow = 307 // digits # mitigate python's overflow point
        expos = expo_get(d,maxpow)
        for expo in expos: # fork of x = (a**d) % n, result too large
            tempa = 1
            for i in range(len(expo)):
                if i == 0:
                    tempa = (a ** expo[i]) % n
                else:
                    tempa = (tempa ** expo[i]) % n
            x = (x * tempa) % n

        for j in range(int(s)):
            y = (x**2) % n
            if y == 1 and x != 1 and x != n-1:
                return "Not prime", 1
            x = y
            #print(y)
        if y != 1:
            return "Not prime", 2
    return "Likely prime"

number = int(input(""))
'''if len(str(number)) < 10:
    print(Baillie(number))
else:'''
print(Miller_Rabin(number))
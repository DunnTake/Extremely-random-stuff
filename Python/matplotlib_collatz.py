import matplotlib.pyplot as plt

def collatz(n):
    step = 0
    while n != 1:
        if n % 2 == 1:
            n = (n * 3) + 1
        else:
            n /= 2
        step += 1
    return step


min = int(input("min: "))
max = int(input("max: "))
x = []
y = []

for i in range(min, max + 1):
    #change function here
    result = (100-i**2)**(1/2)
    x.append(i)
    y.append(result)


plt.plot(x,y, color='blue', marker='o', linestyle='-')

plt.title("graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
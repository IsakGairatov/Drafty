x = int(input())
a = int('1' + '0' * (x - 1))
b = int('1' + '0' * x)

for i in range(b - 1, a - 1, -2):
    print(i, end=' ')

a = int(input())
b = int(input())

if a >= b:
    x = range(a, b - 1, -1)
elif a < b:
    x = range(a, b + 1)

for n in x:
    print(n, end=' ')

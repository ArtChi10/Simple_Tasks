def gsd(a, b):
    while b:
        a, b = b, a % b
    return a
a = int(input())
b = int(input())
a, b = max(a, b), min(a, b)
print(gsd(a, b))
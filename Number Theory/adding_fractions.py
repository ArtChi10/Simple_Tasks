a, b, c, d = map(int, input().split())
m = a*d+b*c
n = b*d
def gsd(a, b):
    while b:
        a, b = b, a%b
    return a
x = gsd(m, n)
print(m//x, n//x)
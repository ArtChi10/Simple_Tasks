def gsd(a, b):
    while b:
        a, b = b, a % b
    return a


def nok(a, b):
    a, b = max(a, b), min(a, b)
    return (a * b) // gsd(a, b)


a, b = map(int, input().split())
print(nok(a, b))
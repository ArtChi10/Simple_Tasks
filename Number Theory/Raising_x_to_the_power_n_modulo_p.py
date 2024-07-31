def modular_exponentiation(x, n, p):
    result = 1
    x = x % p  # Уменьшаем x по модулю p сразу, если оно больше p

    while n > 0:
        if n % 2 == 1:  # Если n нечетное, умножаем результат на x
            result = (result * x) % p
        n = n // 2  # Делим n пополам
        x = (x * x) % p  # Умножаем x на само себя

    return result

# Пример ввода
x = int(input("Введите x: "))
n = int(input("Введите n: "))
p = int(input("Введите p: "))

# Вычисление x^n % p
print(modular_exponentiation(x, n, p))

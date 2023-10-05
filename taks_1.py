def f(x):
    return 1 / (1 + x**3)


epsilon = 0.005

n = 10

# Початне наближене значення інтеграла
I_approx = 0

# Початна різниця між значеннями з іншою половиною вузлів
diff = epsilon * 2

while diff >= epsilon:
    n *= 2
    h = (15 - 2) / n
    sum1 = sum(f(2 + i * h) for i in range(n))
    sum2 = sum(f(2 + i * h) for i in range(0, n, 2))
    I_approx = h * sum2
    diff = abs(I_approx - (h / 2) * sum1)

print(f"Наближене значення інтеграла: {I_approx}")

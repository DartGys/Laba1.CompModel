import math


def f(x):
    return 1 / (1 + x**3)


def left_rectangle_rule(a, b, n):
    h = (b - a) / n
    integral_approximation = 0
    for i in range(n):
        xi = a + i * h
        integral_approximation += f(xi)
    integral_approximation *= h
    return integral_approximation


epsilon = 0.005
n = 1
a = 2  # Початок обчислення інтегралу
M = 10000  # Велике число, для обмеження інтервалу
previous_integral = left_rectangle_rule(a, M, n)
current_integral = left_rectangle_rule(a, M, 2 * n)

while abs(current_integral - previous_integral) / (2**1 - 1) >= epsilon:
    n *= 2
    previous_integral = current_integral
    current_integral = left_rectangle_rule(a, M, 2 * n)

result = current_integral
print("Результат обчислення інтеграла:", result)

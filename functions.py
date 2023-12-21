from random import random
from math import log

# Интенсивность
lambd = 8

# Функция интенсивности
intense_func = lambda x: round(-0.0932 * (x ** 2) + 2.4061 * x - 8.9524, 3)

# Функция неоднородного пуассоновского процесса
def poisson_func(t, lambd=lambd):
    iterations = 0
    while True:
        u1 = random()
        t -= log(u1)/lambd
        u2 = random()
        iterations += 1
        if iterations > 50:
            break
        if u2 <= intense_func(t)/lambd:
            return t

# Функция генерации случайной величины (времени обслуживания)
def service_func(lambd=lambd):
    return -(log(random()))/lambd

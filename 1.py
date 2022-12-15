message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return (Number ** 0.5)


def calc(your_number):
    if your_number <= 0:
        return

    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {CalculateSquareRoot(your_number)}')


print(message)
calc(25.5)

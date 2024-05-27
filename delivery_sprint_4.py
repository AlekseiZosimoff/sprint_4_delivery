import sys

"""
25 май 2024, 21:24:27
114601820
A
Python 3.12.1
OK
-
34ms
4.25Mb
"""


def count_platforms(robots_weights: list, max_weight: int) -> int:
    """
    Подсчёт минимального количества платформ
    для перевозки модулей
    """
    lightest_module: int = 0
    heaviest_module: int = len(robots_weights) - 1
    counter: int = 0

    while lightest_module <= heaviest_module:
        if (robots_weights[lightest_module]
                + robots_weights[heaviest_module] <= max_weight):
            lightest_module += 1
        heaviest_module -= 1
        counter += 1
    return counter


def main():
    robots_weights = [int(i) for i in sys.stdin.readline().strip().split()]
    robots_weights = sorted(robots_weights)
    max_weight = int(sys.stdin.readline().strip())
    print(count_platforms(robots_weights, max_weight))


if __name__ == '__main__':
    main()

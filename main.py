from Solver import Solver
from Shikaku import Shikaku
from colorama import init
from Parser import Parser


def main():
    init()
    with open("Shikakus/shikaku10.txt") as f:
        shikaku = Parser().parse_puzzle(f.read())
        result = Solver.solve(shikaku)
        if len(result) == 0:
            print("Решение отсутствует")
        for task in result:
            print(task)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

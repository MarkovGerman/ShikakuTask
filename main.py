from Solver import Solver
from Shikaku import Shikaku
from colorama import init
from Parser import Parser


def main():
    init()
    with open("Shikakus/shikaku10.txt") as f:
        shikaku = Parser().parse_puzzle(f.read())
        result = Solver.return_all_answer(Solver.solve(shikaku))
        print(result)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

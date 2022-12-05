from Solver import Solver
from Shikaku import Shikaku
from colorama import init
from Parser import Parser


def main():
    init()
    name_puzzle = input()
    print(find_result(name_puzzle))


def find_result(name_puzzle):
    with open(f"Shikakus/{name_puzzle}.txt") as f:
        try:
            shikaku = Parser().parse_puzzle(f.read())
            s = Solver.solve(shikaku)
            return Solver.return_all_answer(shikaku, s)
        except ValueError:
            return "Неправильно введена строка"


if __name__ == '__main__':
    main()

import tkinter as tk
from Parser import Parser
from Solver import Solver

class App:
    def __init__(self):
        def clicked():
            self.size = int(cell.get())
            for b in self.buttons:
                b.grid_remove()
            for e in self.entries:
                e.delete(0)
            self.entries = []
            self.buttons = []
            self.add_entries()

        self.size = 0
        self.buttons = []
        self.entries = []
        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.cells_entry = []
        tk.Label(self.root, text="Введи размер головоломки").grid(row=1, column=0)
        cell = tk.Entry()
        cell.grid(row=1, column=1)
        tk.Button(self.root, text="Введено", command=clicked).grid(row=1, column=2)

    def mainloop(self):
        self.root.mainloop()

    def add_entries(self):
        def clicked():
            self.check_all_entry()
        self.cells_entry = [[] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                entry = tk.Entry(self.root)
                entry.place(x=20 + 30 * i, y=20 + 30 * j, width=30, height=30)
                self.entries.append(entry)
                self.cells_entry[i].append(entry)
        tk.Button(self.root, text="Готово", command=clicked).grid(row=1, column=3)

    def check_all_entry(self):
        result = str(self.size) + "\n"
        for i in range(self.size):
            for j in range(self.size):
                value = self.cells_entry[j][i].get()
                if len(value) == 0:
                    value = "0"
                result += f"{value} "
            result += "\n"
        try:
            shikaku = Parser().parse_puzzle(result)
            s = Solver.solve(shikaku)
            self.print_result(s)
            print(Solver.return_all_answer(shikaku, s))
        except ValueError:
            print("Неправильно введена строка")
            label = tk.Label(self.root, text="Неправильно введена строка")
            label.grid(row=self.size + 4, column=0)
            self.buttons.append(label)

    def print_result(self, res):
        Colors = ['green', 'red', 'chartreuse2', 'cyan', 'cyan4', 'DarkGray', 'DarkOliveGreen1', 'IndianRed', 'indigo']
        for k in range(len(res)):
            for i in range(self.size):
                for j in range(self.size):
                    cell = res[k].cells[i][j]
                    b = tk.Button(self.root, text=str(cell.number), bg=Colors[cell.color_tkinter % len(Colors)])
                    b.grid(row=(k+1) * self.size + i, column=(k+1)*self.size + j + 2)
                    self.buttons.append(b)


if __name__ == "__main__":
    app = App()
    app.mainloop()

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()



        self.btn_submit = tk.Button(self, text="Отправить")
        self.btn_submit.pack(padx=10, pady=10, side=tk.RIGHT)


if __name__ == "__main__":
    app = App()
    app.mainloop()

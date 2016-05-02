# I modified a simple Tkinter script to see how it functions

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.pressButton = tk.Button(self, text='Print text in terminal',
            command=self.button_press)
        self.pressButton.grid(row=1, column=0, columnspan=1)
        self.quitButton = tk.Button(self, text='Close Window',
            command=self.quit)
        self.quitButton.grid(row=0, column=1, columnspan=1)

    def button_press(self):
        print('You pressed the button!')

app = Application()
app.master.title("Jimmy's application")
app.mainloop()

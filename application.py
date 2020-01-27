import tkinter as tk

# Так ты подключаешь дополнительные окна
from first import First # Это окно, которое рисует обычный куб (самый банальный)
from second import Second
from third import Third
from fourth import Fourth
from fifth import Fifth
from sixth import Sixth
from start import Start # Это первоначальное окно, которое перенаправляет на все остальные
# Аналогично нужно будет подключить все новые тобой написанные классы

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Start, First, Second, Third, Fourth, Fifth, Sixth): #Здесь прописаны все классы-окна, которые используются

            frame = F(container, self, Start)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            frame.configure(background='azure') #Цвет фона

        self.show_frame(Start)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

app = Application()

app.title("OLAP-pic") # название всей формы
app.minsize(530, 420) # размер окна

app.mainloop()

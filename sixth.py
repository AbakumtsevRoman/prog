import tkinter as tk
from PIL import ImageTk, Image
from openpyxl import load_workbook
from olap import OLAP
import re

class Sixth(tk.Frame):
    def __init__(self, parent, controller, back=None):
        tk.Frame.__init__(self,parent)
        self.create_widgets(parent, controller, back)

    def create_widgets(self, parent, controller, back):

        self.l14 = tk.Label(self, text="Развертка OLAP-куба", font="Arial 11", background='azure')
        self.l14.pack(side="top", pady=5)	
	
        self.l1 = tk.Label(self, text="Имя файла:", background='azure')
        self.l1.pack(side="top")
        self.file = tk.Entry(self, bg="yellow")
        self.file.bind("<Key>", self.is_button_disabled)
        self.file.pack(side="top")

        self.l1 = tk.Label(self, text="Имя листа:", background='azure')
        self.l1.pack(side="top")
        self.list = tk.Entry(self, bg="yellow")
        self.list.bind("<Key>", self.is_button_disabled)
        self.list.pack(side="top")

        self.l1 = tk.Label(self, text="1 измерение:", background='azure')
        self.l1.pack(side="top")
        self.r1 = tk.Entry(self, bg="yellow")
        self.r1.bind("<Key>", self.is_button_disabled)
        self.r1.pack(side="top")

        self.l2 = tk.Label(self, text="2 измерение:", background='azure')
        self.l2.pack(side="top")
        self.r2 = tk.Entry(self, bg="yellow")
        self.r2.bind("<Key>", self.is_button_disabled)
        self.r2.pack(side="top")

        self.l3 = tk.Label(self, text="3 измерение:", background='azure')
        self.l3.pack(side="top")
        self.r3 = tk.Entry(self, bg="yellow")
        self.r3.bind("<Key>", self.is_button_disabled)
        self.r3.pack(side="top")

        self.imgF = tk.Label(self, text="Имя для сохранения (по умолчанию result.jpg): ", background='azure')
        self.imgF.pack(side="top")
        self.img = tk.Entry(self)
        self.img.bind("<Key>", self.is_button_disabled)
        self.img.pack(side="top")


        self.visualize_button = tk.Button(self)
        self.visualize_button["text"] = "Визуализировать"
        self.visualize_button["command"] = self.click
        self.visualize_button["state"] = "disabled"
        self.visualize_button.pack(side="top", pady=15)

        # Кнопка переводящая на начальный экран
        button = tk.Button(self, text="Назад", command=lambda: controller.show_frame(back))
        button.pack(side="top")
    
    def check_range_input(self, r):
        regex = r"[A-Z]{1}\d+:[A-Z]{1}\d+"
        if re.match(regex, r.get()):
            r["bg"] = "white"
            return True
        r["bg"] = "yellow"
        return False

    def is_button_disabled(self, *args):
        if len(self.file.get()) != 0:
            self.file["bg"] = "white"
        else:
            self.file["bg"] = "yellow"
        if len(self.list.get()) != 0:
            self.list["bg"] = "white"
        else:
            self.list["bg"] = "yellow"
        if sum((self.check_range_input(self.r1), self.check_range_input(self.r2), self.check_range_input(self.r3))) == 3 and len(self.file.get()) != 0 and len(self.list.get()) != 0:
            self.visualize_button["state"] = "normal"

    # обработчик нажатия на кнопку "Визуализировать"
    def click(self):
        r = [self.r1.get(), self.r2.get(), self.r3.get()]

        wb = load_workbook(filename = self.file.get())
        sheet = wb[self.list.get()]

        # Координаты для каждой картинки
        X = (552, 510)
        Y = (130, 105)
        Z = (75, 545)

        x = ((210, 510), (310, 510), (410, 510))
        y = ((90, 244), (90, 344), (90, 444))
        z = ((538, 478), (588, 448), (638, 418))

        # А тут передаешь для рисования
        # Первым аргументом идет файл картинки на которой будет рисоваться результат
        # Новая картинка будет сохранена под именем result.jpg
        o = OLAP("pics/pic6.jpg", X, Y, Z, x, y, z)

        o.drawXName(sheet[r[0].split(":")[0][0]][int(r[0].split(":")[0][1:])-1].value)
        o.drawYName(sheet[r[1].split(":")[0][0]][int(r[1].split(":")[0][1:])-1].value)
        o.drawZName(sheet[r[2].split(":")[0][0]][int(r[2].split(":")[0][1:])-1].value)

        for rIndex in range (len(r)):
            startLetter, startNumber = r[rIndex].split(":")[0][0], int(r[rIndex].split(":")[0][1:])
            for i in range(len(o.points)):
                o.drawText(str(sheet[startLetter][startNumber+i].value), o.points[rIndex][i][0], o.points[rIndex][i][1], 0.0)

        # новую картинку сохраняем в тот файл, который указали в поле
        o.saveImage(self.img.get())
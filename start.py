import tkinter as tk

# Импорт имеющихся окон
# Классы находятся в соответствующих файлах
from first import First
from second import Second
from third import Third
from fourth import Fourth
from fifth import Fifth
from sixth import Sixth
#from idlelib.tooltip import ListboxToolTip


# Стартовое окно
class Start(tk.Frame):

    def __init__(self, parent, controller, back=None):
        tk.Frame.__init__(self,parent)

        # При нажатии на эту кнопку открывается окно для рисования полного OLAP-куба
        button1 = tk.Button(self, text="Обычный OLAP-куб", width=30, command=lambda: controller.show_frame(First))# В controller.show_frame - имя класса
        button1.pack(pady=15)

        button2 = tk.Button(self, text="1-ый срез OLAP-куба", width=30, command=lambda: controller.show_frame(Second))
        button2.pack()
        
        button3 = tk.Button(self, text="2-ой срез OLAP-куба", width=30, command=lambda: controller.show_frame(Third))
        button3.pack(pady=15)

        button4 = tk.Button(self, text="Транспонирование OLAP-куба", width=30, command=lambda: controller.show_frame(Fourth))
        button4.pack()

        button5 = tk.Button(self, text="Свертка OLAP-куба", width=30, command=lambda: controller.show_frame(Fifth))
        button5.pack(pady=15)

        button6 = tk.Button(self, text="Развертка OLAP-куба", width=30, command=lambda: controller.show_frame(Sixth))
        button6.pack()
        
		
		# Чтобы добавить кнопку, которая открывает новое окно - импортируешь в начале класс, который ты напишешь
        # и делаешь кнопку как на примере выше
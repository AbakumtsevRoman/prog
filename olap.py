#!/usr/bin/python3

from openpyxl import load_workbook
from PIL import Image
from PIL import ImageFont, ImageDraw, ImageOps
import time

#z-name 550X363
#z1 - 415x356
#z2 - 435x335
#z3 - 455x315
#z4 - 480-294

#x-name - 212x424
#x1 - 157x424
#x2- 227x424
#x3 - 297x424
#x4 - 387x424

#y-name - 7x321
#y1 - 45x335
#y2 - 45x265
#y2 - 45x195
#y3 - 45x125

class OLAP:

    def __init__(self, filename, X, Y, Z, x, y, z):
        self.im = Image.open(filename)

        self.X = X
        self.Y = Y
        self.Z = Z

        self.x = x
        self.y = y
        self.z = z

        self.points = (self.x, self.y, self.z)

    def drawText(self, text, x, y, angle):
        f = ImageFont.truetype("arial.ttf", 17, encoding='UTF-8')
        txt=Image.new('RGBA', (500,50))
        d = ImageDraw.Draw(txt)
        d.text( (0, 0), text,  font=f, fill=(0,0,0,255))
        w=txt.rotate(angle, expand=True, center=(0,0))
        self.im.paste(w, (x,y),  w)

    def drawZName(self, text):
        self.drawText(text, self.Z[0], self.Z[1], 0.0)

    def drawXName(self, text):
        self.drawText(text, self.X[0], self.X[1], 0.0)

    def drawYName(self, text):
        self.drawText(text, self.Y[0], self.Y[1], 0.0)
		
    def drawZ1Name(self, text):
        self.drawText(text, 623, 380, 0.0)

    def drawX1Name(self, text):
        self.drawText(text, 710, 70, 0.0)

    def drawY1Name(self, text):
        self.drawText(text, 425, 155, 0.0)	

    def saveImage(self, filename):
        if filename.strip(" ") == "":
            filename = "result.jpg"
        self.im.save(filename)

# if __name__ == "__main__":

#     r = ["A1:A5", "B1:B6", "C1:C6"]

#     wb = load_workbook(filename = 'roma.xlsx')
#     sheet = wb['Лист1']

#     o = OLAP()
#     o.drawXName(sheet[r[0].split(":")[0][0]][int(r[0].split(":")[0][1:])-1].value)
#     o.drawYName(sheet[r[1].split(":")[0][0]][int(r[1].split(":")[0][1:])-1].value)
#     o.drawZName(sheet[r[2].split(":")[0][0]][int(r[2].split(":")[0][1:])-1].value)

#     for rIndex in range (len(r)):
#         startLetter, startNumber = r[rIndex].split(":")[0][0], int(r[rIndex].split(":")[0][1:])
#         for i in range(len(o.points)):
#             o.drawText(str(sheet[startLetter][startNumber+i].value), o.points[rIndex][i][0], o.points[rIndex][i][1], 0.0)

#     o.saveImage("result.jpg")

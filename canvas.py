from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
    defaultpensize= 3
    defaultpenc= 'black'
    def __init__(self):
        self.screen= Tk()
        self.penbutton= Button(self.screen, text= 'Pen', command= self.usepen)
        self.penbutton.grid(row= 0, column= 0)
        self.brushbutton= Button(self.screen, text= 'Brush', command= self.usebrush)
        self.brushbutton.grid(row= 0, column= 1)
        self.colourbutton= Button(self.screen, text= 'Colour', command= self.choosecolour)
        self.colourbutton.grid(row= 0, column= 2)
        self.eraserbutton= Button(self.screen, text= 'Eraser', command= self.useeraser)
        self.eraserbutton.grid(row= 0, column= 3)
        self.sizebutton= Scale(self.screen, from_= 1, to= 10)
        self.sizebutton.grid(row= 0, column= 4)
        self.canvas= Canvas(self.screen, bg= 'white', width= 600, height= 600)
        self.canvas.grid(row= 1, columnspan= 5)
        self.setup()
        
        self.screen.mainloop()
        
    def setup(self):
        self.oldx= None
        self.oldy= None
        self.colour= self.defaultpenc
        self.eraser_on= False
        self.activebutton= self.penbutton
        self.linewidth= self.sizebutton.get()
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1', self.reset)
    
    def usepen(self):
        self.activebutton(self.penbutton)
    
    def usebrush(self):
        self.activebutton(self.brushbutton)

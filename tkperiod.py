from tkinter import *
import EmotionPrediction as EP
from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        im = Image.open('F:\\Bili\\current_period.jpg')
        ph = ImageTk.PhotoImage(im)

        self.helloLabel = Label(self, text='情绪、智慧、精力循环周期')
        self.helloLabel.pack()

        self.helloLabel = Label(self, image=ph)
        self.helloLabel.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.helloLabel.pack()

        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

EP.sinplot()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
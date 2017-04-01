from Tkinter import Tk, Frame, BOTH, Canvas

class Sumitup(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.reds = ["#ff8080", "#ff6666", "#ff4d4d", "#ff3333", "#ff1a1a", "#ff0000", "#e60000", "#cc0000", "#b30000"]
        self.blues = ["#668cff", "#4d79ff", "#3366ff", "#1a53ff", "#0040ff", "#0039e6", "#0033cc", "#002db3", "#002699"]


        self.parent = parent
        self.parent.title("SumItUp")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.field = Canvas(self, width=500, height=300, background="gray25")
        self.field.pack()
        self.drawField()
        self.makeTile(150, 40, 3)
        self.makeTile(200, 80, -6)
        self.makeTile(200, 40, -9)


    def centerWindow(self):

        w = 500
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def drawField(self):

        self.field.create_rectangle(130, 20, 370, 280, fill="gray16")
        #This is main canvas
        self.field.create_rectangle(380, 20, 480, 120, fill="gray16")
        #This is scoreboard

    def makeTile(self, x, y, number):

        if number < 0:
            self.field.create_rectangle(x, y, x+20, y+20, fill=self.reds[abs(number)-1])
        else:
            self.field.create_rectangle(x, y, x+20, y+20, fill=self.blues[number-1])
        #tile color changes depending on the magnitude of the number

        self.field.create_text(x+10, y+10, text=str(number), fill="#f2f2f2")

def main():

    root = Tk()
    root.geometry("500x300+450+300")
    app = Sumitup(root)
    root.mainloop()

if __name__ == '__main__':
    main()

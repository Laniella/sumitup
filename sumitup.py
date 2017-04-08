from Tkinter import Tk, Frame, BOTH, Canvas
from random import randint

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
        self.tiles = []

        self.teststuff()

    #list of columns 0:140, 1:160 .... 10:360
    columns = [x for x in range(140, 360, 20)]

    def teststuff(self):
    	
        self.makeTile(randint(0, len(Sumitup.columns) - 1))
        self.makeTile(randint(0, len(Sumitup.columns) - 1))
        self.makeTile(randint(0, len(Sumitup.columns) - 1))
        print self.tiles


    def centerWindow(self):

        w = 500
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def drawField(self):
    	#This is main canvas
        self.field.create_rectangle(130, 20, 370, 280, fill="gray16")
       
        #This is scoreboard
        self.field.create_rectangle(380, 20, 480, 120, fill="gray16")
        

    def makeTile(self, column):
    	#tile color changes depending on the magnitude of the number
    	number = randint(-9, 9)

        if number < 0:
        	#tiles made at top of the main canvas, randomly
            rec_id = self.field.create_rectangle(Sumitup.columns[column] - 10, 20,
            									 Sumitup.columns[column] + 10, 40,
            									 fill=self.reds[abs(number)-1])
        else:
            rec_id = self.field.create_rectangle(Sumitup.columns[column] - 10, 20,
            									 Sumitup.columns[column] + 10, 40, 
            									 fill=self.blues[number-1])
        

        text_id = self.field.create_text(Sumitup.columns[column], 30, text=str(number), fill="#f2f2f2")

        self.tiles.append((rec_id, text_id))
    	


def main():

    root = Tk()
    root.geometry("500x300+450+300")
    app = Sumitup(root)
    root.mainloop()

if __name__ == '__main__':
    main()

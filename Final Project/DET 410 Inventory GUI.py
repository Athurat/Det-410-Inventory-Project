from tkinter import *
import tkinter
import tkinter.messagebox
import tkinter as tk
ws = Tk()
ws.title('DET 410 Inventory and Requesitions')
ws.geometry('500x500')

#Display empty an empty window
class MainGUI:
    def __init__ (self):
        self.main_window = tkinter.TK()
#3 frames for organization
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
#Pack three frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

#Create the top title
        self.title_label = tkinter.Label(self.top_frame, text = 'DET 410 Inventory and Requisitions', font = 40)
        self.title_label.pack()

    def addbuttonwindow(self):
        #remove the main window
        self.root.destroy()
        self.addbuttonwin = tk.TK()
        self.addbuttonwin.title('Add Items')

        #Create Frames
        self.firstframe = (self.addbuttonwin)
        self.secondframe = (self.addbuttonwin)
        self.thirdframe = (self.addbuttonwin)
        self.fourthframe = (self.addbuttonwin)
        self.fifthframe = (self.addbuttonwin)
        self.sixthframe = (self.addbuttonwin)

        #pack frames
        self.firstframe.pack()
        self.secondframe.pack()
        self.thirdframe.pack()
        self.fourthframe.pack()
        self.fifthframe.pack()
        self.sixthframe.pack()
tkinter.mainloop()

if __name__ == '__main__':
    mainGUI = MainGUI()


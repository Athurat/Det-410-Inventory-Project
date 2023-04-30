import tkinter as tk
from tkinter import *
from tkinter import ttk

class HeadGUI:
    def __init__ (self):
        # create the main window
        self.root = tk.Tk()
        #Create Frames
        self.topframe = Frame(self.root)
        self.middleframe = Frame(self.root)
        self.lowerframe = Frame(self.root)
        self.editframe = Frame(self.root)
        self.bottomframe = Frame(self.root)

        #Pack Frames
        self.topframe.pack()
        self.middleframe.pack()
        self.lowerframe.pack()
        self.editframe.pack()
        self.bottomframe.pack()

        # set the window title
        self.root.title("DET 410 Inventory and Requisitions")


        # create a label with large font size and centered text
        title_label = tk.Label(self.topframe, text="DET 410 Inventory And Requisitions", font=("Arial", 50),width = 500, height = 2 , bg="purple", fg="white", bd=5, relief="ridge")
        title_label.pack()

        #create and pack quote
        Quote_label = tk.Label(self.middleframe, text='Fly, Fight, and Win!',height=2, font=("Arial", 40), bg="yellow", fg='Black', bd=5, relief="ridge", anchor = 'e')
        Quote_label.pack(side=tk.RIGHT)

        #Create search bar
        Searchbutton = tk.Button(self.middleframe, text='Search', command='search', width=30, height=8)
        Searchbutton.pack(side=tk.LEFT)

        entry = tk.Entry(self.middleframe, width=20, font=('Arial', 40))
        entry.pack(expand=True, fill='y')

        #Select Button
        Selectbutton = tk.Button(self.lowerframe, text='SELECT', width=30, height=5)
        Selectbutton.pack(side=tk.LEFT)

        #Create Add button
        Addbutton = tk.Button(self.lowerframe, text='ADD', width=30, height=5)
        Addbutton.pack(side=tk.LEFT)

        #Create Delete Button
        Deletebutton = tk.Button(self.lowerframe, text='DELETE', width=30, height=5)
        Deletebutton.pack(side=tk.LEFT)

        #Create Edit/Reserve Button
        Editbutton = tk.Button(self.lowerframe, text='EDIT/RESERVE', width=30, height=5)
        Editbutton.pack(side=tk.LEFT)

        #Create a row of stuff for editing
        id = Label(self.editframe, text="Category",relief="ridge")
        id.grid(row=0, column=0)

        Catcode = Label(self.editframe, text="CatCode",relief="ridge")
        Catcode.grid(row=0, column=1)

        ItemDesc = Label(self.editframe, text="Item Description",relief="ridge")
        ItemDesc.grid(row=0, column=2)

        location = Label(self.editframe, text ='Location',relief="ridge")
        location.grid(row=0, column=3)

        purchaselocation = Label(self.editframe, text = 'Purchase Location',relief="ridge")
        purchaselocation.grid(row=0, column=4)

        quantity = Label(self.editframe, text = 'Quantity',relief="ridge")
        quantity.grid(row=0, column=5)

        quality = Label(self.editframe, text = 'Quality',relief="ridge")
        quality.grid(row=0, column= 6)

        reserved = Label(self.editframe, text = 'Reserved To:',relief="ridge")
        reserved.grid(row=0, column = 7)

        # Create entry widgets
        id_entry = Entry(self.editframe)
        id_entry.grid(row=1, column=0)

        Category_entry = Entry(self.editframe)
        Category_entry.grid(row=1, column=1)

        itemdesc_entry = Entry(self.editframe)
        itemdesc_entry.grid(row=1, column=2)

        location_entry = Entry(self.editframe)
        location_entry.grid(row=1, column=3)

        purchaselocation_entry = Entry(self.editframe)
        purchaselocation_entry.grid(row=1,column=4)

        quantity_entry = Entry(self.editframe)
        quantity_entry.grid(row=1,column=5)

        quality_entry = Entry(self.editframe)
        quality_entry.grid(row=1, column=6)

        reservation_entry = Entry(self.editframe)
        reservation_entry.grid(row=1, column=7)

        # Scrollbar for Listbox
        yscroll = Scrollbar(self.bottomframe)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll = Scrollbar(self.bottomframe, orient='horizontal')
        xscroll.pack(side=BOTTOM, fill=X)

        # Create and pack inventory list
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8')
        Inventorylist = ttk.Treeview(self.bottomframe, columns=columns, show='headings',yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        Inventorylist.pack(side=tk.TOP)

        # define our columns and set the Headers
        Inventorylist.heading('#1', text='ID')
        Inventorylist.heading('#2', text='Category Code')
        Inventorylist.heading('#3', text='Item Description')
        Inventorylist.heading('#4', text='Location')
        Inventorylist.heading('#5', text='Purchase Location')
        Inventorylist.heading('#6', text='Quantity')
        Inventorylist.heading('#7', text='Quality')
        Inventorylist.heading('#8', text='Reserved')

        # Set Column Width/height
        Inventorylist.column("#1", width=190)
        Inventorylist.column("#2", width=190)
        Inventorylist.column("#3", width=190)
        Inventorylist.column("#4", width=190)
        Inventorylist.column("#5", width=190)
        Inventorylist.column("#6", width=190)
        Inventorylist.column("#7", width=190)
        Inventorylist.column("#8", width=190)


        # Add some data to the listbox
        Inventorylist.insert('', 'end', values=('Row 1 Column 1', 'Row 1 Column 2', 'Row 1 Column 3', 'Row 1 column 4', 'Row 1 Column 5', 'Row 1, column 6', 'Row 1 column 7', 'row 1 column 8'))
        Inventorylist.insert('', 'end', values=('Row 2 Column 1', 'Row 2 Column 2', 'Row 2 Column 3'))
        Inventorylist.insert('', 'end', values=('Row 3 Column 1', 'Row 3 Column 2', 'Row 3 Column 3'))
        Inventorylist.insert('', 'end', values=('Row 4 Column 1', 'Row 4 Column 2', 'Row 4 Column 4'))
        Inventorylist.insert('', 'end', values=('Row 5 Column 1', 'Row 5 Column 2', 'Row 5 Column 5'))
        Inventorylist.insert('', 'end', values=('Row 6 Column 1', 'Row 6 Column 2', 'Row 6 Column 6'))

    # Select Row and Edit Row
    def Add_button(self):
        # clear entry boxes
        id_entry.delete(0, END)
        Category_entry.delete(0, END)
        itemdesc_entry.delete(0, END)
        location_entry.delete(0, END)
        purchaselocation_entry.delete(0, END)
        quality_entry.delete(0, END)
        quantity_entry.delete(0, END)
        reservation_entry.delete(0, END)

        # Get row that has focus
        selected = Inventorylist.focus()
        # grab record values
        values = Inventorylist.item(selected, 'values')

        # Insert focus row in entry boxes
        id_entry.insert(0, values[0])
        Category_entry.insert(0, values[0])
        itemdesc_entry.insert(0, values[0])
        location_entry.insert(0, values[0])
        purchaselocation_entry.insert(0, values[0])
        quality_entry.insert(0, values[0])
        quantity_entry.insert(0, values[0])
        reservation_entry.insert(0, values[0])

    # Update Record
    def update_record(self):
        selected = Inventorylist.focus()

        # save new data
        Inventorylist.item(selected, text="",
                           values=(id_entry.get(), Category_entry.get(), itemdesc_entry.get(), location_entry.get(),
                                   purchaselocation_entry.get(), quality_entry.get(), quantity_entry.delete.get(),
                                   reservation_entry.get()))

        # clear entry boxes
        id_entry.delete(0, END)
        Category_entry.delete(0, END)
        itemdesc_entry.delete(0, END)
        location_entry.delete(0, END)
        purchaselocation_entry.delete(0, END)
        quality_entry.delete(0, END)
        quantity_entry.delete(0, END)
        reservation_entry.delete(0, END)

        # Run the GUI main loop
        self.root.mainloop()

if __name__ == '__main__':
    mainGUI = HeadGUI()

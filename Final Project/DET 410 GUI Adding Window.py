import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3 as lite
import sys
#import library for images
from PIL import ImageTk, Image

#Get the Database Data
conn = lite.connect('DET410 Inventory DB.db')

#Class for all functions
class HeadGUI:
    def __init__ (self):
        # create the main window and window resolution
        self.root = tk.Tk()
        self.root.configure(bg="blue")
        self.root.geometry("1920x1080")
        #Create background Frames
        self.topframe = Frame(self.root, bg="blue")
        self.middleframe = Frame(self.root)
        self.lowerframe = Frame(self.root)
        self.editframe = Frame(self.root)
        self.bottomframe = Frame(self.root)
        self.lowestframe = Frame(self.root)

        #Pack all Frames
        self.topframe.pack()
        self.middleframe.pack()
        self.lowerframe.pack()
        self.editframe.pack()
        self.bottomframe.pack()
        self.lowestframe.pack()


        #Image creation for the DET 410 Emblems
        img1 = ImageTk.PhotoImage(Image.open("DET410Emblem#1.jpg"))
        img2 = ImageTk.PhotoImage(Image.open("DET410Emblem#2.jpg"))
        # Make the Labels for the emblems
        label = Label(self.topframe, image=img1)
        label.pack(side=tk.RIGHT)
        label = Label(self.topframe, image=img2)
        label.pack(side=tk.LEFT)

        # set the window title
        self.root.title("DET 410 Inventory and Requisitions")

        # Make the Labels for the Key
        label = Label(self.lowestframe, text="Key:", width = 100, height = 7, relief='sunken', font=("Arial", 10) )
        label.pack(side=tk.LEFT)
        label = Label(self.lowestframe, text="WP = Weapons    PT = Physical Training \nUT = Utility    DO = Decor/Furniture \nOFF = Office      KH = Kitchen/Food \nCL = Clothing      FT = Field Training ",
                      width = 100, height = 7, relief='sunken', font=("Arial", 10))
        label.pack(side=tk.RIGHT)


        # create a label with large font size and centered text
        title_label = tk.Label(self.topframe, text="DET 410 Inventory And Requisitions", font=("Arial", 50),width = 500, height = 2 , bg="purple", fg="white", bd=5, relief="ridge")
        title_label.pack()

        #create and pack quote
        Quote_label = tk.Label(self.middleframe, text='Fly, Fight, and Win!',height=2, font=("Arial", 40), bg="yellow", fg='Black', bd=5, relief="ridge")
        Quote_label.pack(side=tk.RIGHT)

        #Create a row of stuff for editing
        id = Label(self.editframe, text="ID",relief="ridge")
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

        #Configure the scrollbars
        yscroll.config(command=Inventorylist.yview)
        xscroll.config(command=Inventorylist.xview)

        # Creates the Error Box for Datatype Error (ID and Quantity)
        ######

        Inventorylist["columns"] = columns

        # define the columns and set the Headers
        Inventorylist.heading('#1', text='ID')
        Inventorylist.heading('#2', text='Category Code')
        Inventorylist.heading('#3', text='Item Description')
        Inventorylist.heading('#4', text='Location')
        Inventorylist.heading('#5', text='Purchase Location')
        Inventorylist.heading('#6', text='Quality')
        Inventorylist.heading('#7', text='Quantity')
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
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Items")

            # Add all data to the listbox
            rows = cur.fetchall()
            for row in rows:
                Inventorylist.insert("",tk.END,values=row)

        # Select Row and Edit Row
        def select_record():
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
            Category_entry.insert(0, values[1])
            itemdesc_entry.insert(0, values[2])
            location_entry.insert(0, values[3])
            purchaselocation_entry.insert(0, values[4])
            quality_entry.insert(0, values[5])
            quantity_entry.insert(0, values[6])
            reservation_entry.insert(0, values[7])

        # Update Record
        def update_record():
            conn = lite.connect('DET410 Inventory DB.db')

            cur = conn.cursor()
            selected = Inventorylist.focus()
            # save new data
            Inventorylist.item(selected, text="", values=(id_entry.get(), Category_entry.get(), itemdesc_entry.get(), location_entry.get(),
                                       purchaselocation_entry.get(), quality_entry.get(), quantity_entry.get(),
                                       reservation_entry.get()))
            cur.execute("""UPDATE Items SET
             CatCode = :Category,
             ItemDesc = :itemdesc,
             Location = :location,
             PurchaseLocation = :purchaselocation,
             Quality = :quality,
             Quantity = :quantity,
             Reserved = :reservation
             
             WHERE OID = :OID""",
            {'Category': Category_entry.get(),
             'itemdesc': itemdesc_entry.get(),
             'location': location_entry.get(),
             'purchaselocation': purchaselocation_entry.get(),
             'quality': quality_entry.get(),
             'quantity': quantity_entry.get(),
             'reservation': reservation_entry.get(),
             'OID': id_entry.get()})

            # clear entry boxes
            id_entry.delete(0, END)
            Category_entry.delete(0, END)
            itemdesc_entry.delete(0, END)
            location_entry.delete(0, END)
            purchaselocation_entry.delete(0, END)
            quality_entry.delete(0, END)
            quantity_entry.delete(0, END)
            reservation_entry.delete(0, END)

            # Gets each row and deletes the content of the listbox
            for item in Inventorylist.get_children():
                Inventorylist.delete(item)
            # Calls Back the Contents of the Listbox
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Items")
                rows = cur.fetchall()
                for row in rows:
                    Inventorylist.insert("", tk.END, values=row)

            conn.commit()
            conn.close()

        #adding new rows of data
        def add_record():
            conn = lite.connect('DET410 Inventory DB.db')
            cur = conn.cursor()
            ID = id_entry.get()
            Category = Category_entry.get()
            Itemdesc = itemdesc_entry.get()
            Location = location_entry.get()
            PurchaseLoc = purchaselocation_entry.get()
            Quality = quality_entry.get()
            Quantity = quantity_entry.get()
            Reservation = reservation_entry.get()
            cur.execute('''INSERT INTO Items (ID, CatCode, ItemDesc, Location, PurchaseLocation, Quality, Quantity, Reserved) VALUES
             (?, ?, ?, ?, ?, ?, ?, ?)''',(ID, Category, Itemdesc, Location, PurchaseLoc, Quality, Quantity,Reservation))
            conn.commit()
            conn.close()

            conn = lite.connect('DET410 Inventory DB.db')
            #Gets each row and deletes the content of the listbox
            for item in Inventorylist.get_children():
                Inventorylist.delete(item)
            #Calls Back the Contents of the Listbox
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Items")
                rows = cur.fetchall()
                for row in rows:
                    Inventorylist.insert("", tk.END, values=row)

            conn.close()
            #Searchbar Function
        def search():

            q = entry.get()
            if q == "":
                conn = lite.connect('DET410 Inventory DB.db')
                cur = conn.cursor()

                #refresh
                for item in Inventorylist.get_children():
                    Inventorylist.delete(item)
                # Calls Back the Contents of the Listbox
                with conn:
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Items")
                    rows = cur.fetchall()
                    for row in rows:
                        Inventorylist.insert("", tk.END, values=row)
                conn.close()

            for item in Inventorylist.get_children():

                values = Inventorylist.item(item)['values']
                safe = False
                for i in values:
                    if q in str(i):
                        safe = True

                if not safe:
                    #deleted
                    Inventorylist.delete(item)



        def delete_record():

            def delete():
                conn = lite.connect('DET410 Inventory DB.db')
                cur = conn.cursor()
                #Selected row within the entry boxes set for deletion
                selected = Inventorylist.focus()
                id = Inventorylist.item(selected)['values'][0]

                cur.execute ("DELETE FROM Items Where ID ="+str(id))
                #database delete
                test.destroy()
                # Gets each row and deletes the content of the listbox
                for item in Inventorylist.get_children():
                    Inventorylist.delete(item)

                conn.commit()
                conn.close()

                # Calls Back the Contents of the Listbox

                conn = lite.connect('DET410 Inventory DB.db')
                # Gets each row and deletes the content of the listbox
                for item in Inventorylist.get_children():
                    Inventorylist.delete(item)
                # Calls Back the Contents of the Listbox
                with conn:
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Items")
                    rows = cur.fetchall()
                    for row in rows:
                        Inventorylist.insert("", tk.END, values=row)
            def cancel():
                #do nothing
                test.destroy()
                #Create new prompt box
            test = tk.Toplevel(self.root)

                #Deletion Prompt Box
            l = tk.Label(test, text="Are you sure you want to delete this Item?",font=("Arial", 50),width = 500, height = 2 , bg="black", fg="white", bd=5, relief="ridge" )
            y = tk.Button(test, text="Yes", command=delete, width = 200, height = 2, bg="green", fg="white", bd=5)
            n = tk.Button(test, text="No", command=cancel, width = 200, height = 2, bg="red", fg="white", bd=5)

            l.pack()
            y.pack()
            n.pack()





            # Select Button
        Selectbutton = tk.Button(self.lowerframe, text='SELECT', width=30, height=5, command=select_record)
        Selectbutton.pack(side=tk.LEFT)

        # Create Add button
        Addbutton = tk.Button(self.lowerframe, text='ADD', width=30, height=5, command=add_record)
        Addbutton.pack(side=tk.LEFT)

        # Create Delete Button
        Deletebutton = tk.Button(self.lowerframe, text='DELETE', width=30, height=5, command=delete_record)
        Deletebutton.pack(side=tk.LEFT)

        # Create Edit/Reserve Button
        Editbutton = tk.Button(self.lowerframe, text='EDIT/RESERVE', width=30, height=5,command=update_record)
        Editbutton.pack(side=tk.LEFT)

        # Create search bar
        Searchbutton = tk.Button(self.middleframe, text='Search', command=search, width=30, height=8)
        Searchbutton.pack(side=tk.LEFT)

        entry = tk.Entry(self.middleframe, relief="ridge", width=20, font=('Arial', 40))
        entry.pack(expand=True, fill='y')

    #Close Database
        conn.close()

        # Run the GUI main loop
        self.root.mainloop()
if __name__ == '__main__':
    mainGUI = HeadGUI()

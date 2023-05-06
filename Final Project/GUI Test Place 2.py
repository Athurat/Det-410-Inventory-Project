import sqlite3

conn = sqlite3.connect('database_name.db')

cur = conn.cursor()
cur.execute("SELECT * FROM table_name")

rows = cur.fetchall()

import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

for row in rows:
    listbox.insert(tk.END, row)

root.mainloop()
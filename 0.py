import tkinter as tk

root = tk.Tk()
root.geometry('600x400')
root.state('zoomed')
text = tk.Text(root)
text.pack()
root.mainloop()
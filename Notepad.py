from tkinter import *


def clear_file():
    entry.delete(1.0, END)


def exit_file():
    canvas.destroy()


canvas = Tk()
canvas.geometry('400x600')
canvas.title('Notepad')
canvas.config(bg='white')

top = Frame(canvas)
top.pack(padx=10, pady=5, anchor='nw')


b1 = Button(canvas, text='Clear', bg='white', command=clear_file)
b1.pack(in_=top, side=LEFT)

b2 = Button(canvas, text='Exit', bg='white', command=exit_file)
b2.pack(in_=top, side=LEFT)

entry = Text(canvas, wrap=WORD, bg='#F9DDA4', font=('poppins', 15))
entry.pack(padx=10, pady=5, expand=TRUE, fill=BOTH)

canvas.mainloop()

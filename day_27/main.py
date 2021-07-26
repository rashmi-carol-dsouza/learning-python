import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

#Button


def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())


button = tkinter.Button(text="Click", command=button_clicked)
button.pack()

#Entry



input=tkinter.Entry(width=10)
input.pack()
input.get()

window.mainloop()

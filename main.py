# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *

def button_clicked():
    if input_miles.get() != "":
        lab_km.config(text=str(round(float(input_miles.get()) * 1.60934, 3)))
        print("Calculater")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=700, height=200)
window.config(padx=50, pady=100)

input_miles = Entry(width=10)
input_miles.pack(side="left")

lab_miles = Label(text="Miles is equal to  ", font=("Courier New", 24, "bold"))
lab_miles.pack(side="left", padx=10)

lab_km = Label(text="          ", font=("Courier New", 24, "bold"))
lab_km.pack(side="left")

lab_kmm = Label(text="Km", font=("Courier New", 24, "bold"))
lab_kmm.pack(side="left", padx=20)

button = Button(text="Calculate", command=button_clicked)
button.pack()

# window = Tk()
# window.title("MyFirstGUI")
# window.minsize(width=700,height=300)
# window.config(padx=20,pady=20)
#
# #label
#
# my_label = Label(text="I am a Label", font=("Ariel", 24, "bold"))
# my_label.grid(column=0, row=0)
# my_label.config(padx=100,pady=50)
# #bttn
#
#
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=1,row=1)
#
# button_new = Button(text="Click me Too", command=button_clicked)
# button_new.grid(column=2,row=0)
# #entry
#
# input=Entry(width=10)
# input.grid(column=3, row=2)




window.mainloop()
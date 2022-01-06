from tkinter import *

root = Tk()
root.title("Calculator by Davis Burrill")

entry = Entry(root, width=26, font=("Courier", 28))
entry.grid(row=0, column=0, columnspan=4, pady=10)

def button_click(number):
    #entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_equal():
    answer = entry.get()
    print(14+2)

def button_add():
    answer = entry.get()
    entry.delete(0, END)

def button_sub():
    answer = entry.get()
    print(14+2)

def button_mult():
    answer = entry.get()
    print(14+2)

def button_div():
    answer = entry.get()
    print(14+2)

def button_clear():
    entry.delete(0, END)


num_1 = Button(root, text="1", width=5, pady=5, command=lambda: button_click(1), font=("Courier", 24)).grid(row=3, column=0)
num_2 = Button(root, text="2", width=5, pady=5, command=lambda: button_click(2), font=("Courier", 24)).grid(row=3, column=1)
num_3 = Button(root, text="3", width=5, pady=5, command=lambda: button_click(3), font=("Courier", 24)).grid(row=3, column=2)

num_4 = Button(root, text="4", width=5, pady=5, command=lambda: button_click(4), font=("Courier", 24)).grid(row=2, column=0)
num_5 = Button(root, text="5", width=5, pady=5, command=lambda: button_click(5), font=("Courier", 24)).grid(row=2, column=1)
num_6 = Button(root, text="6", width=5, pady=5, command=lambda: button_click(6), font=("Courier", 24)).grid(row=2, column=2)

num_7 = Button(root, text="7", width=5, pady=5, command=lambda: button_click(7), font=("Courier", 24)).grid(row=1, column=0)
num_8 = Button(root, text="8", width=5, pady=5, command=lambda: button_click(8), font=("Courier", 24)).grid(row=1, column=1)
num_9 = Button(root, text="9", width=5, pady=5, command=lambda: button_click(9), font=("Courier", 24)).grid(row=1, column=2)

num_0 = Button(root, text="0", width=5, pady=5, command=lambda: button_click(0), font=("Courier", 24)).grid(row=4, column=0)
button_AC = Button(root, text="AC", width=5, pady=5, command=button_clear, font=("Courier", 24)).grid(row=4, column=1)
button_equal = Button(root, text="=", width=5, pady=5, command=button_equal, font=("Courier", 24)).grid(row=4, column=2)

button_divide = Button(root, text="÷", width=5, pady=5, command=lambda: button_click("÷"), font=("Courier", 24)).grid(row=1, column=3)
button_multiply= Button(root, text="x", width=5, pady=5, command=lambda: button_click("x"), font=("Courier", 24)).grid(row=2, column=3)
button_minus = Button(root, text="-", width=5, pady=5, command=lambda: button_click("-"), font=("Courier", 24)).grid(row=3, column=3)
button_add = Button(root, text="+", width=5, pady=5, command=lambda: button_click("+"), font=("Courier", 24)).grid(row=4, column=3)

# Main Loop
root.mainloop()





from tkinter import *

root = Tk()
root.title("Calculator by Davis Burrill")

entry = Entry(root, width=16, font=("Courier", 28))
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button Images

# img_one = PhotoImage(file="one.png")
# img_two = PhotoImage(file="two.png")
# img_three = PhotoImage(file="three.png")
# img_four = PhotoImage(file="four.png")
# img_five = PhotoImage(file="five.png")
# img_six = PhotoImage(file="six.png")
# img_seven = PhotoImage(file="seven.png")
# img_eight = PhotoImage(file="eight.png")
# img_nine = PhotoImage(file="nine.png")
# img_zero = PhotoImage(file="zero.png")
# img_decimal = PhotoImage(file="decimal.png")

def button_click(number):
    #entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def equal_button():
    answer = eval(entry.get())
    entry.delete(0,END)
    entry.insert(0, answer)

def clear_button():
    entry.delete(0, END)


num_1 = Button(root, text="1", borderwidth=0, pady=10, padx=10, command=lambda: button_click(1), font=("Courier", 24)).grid(row=4, column=0)
num_2 = Button(root, text="2", borderwidth=0, pady=10, padx=10, command=lambda: button_click(2), font=("Courier", 24)).grid(row=4, column=1)
num_3 = Button(root, text="3", borderwidth=0, pady=10, padx=10, command=lambda: button_click(3), font=("Courier", 24)).grid(row=4, column=2)

num_4 = Button(root, text="4", borderwidth=0, pady=10, padx=10, command=lambda: button_click(4), font=("Courier", 24)).grid(row=3, column=0)
num_5 = Button(root, text="5", borderwidth=0, pady=10, padx=10, command=lambda: button_click(5), font=("Courier", 24)).grid(row=3, column=1)
num_6 = Button(root, text="6", borderwidth=0, pady=10, padx=10, command=lambda: button_click(6), font=("Courier", 24)).grid(row=3, column=2)

num_7 = Button(root, text="7", borderwidth=0, pady=10, padx=10, command=lambda: button_click(7), font=("Courier", 24)).grid(row=2, column=0)
num_8 = Button(root, text="8", borderwidth=0, pady=10, padx=10, command=lambda: button_click(8), font=("Courier", 24)).grid(row=2, column=1)
num_9 = Button(root, text="9", borderwidth=0, pady=10, padx=10, command=lambda: button_click(9), font=("Courier", 24)).grid(row=2, column=2)

num_0 = Button(root, text="0", borderwidth=0, pady=10, padx=10, command=lambda: button_click(0), font=("Courier", 24)).grid(row=5, column=0)
button_dec = Button(root, text=".", borderwidth=0, pady=10, padx=10, command=lambda: button_click("."), font=("Courier", 24)).grid(row=5, column=1)
button_equal = Button(root, text="=", borderwidth=0, pady=10, padx=10, command=equal_button, font=("Courier", 24)).grid(row=5, column=2)

button_divide = Button(root, text="÷", borderwidth=0, pady=10, padx=10, command=lambda: button_click("/"), font=("Courier", 24)).grid(row=2, column=3)
button_multiply= Button(root, text="x", borderwidth=0, pady=10, padx=10, command=lambda: button_click("*"), font=("Courier", 24)).grid(row=3, column=3)
button_minus = Button(root, text="-", borderwidth=0, pady=10, padx=10, command=lambda: button_click("-"), font=("Courier", 24)).grid(row=4, column=3)
button_add = Button(root, text="+", borderwidth=0, pady=10, padx=10, command=lambda: button_click("+"), font=("Courier", 24)).grid(row=5, column=3)

button_par1 = Button(root, text="(", borderwidth=0, pady=10, padx=10, command=lambda: button_click("("), font=("Courier", 24)).grid(row=1, column=0)
button_par2= Button(root, text=")", borderwidth=0, pady=10, padx=10, command=lambda: button_click(")"), font=("Courier", 24)).grid(row=1, column=1)
# Need to make this percent find percent instead of remainder
button_perc = Button(root, text="%", borderwidth=0, pady=10, padx=10, command=lambda: button_click("%"), font=("Courier", 24)).grid(row=1, column=2)
button_AC = Button(root, text="AC", borderwidth=0, pady=10, padx=3, command=clear_button, font=("Courier", 24)).grid(row=1, column=3)

# Main Loop
root.mainloop()





from tkinter import *
import math

numbers = []
full = []


def display_numbers(number, operations):
    global numbers
    global full
    if operations:
        full.append(numbers)
        numbers = []
        
        if number == "AC":
            full = []
            display = Label(main, text = "", font = myFont, anchor = "e", width = 16, bg = "Black", fg = "White").grid(row = 0, column = 0, rowspan = 2, columnspan = 4)

        if number == "=":
            string  = ""
            for i in full:
                if isinstance(i, list):
                    i = "".join(i)
                string += i
            display = Label(main, text = eval(string.replace("AC", "")), font = myFont, anchor = "e", width = 16, bg = "Black", fg = "White").grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
            full = []

        else:
            full.append(number)
            display = Label(main, text = "", font = myFont, anchor = "w", width = 16, bg = "Black", fg = "White").grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
    elif number == "+/-":
        numbers.insert(0,"-")
        display = Label(main, text = "".join(numbers), font = myFont, anchor = "w", width = 16, bg = "Black", fg = "White").grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
    else:
        numbers.append(number)
        display = Label(main, text = "".join(numbers), font = myFont, anchor = "w", width = 16, bg = "Black", fg = "White").grid(row = 0, column = 0, rowspan = 2, columnspan = 4)

main = Tk()
main.config(bg = "Black")
main.title("Calculator")
myFont = ("Helvetica", 20, "bold")

Label(main, text = "\n", font = myFont, bg = "Black", anchor = "w", width = 16).grid(row = 0, column = 0, rowspan = 2, columnspan = 4, sticky = "nsew")

ac = PhotoImage(file = "Operations\AC.png")
change_sign = PhotoImage(file = "Operations\Change Sign.png")
percent = PhotoImage(file = "Operations\Percentage.png")
divide = PhotoImage(file = "Operations\Divide.png")

seven = PhotoImage(file = "Numbers\\7.png")
eight = PhotoImage(file = "Numbers\8.png")
nine = PhotoImage(file = "Numbers\9.png")
times = PhotoImage(file = "Operations\Times.png")

four = PhotoImage(file = "Numbers\\4.png")
five = PhotoImage(file = "Numbers\\5.png")
six = PhotoImage(file = "Numbers\\6.png")
minus = PhotoImage(file = "Operations\Minus.png")

one = PhotoImage(file = "Numbers\\1.png")
two = PhotoImage(file = "Numbers\\2.png")
three = PhotoImage(file = "Numbers\\3.png")
plus = PhotoImage(file = "Operations\Plus.png")

zero = PhotoImage(file = "Numbers\\0.png")
dot = PhotoImage(file = "Operations\Dot.png")
equals = PhotoImage(file = "Operations\Equals.png")


Button(image = ac, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("AC", True)).grid(row = 3, column = 0, padx = 10, pady = 10)
Button(image = change_sign, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("+/-", False)).grid(row = 3, column = 1, padx = 10, pady = 10)
Button(image = percent, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("%", True)).grid(row = 3, column = 2, padx = 10, pady = 10)
Button(image = divide, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("/", True)).grid(row = 3, column = 3, padx = 10, pady = 10)

Button(image = seven, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("7", False)).grid(row = 4, column = 0, padx = 10, pady = 10)
Button(image = eight, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("8", False)).grid(row = 4, column = 1, padx = 10, pady = 10)
Button(image = nine, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("9", False)).grid(row = 4, column = 2, padx = 10, pady = 10)
Button(image = times, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("*", True)).grid(row = 4, column = 3, padx = 10, pady = 10)

Button(image = four, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("4", False)).grid(row = 5, column = 0, padx = 10, pady = 10)
Button(image = five, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("5", False)).grid(row = 5, column = 1, padx = 10, pady = 10)
Button(image = six, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("5", False)).grid(row = 5, column = 2, padx = 10, pady = 10)
Button(image = minus, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("-", True)).grid(row = 5, column = 3, padx = 10, pady = 10)

Button(image = one, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("1", False)).grid(row = 6, column = 0, padx = 10, pady = 10)
Button(image = two, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("2", False)).grid(row = 6, column = 1, padx = 10, pady = 10)
Button(image = three, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("3", False)).grid(row = 6, column = 2, padx = 10, pady = 10)
Button(image = plus, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("+", True)).grid(row = 6, column = 3, padx = 10, pady = 10)

Button(image = zero, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("0", False)).grid(row = 7, column = 0, columnspan = 2, sticky="nsew", padx = 10, pady = 10)
Button(image = dot, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers(".", False)).grid(row = 7, column = 2, padx = 10, pady = 10)
Button(image = equals, bg = "Black", activebackground = "Black", borderwidth = 0, command = lambda: display_numbers("=", True)).grid(row = 7, column = 3, padx = 10, pady = 10)

main.mainloop()
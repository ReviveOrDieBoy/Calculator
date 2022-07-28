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
            display = Label(main, text = "", font = myFont, anchor = "e", width = 14).grid(row = 0, column = 0, rowspan = 2, columnspan = 4)

        if number == "=":
            string  = ""
            for i in full:
                if isinstance(i, list):
                    i = "".join(i)
                string += i
            display = Label(main, text = eval(string.replace("AC", "")), font = myFont, anchor = "e", width = 14).grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
            full = []

        else:
            full.append(number)
            display = Label(main, text = "", font = myFont, anchor = "w", width = 14).grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
    elif number == "+/-":
        numbers.insert(0,"-")
        display = Label(main, text = "".join(numbers), font = myFont, anchor = "w", width = 14).grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
    else:
        numbers.append(number)
        display = Label(main, text = "".join(numbers), font = myFont, anchor = "w", width = 14).grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
#    a = Entry(main)
 #   a.configure(bg="white",fg="grey", relief="flat", state="readonly")
  #  a.insert("end", "world")

main = Tk()
main.config(bg = "Black")
main.title("Calculator")
myFont = ("Helvetica", 20)

Label(main, text = "", font = myFont).grid(row = 0, column = 0, rowspan = 2, columnspan = 4, sticky = "nsew")


Button(main, text = "AC", bg = "dark gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("AC", True)).grid(row = 2, column = 0)
Button(main, text = "+/-", bg = "dark gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("+/-", False)).grid(row = 2, column = 1)
Button(main, text = "%", bg = "dark gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("%", True)).grid(row = 2, column = 2)
Button(main, text = "÷", bg = "Orange", font = myFont, width = 3, height = 1, command = lambda: display_numbers("/", True)).grid(row = 2, column = 3)

Button(main, text = "7", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("7", False)).grid(row = 3, column = 0)
Button(main, text = "8", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("8", False)).grid(row = 3, column = 1)
Button(main, text = "9", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("9", False)).grid(row = 3, column = 2)
Button(main, text = "×", bg = "Orange", font = myFont, width = 3, height = 1, command = lambda: display_numbers("*", True)).grid(row = 3, column = 3)

Button(main, text = "4", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("4", False)).grid(row = 4, column = 0)
Button(main, text = "5", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("5", False)).grid(row = 4, column = 1)
Button(main, text = "6", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("6", False)).grid(row = 4, column = 2)
Button(main, text = "-", bg = "Orange", font = myFont, width = 3, height = 1, command = lambda: display_numbers("-", True)).grid(row = 4, column = 3)

Button(main, text = "1", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("1", False)).grid(row = 5, column = 0)
Button(main, text = "2", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("2", False)).grid(row = 5, column = 1)
Button(main, text = "3", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers("3", False)).grid(row = 5, column = 2)
Button(main, text = "+", bg = "Orange", font = myFont, width = 3, height = 1, command = lambda: display_numbers("+", True)).grid(row = 5, column = 3)

Button(main, text = "0", bg = "gray", font = myFont, height = 1, command = lambda: display_numbers("0", False)).grid(row = 6, column = 0, columnspan = 2, sticky="nsew")
Button(main, text = ".", bg = "gray", font = myFont, width = 3, height = 1, command = lambda: display_numbers(".", False)).grid(row = 6, column = 2)
Button(main, text = "=", bg = "Orange", font = myFont, width = 3, height = 1, command = lambda: display_numbers("=", True)).grid(row = 6, column = 3)

main.mainloop()
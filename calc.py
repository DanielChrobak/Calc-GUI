from tkinter import *
root = Tk()

root.geometry("275x400")

root.minsize(275, 400)

root.maxsize(275, 400)

lst = []

sq = False

err = False

last = ""

out = ""

count = 1

lt = False

def which_button(button_press):
  global sq_num
  global sq
  global sqrt_num
  global err
  global sqrt
  global last
  global screen_len
  global par_find
  global total
  global out
  global lt
  if button_press == "=":
    if sqrt == True:
      calc_screen = screen.cget("text")
      sqrt_screen = calc_screen.rpartition("√"[0])
      total = sqrt_screen[2]
      total = (eval(f"{total} ** 0.5"))
      lt = True
      screen.config(text = total, anchor="se")
      sqrt = False
      last = out
    else:
      out = button_press
      calc_screen = screen.cget("text")
      total = eval(calc_screen)
      lt = True
      screen.config(text = total, anchor="se")
      sqrt = False
      last = out
  elif button_press == "1":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "2":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "3":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "4":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "5":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "6":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "7":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "8":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "9":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == "+":
    screen.config(anchor="nw")
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      last = out
  elif button_press == "-":
    screen.config(anchor="nw")
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      last = out
  elif button_press == "clear":
    screen.config(anchor="nw")
    sq = False
    sqrt = False
    screen.config(text = "", anchor="nw")
    last = out
  elif button_press == "/":
    screen.config(anchor="nw")
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      last = out
  elif button_press == "*":
    screen.config(anchor="nw")
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      last = out
  elif button_press == "(":
    screen.config(anchor="nw")
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      if len(screen.cget("text")) == 0:
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
      else:
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
  elif button_press == ")":
    screen.config(anchor="nw")
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      last = out
  elif button_press == "0":
    screen.config(anchor="nw")
    if lt == True or err == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False or err == False or sqrt or sq == False:
      if last == ")":
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + "*" + out, anchor="nw")
        last = out
      else:
        screen.config(anchor="nw")
        out = button_press
        screen.config(text = screen["text"] + out, anchor="nw")
        last = out
  elif button_press == ".":
    screen.config(anchor="nw")
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + out, anchor="nw")
      last = out
  elif button_press == "sqrt":
    screen.config(anchor="nw")
    sqrt = True
    if lt == True:
      screen.config(text = "", anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + "√", anchor="nw")
      lt = False
      last = out
    elif lt == False:
      screen.config(anchor="nw")
      out = button_press
      screen.config(text = screen["text"] + "√", anchor="nw")
      last = out
  elif button_press == "sq":
    screen.config(anchor="nw")
    calc_screen = screen.cget("text")
    sq_total = eval(f"{calc_screen} * {calc_screen}")
    screen.config(text = sq_total, anchor="se")
    last = out
    lt = True
  else:
    screen.config(text = "ERROR", anchor="center")
    err = True
    

screen = Label(text="", anchor="nw", bg="white", width=29, height=5)
screen.place(x=20,y=25)
root.configure(background="tan")

Title = Label(text="Python Calculator", bg="tan", font="arial")
Title.pack()

QuitButton = Button(text="Close", height = 1, width = 2, command=quit)
QuitButton.place(x = 30, y = 357)

clear = Button(text="Clear", height = 1, width = 2, command=lambda m="clear": which_button(m))
clear.place(x = 200, y = 125)

decimal = Button(root, text=".", height=1, width=2, command=lambda m=".": which_button(m))
decimal.place(x = 143, y = 355)

equals = Button(root, text="=", height=1, width=2, command=lambda m="=": which_button(m))
equals.place(x = 200, y = 355)

zero = Button(root, text="0", height = 1, width = 2, command=lambda m="0": which_button(m))
zero.place(x = 87, y = 355)

one = Button(root, text="1", height = 1, width = 2, command=lambda m="1": which_button(m))
one.place(x = 30, y = 310)

two = Button(root, text="2", height = 1, width = 2, command=lambda m="2": which_button(m))
two.place(x = 87, y = 310)

three = Button(root, text="3", height = 1, width = 2, command=lambda m="3": which_button(m))
three.place(x = 143, y = 310)

four = Button(root, text="4", height = 1, width = 2, command=lambda m="4": which_button(m))
four.place(x = 30, y = 265)

five = Button(root, text="5", height = 1, width = 2, command=lambda m="5": which_button(m))
five.place(x = 87, y = 265)

six = Button(root, text="6", height = 1, width = 2, command=lambda m="6": which_button(m))
six.place(x = 143, y = 265)

seven = Button(root, text="7", height = 1, width = 2, command=lambda m="7": which_button(m))
seven.place(x = 30, y = 220)

eight = Button(root, text="8", height = 1, width = 2, command=lambda m="8": which_button(m))
eight.place(x = 87, y = 220)

nine = Button(root, text="9", height = 1, width = 2, command=lambda m="9": which_button(m))
nine.place(x = 143, y = 220)

plus = Button(root, text="+", height = 1, width = 2, command=lambda m="+": which_button(m))
plus.place(x = 200, y = 310)

minus = Button(root, text="-", height = 1, width = 2, command=lambda m="-": which_button(m))
minus.place(x = 200, y = 265)

divide = Button(root, text="/", height = 1, width = 2, command=lambda m="/": which_button(m))
divide.place(x = 200, y = 220)

multiply = Button(root, text="x", height = 1, width = 2, command=lambda m="*": which_button(m))
multiply.place(x = 200, y = 175)

par_left = Button(root, text="(", height = 1, width = 2, command=lambda m="(": which_button(m))
par_left.place(x = 87, y = 175)

par_right = Button(root, text=")", height = 1, width = 2, command=lambda m=")": which_button(m))
par_right.place(x = 143, y = 175)

square_root = Button(root, text="√", height = 1, width = 2, command=lambda m="sqrt": which_button(m))
square_root.place(x = 30, y = 175)

squared = Button(root, text="x²", height = 1, width = 2, command=lambda m="sq": which_button(m))
squared.place(x = 143, y = 125)

root.mainloop()

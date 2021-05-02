from tkinter import Tk, PhotoImage, Label, Button, Frame
from PIL import Image, ImageTk
import os
import sqlite3
from income import Income_Window
from expenses import Expense_Window
from cashroi import ROI_Window
from db_connect import DB_Connect

# Establish SQLite3 DB connection
db = DB_Connect()


### Set the window ###
root = Tk()
root.geometry("800x633")  # place GUI at x=350, y=10
root.title("Das Kapital - The People's ROI Kalkulator")
root.iconphoto(False, PhotoImage(file="img/commie.png"))


#################################
##### MAIN WINDOW ###############
#################################


splash_img = Image.open('img/splash.jpg')
splash_img = ImageTk.PhotoImage(splash_img)
splash_img_label = Label(root, image=splash_img)
splash_img_label.image = splash_img
splash_img_label.place(x=0, y=0, relwidth=1, relheight=1)

# Icon for Buttons
icon = Image.open("img/commie.png")
icon = ImageTk.PhotoImage(icon)


# Income - Button
inc_button = Button(root, text="OUR Income", font=("orbital", 20),
                    image=icon, compound="left", padx=30, pady=20,
                    wraplength=120, justify="center", borderwidth=10,
                    command=lambda: Income_Window(db))
inc_button.grid(row=1, column=0, pady=75)

# Expenses - Button
inc_button = Button(root, text="OUR Expenses", font=("orbital", 20),
                    image=icon, compound="left", padx=20, pady=20,
                    wraplength=120, justify="center", borderwidth=10,
                    command=lambda: Expense_Window(db))
inc_button.grid(row=1, column=1, pady=75)


# Calculate COCROI - Button
calc_button = Button(root, text="Calculate OUR Cash ROI", font=("orbital", 20),
                     image=icon, compound="left", padx=135, pady=20,
                     wraplength=200, justify="center", borderwidth=10,
                     command=lambda: ROI_Window(db))
calc_button.grid(row=2, column=0, columnspan=2)


#################################
######HEADER AREA################
#################################

# Main window occurs BEFORE the header,
# otherwise there are layering conflicts. Main window sets the background
# for the entire window, as Tkinter doesn't support bg images in frames.

# header area - create frame
header = Frame(root, width=800, height=100, bg="red4")
header.grid(columnspan=2, row=0)


# header - place photo
banner_img = Image.open('img/header.png')
banner_img = ImageTk.PhotoImage(banner_img)
banner_img_label = Label(header, image=banner_img)
banner_img_label.image = banner_img
banner_img_label.grid(column=0, row=0)


# Terminate the window
root.mainloop()

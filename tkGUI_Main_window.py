from tkinter import *
from PIL import Image, ImageTk
import os
import sqlite3
import dbwriter
import income
import expenses
import cashroi


# Delete old SQLite3 Database if existant
if os.path.exists("my_property.db"):
    os.remove("my_property.db")

# Esatblish a connection to SQLite DB
conn = sqlite3.connect("my_property.db")
db_curs = conn.cursor()

# Write database tables
#table1 - Revenue
db_curs.execute("""CREATE TABLE income (
            rental_income integer,
            laundry_income integer,
            storage_income integer,
            misc_income integer)""")
#table2 - Expenses
db_curs.execute("""CREATE TABLE expenses (
            tax_exp integer,
            insurance_exp integer,
            utility_exp integer,
            hoa_fees integer,
            lawn_exp integer,
            vacancy_exp integer,
            repair_exp integer,
            capex_exp integer,
            property_man integer,
            mortgage_integer 
            )   """)

#table3 - Investment
db_curs.execute("""CREATE TABLE investment (
            down_pay integer,
            closing_cost integer,
            rehab_cost integer,
            misc integer
            )""")

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
                    image=icon, compound=LEFT, padx=30, pady=20,
                    wraplength=120, justify="center", borderwidth=10,
                    command=lambda: launch_income_window())
inc_button.grid(row=1, column=0, pady=75)


def launch_income_window():
    inc_window = income.Income_Window(db_curs)


# Expenses - Button
inc_button = Button(root, text="OUR Expenses", font=("orbital", 20),
                    image=icon, compound=LEFT, padx=20, pady=20,
                    wraplength=120, justify="center", borderwidth=10,
                    command=lambda: launch_expense_window())
inc_button.grid(row=1, column=1, pady=75)


def launch_expense_window():
    exp_window = expenses.Expense_Window(db_curs)


# Calculate COCROI - Button
calc_button = Button(root, text="Calculate OUR Cash ROI", font=("orbital", 20),
                     image=icon, compound=LEFT, padx=135, pady=20,
                     wraplength=200, justify="center", borderwidth=10,
                     command=lambda: launch_ROI_window())


def launch_ROI_window():
    ROI_window = cashroi.ROI_Window(db_curs)


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

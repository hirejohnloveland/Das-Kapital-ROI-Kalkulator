from tkinter import Tk, PhotoImage, Label, Button, Frame
from PIL import Image, ImageTk
import os
import sqlite3
from income import Income_Window
from expenses import Expense_Window
from invest import Invest_Window
from db_connect import DB_Connect


class GUI():
    """Create the GUI main window and associated objects"""

    def __init__(self, db):
        self.db = db
        self.root = Tk()
        self.__create_window()
        self.splash_img = self.__draw_splash_image()
        self.icon = self.__get_button_icons()
        self.income_button = self.__income_button()
        self.expense_button = self.__expense_button()
        self.roi_button = self.__roi_button()
        self.__stack_header_on_top()
        self.root.mainloop()

    def __create_window(self):
        ### Set the window ###
        self.root.geometry("800x633")  # place GUI at x=350, y=10
        self.root.title(
            "Das Kapital - The People's ROI Kalkulator")
        self.root.iconphoto(False, PhotoImage(file="img/commie.png"))

    # Generate the splash

    def __draw_splash_image(self):
        splash_img = Image.open('img/splash.jpg')
        splash_img = ImageTk.PhotoImage(splash_img)
        splash_img_label = Label(self.root, image=splash_img)
        splash_img_label.image = splash_img
        splash_img_label.place(x=0, y=0, relwidth=1, relheight=1)
        return splash_img_label

    def __get_button_icons(self):
        # Icon for Buttons
        icon = Image.open("img/commie.png")
        icon = ImageTk.PhotoImage(icon)
        return icon

    def __income_button(self):
        button = Button(self.root, text="OUR Income", font=("orbital", 20),
                        image=self.icon, compound="left", padx=30, pady=20,
                        wraplength=120, justify="center", borderwidth=10,
                        command=lambda: Income_Window(self.db))
        button.grid(row=1, column=0, pady=75)
        return button

    def __expense_button(self):
        button = Button(self.root, text="OUR Expenses", font=("orbital", 20),
                        image=self.icon, compound="left", padx=20, pady=20,
                        wraplength=120, justify="center", borderwidth=10,
                        command=lambda: Expense_Window(self.db))
        button.grid(row=1, column=1, pady=75)
        return button

    def __roi_button(self):
        button = Button(self.root, text="Calculate OUR Cash ROI", font=("orbital", 20),
                        image=self.icon, compound="left", padx=135, pady=20,
                        wraplength=200, justify="center", borderwidth=10,
                        command=lambda: Invest_Window(self.db))
        button.grid(row=2, column=0, columnspan=2)
        return button

    # Main window occurs BEFORE the header,
    # otherwise there are layering conflicts. Main window sets the background
    # for the entire window, as Tkinter doesn't support bg images in frames.
    def __stack_header_on_top(self):

        # header area - create frame
        header = Frame(self.root, width=800, height=100, bg="red4")
        header.grid(columnspan=2, row=0)

        # header - place photo
        banner_img = Image.open('img/header.png')
        banner_img = ImageTk.PhotoImage(banner_img)
        banner_img_label = Label(header, image=banner_img)
        banner_img_label.image = banner_img
        banner_img_label.grid(column=0, row=0)

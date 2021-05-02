from tkinter import Label, Entry, Button, Toplevel, E, W, DISABLED, NORMAL
import db_connect


class Income_Window():
    def __init__(self, db):
        self.db = db
        self.top = Toplevel()
        self.rental_inc_lbl = self.__rental_inc_lbl()
        self.rental_inc_box = self.__rental_inc_box()
        self.laundry_inc_lbl = self.__laundry_inc_lbl()
        self.laundry_inc_box = self.__laundry_inc_box()
        self.storage_inc_lbl = self.__storage_inc_lbl()
        self.storage_inc_box = self.__storage_inc_box()
        self.misc_inc_lbl = self.__misc_inc_lbl()
        self.misc_inc_box = self.__misc_inc_box()
        self.total_inc_lbl = self.__total_inc_lbl()
        self.total_inc_box = self.__total_inc_box()
        self.calc_btn = self.__calc_btn()
        self.proceed_btn = self.__proceed_btn()

    def __rental_inc_lbl(self):
        label = Label(self.top, text="Monthly Rental Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=0, column=0, sticky=E)
        return label

    def __rental_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=0, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def __laundry_inc_lbl(self):
        label = Label(self.top, text="Monthly Laundry Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=1, column=0, sticky=E)
        return label

    def __laundry_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=1, column=1, padx=10, sticky=W)
        return box

    def __storage_inc_lbl(self):
        label = Label(self.top, text="Monthly Storage Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=3, column=0, sticky=E)
        return label

    def __storage_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=3, column=1, padx=10, sticky=W)
        return box

    def __misc_inc_lbl(self):
        label = Label(self.top, text="Monthly Misc. Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=4, column=0, sticky=E)
        return label

    def __misc_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=4, column=1, padx=10, sticky=W)
        return box

    def __total_inc_lbl(self):
        label = Label(self.top, text="Monthly Total Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=5, column=0, sticky=E)
        return label

    def __total_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=5, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def __calc_btn(self):
        button = Button(
            self.top, text="Calculate Monthly Total Income", wraplength=120, padx=40, borderwidth=4, command=lambda: self.update())
        button.grid(row=6, column=0, pady=5, padx=5)
        return button

    def __proceed_btn(self):
        button = Button(
            self.top, text="Back to main Menu", wraplength=80, padx=40, borderwidth=4, command=lambda: self.top.destroy())
        button.grid(row=6, column=1, padx=5, pady=20)
        return button

    def update(self):
        self.submit_calc()
        total_value = self.query()
        self.total_inc_box_update(total_value)

    def submit_calc(self):
        income_dict = {
            0: self.rental_inc_box.get(),
            1: self.laundry_inc_box.get(),
            2: self.storage_inc_box.get(),
            3: self.misc_inc_box.get()
        }
        self.db.insert_income(income_dict)

    def query(self):
        recordset = self.db.income_query()
        result = sum([int(i) for i in recordset[0]])
        return result

    def total_inc_box_update(self, value):
        self.total_inc_box["state"] = NORMAL
        self.total_inc_box.insert(0, value)
        self.total_inc_box["state"] = DISABLED

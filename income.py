from tkinter import Label, Entry, Button, Toplevel, E, W, DISABLED, NORMAL, messagebox
import db_connect


class Income_Window():
    """Create the income window and it's fields and methods"""

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
        self.__populate_boxes()
        self.__update_fields()

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
            self.top, text="Calculate Monthly Total Income", wraplength=120, padx=40, borderwidth=4, command=lambda: self.__update_fields())
        button.grid(row=6, column=0, pady=5, padx=5)
        return button

    def __proceed_btn(self):
        button = Button(
            self.top, text="Back to main Menu", wraplength=80, padx=40, borderwidth=4, command=lambda: self.top.destroy())
        button.grid(row=6, column=1, padx=5, pady=20)
        return button

    ########################################################
    ##########Functions to update window fields#############
    ########################################################

    def __update_fields(self):
        try:
            self.__update_db()
            self.__delete_boxes()
            self.__populate_boxes()
        except:
            messagebox.showwarning(title="Input Error",
                                   message="Only whole numbers are allowed for input!")
            self.top.lift()

    def __populate_boxes(self):
        recordset = self.db.income_query()
        record_list = [x for x in recordset[0]]
        self.rental_inc_box.insert(0, record_list[0])
        self.rental_inc_box.select_range(0, "end")
        self.laundry_inc_box.insert(0, record_list[1])
        self.storage_inc_box.insert(0, record_list[2])
        self.misc_inc_box.insert(0, record_list[3])
        self.total_inc_box.insert(0, self.__get_total_income())
        self.total_inc_box["state"] = DISABLED

    def __delete_boxes(self):
        self.rental_inc_box.delete(0, "end")
        self.laundry_inc_box.delete(0, "end")
        self.storage_inc_box.delete(0, "end")
        self.misc_inc_box.delete(0, "end")
        self.total_inc_box["state"] = NORMAL
        self.total_inc_box.delete(0, "end")

    ########################################################
    ########## Database Calls###############################
    ########################################################

    def __get_total_income(self):
        recordset = self.db.income_query()
        result = sum([int(i) for i in recordset[0]])
        return result

    def __update_db(self):
        income_dict = {
            0: int(self.rental_inc_box.get()),
            1: int(self.laundry_inc_box.get()),
            2: int(self.storage_inc_box.get()),
            3: int(self.misc_inc_box.get())
        }
        self.db.update_income(income_dict)
        self.db.update_income()

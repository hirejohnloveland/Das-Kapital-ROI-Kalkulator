from tkinter import *


class Income_Window():
    def __init__(self, cursor):
        self.cursor = cursor
        self.top = Toplevel()
        self.rental_inc_lbl = self.rental_inc_lbl()
        self.rental_inc_box = self.rental_inc_box()
        self.laundry_inc_lbl = self.laundry_inc_lbl()
        self.laundry_inc_box = self.laundry_inc_box()
        self.storage_inc_lbl = self.storage_inc_lbl()
        self.storage_inc_box = self.storage_inc_box()
        self.misc_inc_lbl = self.misc_inc_lbl()
        self.misc_inc_box = self.misc_inc_box()
        self.total_inc_lbl = self.total_inc_lbl()
        self.total_inc_box = self.total_inc_box()
        self.calc_btn = self.calc_btn()
        self.proceed_btn = self.proceed_btn()

    def rental_inc_lbl(self):
        label = Label(self.top, text="Monthly Rental Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=0, column=0, sticky=E)
        return label

    def rental_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=0, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def laundry_inc_lbl(self):
        label = Label(self.top, text="Monthly Laundry Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=1, column=0, sticky=E)
        return label

    def laundry_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=1, column=1, padx=10, sticky=W)
        return box

    def storage_inc_lbl(self):
        label = Label(self.top, text="Monthly Storage Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=3, column=0, sticky=E)
        return label

    def storage_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=3, column=1, padx=10, sticky=W)
        return box

    def misc_inc_lbl(self):
        label = Label(self.top, text="Monthly Misc. Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=4, column=0, sticky=E)
        return label

    def misc_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=4, column=1, padx=10, sticky=W)
        return box

    def total_inc_lbl(self):
        label = Label(self.top, text="Monthly Total Income:",
                      padx=10, pady=5, justify="right")
        label.grid(row=5, column=0, sticky=E)
        return label

    def total_inc_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=5, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def calc_btn(self):
        button = Button(
            self.top, text="Calculate Monthly Total Income", wraplength=120, padx=40, borderwidth=4, command=lambda: self.update())
        button.grid(row=6, column=0, pady=5, padx=5)
        return button

    def proceed_btn(self):
        button = Button(
            self.top, text="Back to main Menu", wraplength=80, padx=40, borderwidth=4, command=lambda: self.top.destroy())
        button.grid(row=6, column=1, padx=5, pady=20)
        return button

    def update(self):
        self.submit_calc()
        total_value = self.query()
        self.total_inc_box_update(total_value)

    def submit_calc(self):
        self.cursor.execute("INSERT INTO income VALUES (:rental_inc, :laund_inc, :stor_inc, :misc_inc)",
                            {
                                'rental_inc': self.rental_inc_box.get(),
                                'laund_inc': self.laundry_inc_box.get(),
                                'stor_inc': self.storage_inc_box.get(),
                                'misc_inc': self.misc_inc_box.get()
                            })

    def query(self):
        self.cursor.execute("SELECT * FROM income")
        recordset = self.cursor.fetchall()
        result = sum([int(i) for i in recordset[0]])
        return result

    def total_inc_box_update(self, value):
        self.total_inc_box["state"] = NORMAL
        self.total_inc_box.insert(0, value)
        self.total_inc_box["state"] = DISABLED

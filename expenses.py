from tkinter import *


class Expense_Window():
    def __init__(self, cursor):
        self.cursor = cursor
        self.top = Toplevel()
        self.tax_exp_lbl = self.tax_exp_lbl()
        self.tax_exp_box = self.tax_exp_box()
        self.insurance_exp_lbl = self.insurance_exp_lbl()
        self.insurance_exp_box = self.insurance_exp_box()
        self.utilities_exp_lbl = self.utilities_exp_lbl()
        self.utilities_exp_box = self.utilities_exp_box()
        self.hoa_exp_lbl = self.hoa_exp_lbl()
        self.hoa_exp_box = self.hoa_exp_box()
        self.lawn_exp_lbl = self.lawn_exp_lbl()
        self.lawn_exp_box = self.lawn_exp_box()
        self.vacancy_exp_lbl = self.vacancy_exp_lbl()
        self.vacancy_exp_box = self.vacancy_exp_box()
        self.repair_exp_lbl = self.repair_exp_lbl()
        self.repair_exp_box = self.repair_exp_box()
        self.capex_exp_lbl = self.capex_exp_lbl()
        self.capex_exp_box = self.capex_exp_box()
        self.prop_man_exp_lbl = self.prop_man_exp_lbl()
        self.prop_man_exp_box = self.prop_man_exp_box()
        self.mortgage_exp_lbl = self.mortgage_exp_lbl()
        self.mortgage_exp_box = self.mortgage_exp_box()
        self.total_exp_lbl = self.total_exp_lbl()
        self.total_exp_box = self.total_exp_box()
        self.calc_btn = self.calc_btn()
        self.proceed_btn = self.proceed_btn()

    def tax_exp_lbl(self):
        label = Label(self.top, text="Monthly Tax Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=0, column=0, sticky=E)
        return label

    def tax_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=0, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def insurance_exp_lbl(self):
        label = Label(self.top, text="Monthly Insurance Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=1, column=0, sticky=E)
        return label

    def insurance_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=1, column=1, padx=10, sticky=W)
        return box

    def utilities_exp_lbl(self):
        label = Label(self.top, text="Monthly Utilities Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=2, column=0, sticky=E)
        return label

    def utilities_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=2, column=1, padx=10, sticky=W)
        return box

    def hoa_exp_lbl(self):
        label = Label(self.top, text="Monthly HOA Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=3, column=0, sticky=E)
        return label

    def hoa_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=3, column=1, padx=10, sticky=W)
        return box

    def lawn_exp_lbl(self):
        label = Label(self.top, text="Monthly Lawn Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=4, column=0, sticky=E)
        return label

    def lawn_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=4, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def vacancy_exp_lbl(self):
        label = Label(self.top, text="Monthly Vacancy Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=5, column=0, sticky=E)
        return label

    def vacancy_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=5, column=1, padx=10, sticky=W)
        return box

    def repair_exp_lbl(self):
        label = Label(self.top, text="Monthly Repair Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=6, column=0, sticky=E)
        return label

    def repair_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=6, column=1, padx=10, sticky=W)
        return box

    def capex_exp_lbl(self):
        label = Label(self.top, text="Monthly CAPEX:",
                      padx=10, pady=5, justify="right")
        label.grid(row=7, column=0, sticky=E)
        return label

    def capex_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=7, column=1, padx=10, sticky=W)
        return box

    def prop_man_exp_lbl(self):
        label = Label(self.top, text="Monthly Prop MGMT Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=8, column=0, sticky=E)
        return label

    def prop_man_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=8, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def mortgage_exp_lbl(self):
        label = Label(self.top, text="Monthly Mortgage Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=9, column=0, sticky=E)
        return label

    def mortgage_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=9, column=1, padx=10, sticky=W)
        return box

    def total_exp_lbl(self):
        label = Label(self.top, text="Monthly Total Expenses:",
                      padx=10, pady=5, justify="right")
        label.grid(row=10, column=0, sticky=E)
        return label

    def total_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=10, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def calc_btn(self):
        button = Button(
            self.top, text="Calculate Monthly Total Expenses", wraplength=120, padx=40, borderwidth=4, command=lambda: self.update())
        button.grid(row=11, column=0, pady=5, padx=5)
        return button

    def proceed_btn(self):
        button = Button(
            self.top, text="Back to main Menu", wraplength=80, padx=40, borderwidth=4, command=lambda: self.top.destroy())
        button.grid(row=11, column=1, padx=5, pady=20)
        return button

    def update(self):
        self.submit_calc()
        total_value = self.query()
        self.total_exp_box_update(total_value)

    def submit_calc(self):
        self.cursor.execute("INSERT INTO expenses VALUES (:tax,:ins,:util,:hoa,:lawn,:vac,:rep,:capex,:mgmt,:mort)",
                            {
                                "tax": self.tax_exp_box.get(),
                                "ins": self.insurance_exp_box.get(),
                                "util": self.utilities_exp_box.get(),
                                "hoa": self.hoa_exp_box.get(),
                                "lawn": self.lawn_exp_box.get(),
                                "vac": self.vacancy_exp_box.get(),
                                "rep": self.repair_exp_box.get(),
                                "capex": self.capex_exp_box.get(),
                                "mgmt": self.prop_man_exp_box.get(),
                                "mort": self.mortgage_exp_box.get(),
                            })

    def query(self):
        self.cursor.execute("SELECT * FROM expenses")
        recordset = self.cursor.fetchall()
        result = sum([int(i) for i in recordset[0]])
        return result

    def total_exp_box_update(self, value):
        self.total_exp_box["state"] = NORMAL
        self.total_exp_box.insert(0, value)
        self.total_exp_box["state"] = DISABLED

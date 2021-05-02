from tkinter import *


class ROI_Window():
    def __init__(self, cursor):
        self.cursor = cursor
        self.top = Toplevel()
        self.down_pay_lbl = self.down_pay_lbl()
        self.down_pay_box = self.down_pay_box()
        self.close_cost_lbl = self.close_cost_lbl()
        self.close_cost_box = self.close_cost_box()
        self.rehab_exp_lbl = self.rehab_exp_lbl()
        self.rehab_exp_box = self.rehab_exp_box()
        self.misc_exp_lbl = self.misc_exp_lbl()
        self.misc_exp_box = self.misc_exp_box()
        self.total_inv_lbl = self.total_inv_lbl()
        self.total_inv_box = self.total_inv_box()
        self.cash_flow_lbl = self.cash_flow_lbl()
        self.cash_flow_box = self.cash_flow_box()
        self.cash_ROI_lbl = self.cash_ROI_lbl()
        self.cash_ROI_box = self.cash_ROI_box()
        self.calc_btn = self.calc_btn()
        self.proceed_btn = self.proceed_btn()

    def down_pay_lbl(self):
        label = Label(self.top, text="Down Payment:",
                      padx=10, pady=5, justify="right")
        label.grid(row=0, column=0, sticky=E)
        return label

    def down_pay_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=0, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def close_cost_lbl(self):
        label = Label(self.top, text="Closing Costs:",
                      padx=10, pady=5, justify="right")
        label.grid(row=1, column=0, sticky=E)
        return label

    def close_cost_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=1, column=1, padx=10, sticky=W)
        return box

    def rehab_exp_lbl(self):
        label = Label(self.top, text="Rehabilitation Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=2, column=0, sticky=E)
        return label

    def rehab_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=2, column=1, padx=10, sticky=W)
        return box

    def misc_exp_lbl(self):
        label = Label(self.top, text="Misc. Investment:",
                      padx=10, pady=5, justify="right")
        label.grid(row=3, column=0, sticky=E)
        return label

    def misc_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=3, column=1, padx=10, sticky=W)
        return box

    def total_inv_lbl(self):
        label = Label(self.top, text="Total Investment:",
                      padx=10, pady=5, justify="right")
        label.grid(row=4, column=0, sticky=E)
        return label

    def total_inv_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=4, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def cash_flow_lbl(self):
        label = Label(self.top, text="Annual Cash Flow:",
                      padx=10, pady=5, justify="right")
        label.grid(row=5, column=0, sticky=E)
        return label

    def cash_flow_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=5, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def cash_ROI_lbl(self):
        label = Label(self.top, text="Annual ROI %:",
                      padx=10, pady=5, justify="right")
        label.grid(row=7, column=0, sticky=E)
        return label

    def cash_ROI_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=7, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def calc_btn(self):
        button = Button(
            self.top, text="Calculate Total Investment", wraplength=120, padx=40, borderwidth=4, command=lambda: self.update())
        button.grid(row=8, column=0, pady=5, padx=5)
        return button

    def proceed_btn(self):
        button = Button(
            self.top, text="Back to main Menu", wraplength=80, padx=40, borderwidth=4, command=lambda: self.top.destroy())
        button.grid(row=8, column=1, padx=5, pady=20)
        return button

    def update(self):
        # Return Total Investment from DB, update box
        self.submit_calc()
        total_investment = self.investment_query()
        self.total_inv_box_update(total_investment)

        # Return cash flow from DB, calculate annual CF, update box
        ann_income = self.income_query() * 12
        ann_exp = self.expense_query() * 12
        ann_cash_flow = ann_income-ann_exp
        self.cash_flow_box_update(ann_cash_flow)
        cash_ROI = ann_cash_flow / total_investment
        print(cash_ROI)
        cash_ROI_string = "{:.2%}".format(cash_ROI)
        self.cash_ROI_box_update(cash_ROI_string)

    def submit_calc(self):
        self.cursor.execute("INSERT INTO investment VALUES (:dp,:close,:rehab,:misc)",
                            {
                                "dp": self.down_pay_box.get(),
                                "close": self.close_cost_box.get(),
                                "rehab": self.rehab_exp_box.get(),
                                "misc": self.misc_exp_box.get()
                            })

    def investment_query(self):
        self.cursor.execute("SELECT * FROM investment")
        recordset = self.cursor.fetchall()
        result = sum([int(i) for i in recordset[0]])
        return result

    def income_query(self):
        self.cursor.execute("SELECT * FROM income")
        recordset = self.cursor.fetchall()
        result = sum([int(i) for i in recordset[0]])
        return result

    def expense_query(self):
        self.cursor.execute("SELECT * FROM expenses")
        recordset = self.cursor.fetchall()
        result = sum([int(i) for i in recordset[0]])
        result
        return result

    def total_inv_box_update(self, value):
        self.total_inv_box["state"] = NORMAL
        self.total_inv_box.insert(0, value)
        self.total_inv_box["state"] = DISABLED

    def cash_flow_box_update(self, value):
        self.cash_flow_box["state"] = NORMAL
        self.cash_flow_box.insert(0, value)
        self.cash_flow_box["state"] = DISABLED

    def cash_ROI_box_update(self, value):
        self.cash_ROI_box["state"] = NORMAL
        self.cash_ROI_box.insert(0, value)
        self.cash_ROI_box["state"] = DISABLED

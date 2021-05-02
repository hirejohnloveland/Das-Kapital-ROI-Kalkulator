from tkinter import Label, Entry, Button, Toplevel, E, W, DISABLED, NORMAL
import db_connect


class ROI_Window():
    def __init__(self, db):
        self.db = db
        self.top = Toplevel()
        self.down_pay_lbl = self.__down_pay_lbl()
        self.down_pay_box = self.__down_pay_box()
        self.close_cost_lbl = self.__close_cost_lbl()
        self.close_cost_box = self.__close_cost_box()
        self.rehab_exp_lbl = self.__rehab_exp_lbl()
        self.rehab_exp_box = self.__rehab_exp_box()
        self.misc_exp_lbl = self.__misc_exp_lbl()
        self.misc_exp_box = self.__misc_exp_box()
        self.total_inv_lbl = self.__total_inv_lbl()
        self.total_inv_box = self.__total_inv_box()
        self.cash_flow_lbl = self.__cash_flow_lbl()
        self.cash_flow_box = self.__cash_flow_box()
        self.cash_ROI_lbl = self.__cash_ROI_lbl()
        self.cash_ROI_box = self.__cash_ROI_box()
        self.calc_btn = self.__calc_btn()
        self.proceed_btn = self.__proceed_btn()

    def __down_pay_lbl(self):
        label = Label(self.top, text="Down Payment:",
                      padx=10, pady=5, justify="right")
        label.grid(row=0, column=0, sticky=E)
        return label

    def __down_pay_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=0, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def __close_cost_lbl(self):
        label = Label(self.top, text="Closing Costs:",
                      padx=10, pady=5, justify="right")
        label.grid(row=1, column=0, sticky=E)
        return label

    def __close_cost_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=1, column=1, padx=10, sticky=W)
        return box

    def __rehab_exp_lbl(self):
        label = Label(self.top, text="Rehabilitation Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=2, column=0, sticky=E)
        return label

    def __rehab_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=2, column=1, padx=10, sticky=W)
        return box

    def __misc_exp_lbl(self):
        label = Label(self.top, text="Misc. Investment:",
                      padx=10, pady=5, justify="right")
        label.grid(row=3, column=0, sticky=E)
        return label

    def __misc_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=3, column=1, padx=10, sticky=W)
        return box

    def __total_inv_lbl(self):
        label = Label(self.top, text="Total Investment:",
                      padx=10, pady=5, justify="right")
        label.grid(row=4, column=0, sticky=E)
        return label

    def __total_inv_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=4, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def __cash_flow_lbl(self):
        label = Label(self.top, text="Annual Cash Flow:",
                      padx=10, pady=5, justify="right")
        label.grid(row=5, column=0, sticky=E)
        return label

    def __cash_flow_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=5, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def __cash_ROI_lbl(self):
        label = Label(self.top, text="Annual ROI %:",
                      padx=10, pady=5, justify="right")
        label.grid(row=7, column=0, sticky=E)
        return label

    def __cash_ROI_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=7, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def __calc_btn(self):
        button = Button(
            self.top, text="Calculate Total Investment", wraplength=120, padx=40, borderwidth=4, command=lambda: self.update())
        button.grid(row=8, column=0, pady=5, padx=5)
        return button

    def __proceed_btn(self):
        button = Button(
            self.top, text="Back to main Menu", wraplength=80, padx=40, borderwidth=4, command=lambda: self.top.destroy())
        button.grid(row=8, column=1, padx=5, pady=20)
        return button

    def update(self):
        # Return Total Investment from DB, update box
        self.submit_calc()
        total_investment = self.query()
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
        investment_dict = {
            0: self.down_pay_box.get(),
            1: self.close_cost_box.get(),
            2: self.rehab_exp_box.get(),
            3: self.misc_exp_box.get()
        }
        self.db.insert_investment(investment_dict)

    def query(self):
        recordset = self.db.investment_query()
        result = sum([int(i) for i in recordset[0]])
        return result

    def income_query(self):
        recordset = self.db.income_query()
        result = sum([int(i) for i in recordset[0]])
        return result

    def expense_query(self):
        recordset = self.db.expense_query()
        result = sum([int(i) for i in recordset[0]])
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

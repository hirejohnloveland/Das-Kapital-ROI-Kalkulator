from tkinter import Label, Entry, Button, Toplevel, E, W, DISABLED, NORMAL, messagebox, PhotoImage
import db_connect


class Expense_Window():
    def __init__(self, db):
        self.db = db
        self.top = Toplevel()
        self.__draw_window()
        self.tax_exp_lbl = self.__tax_exp_lbl()
        self.tax_exp_box = self.__tax_exp_box()
        self.insurance_exp_lbl = self.__insurance_exp_lbl()
        self.insurance_exp_box = self.__insurance_exp_box()
        self.utilities_exp_lbl = self.__utilities_exp_lbl()
        self.utilities_exp_box = self.__utilities_exp_box()
        self.hoa_exp_lbl = self.__hoa_exp_lbl()
        self.hoa_exp_box = self.__hoa_exp_box()
        self.lawn_exp_lbl = self.__lawn_exp_lbl()
        self.lawn_exp_box = self.__lawn_exp_box()
        self.vacancy_exp_lbl = self.__vacancy_exp_lbl()
        self.vacancy_exp_box = self.__vacancy_exp_box()
        self.repair_exp_lbl = self.__repair_exp_lbl()
        self.repair_exp_box = self.__repair_exp_box()
        self.capex_exp_lbl = self.__capex_exp_lbl()
        self.capex_exp_box = self.__capex_exp_box()
        self.prop_man_exp_lbl = self.__prop_man_exp_lbl()
        self.prop_man_exp_box = self.__prop_man_exp_box()
        self.mortgage_exp_lbl = self.__mortgage_exp_lbl()
        self.mortgage_exp_box = self.__mortgage_exp_box()
        self.total_exp_lbl = self.__total_exp_lbl()
        self.total_exp_box = self.__total_exp_box()
        self.calc_btn = self.__calc_btn()
        self.proceed_btn = self.__proceed_btn()
        self.__populate_boxes()
        self.__update_fields()

    def __draw_window(self):
        self.top.title(
            "Enter OUR Expenses")
        self.top.iconphoto(False, PhotoImage(file="img/commie.png"))

    def __tax_exp_lbl(self):
        label = Label(self.top, text="Monthly Tax Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=0, column=0, sticky=E)
        return label

    def __tax_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=0, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def __insurance_exp_lbl(self):
        label = Label(self.top, text="Monthly Insurance Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=1, column=0, sticky=E)
        return label

    def __insurance_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=1, column=1, padx=10, sticky=W)
        return box

    def __utilities_exp_lbl(self):
        label = Label(self.top, text="Monthly Utilities Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=2, column=0, sticky=E)
        return label

    def __utilities_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=2, column=1, padx=10, sticky=W)
        return box

    def __hoa_exp_lbl(self):
        label = Label(self.top, text="Monthly HOA Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=3, column=0, sticky=E)
        return label

    def __hoa_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=3, column=1, padx=10, sticky=W)
        return box

    def __lawn_exp_lbl(self):
        label = Label(self.top, text="Monthly Lawn Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=4, column=0, sticky=E)
        return label

    def __lawn_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=4, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def __vacancy_exp_lbl(self):
        label = Label(self.top, text="Monthly Vacancy Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=5, column=0, sticky=E)
        return label

    def __vacancy_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=5, column=1, padx=10, sticky=W)
        return box

    def __repair_exp_lbl(self):
        label = Label(self.top, text="Monthly Repair Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=6, column=0, sticky=E)
        return label

    def __repair_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=6, column=1, padx=10, sticky=W)
        return box

    def __capex_exp_lbl(self):
        label = Label(self.top, text="Monthly CAPEX:",
                      padx=10, pady=5, justify="right")
        label.grid(row=7, column=0, sticky=E)
        return label

    def __capex_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=7, column=1, padx=10, sticky=W)
        return box

    def __prop_man_exp_lbl(self):
        label = Label(self.top, text="Monthly Prop MGMT Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=8, column=0, sticky=E)
        return label

    def __prop_man_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=8, column=1, padx=10, sticky=W)
        box.focus_set()
        return box

    def __mortgage_exp_lbl(self):
        label = Label(self.top, text="Monthly Mortgage Expense:",
                      padx=10, pady=5, justify="right")
        label.grid(row=9, column=0, sticky=E)
        return label

    def __mortgage_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=9, column=1, padx=10, sticky=W)
        return box

    def __total_exp_lbl(self):
        label = Label(self.top, text="Monthly Total Expenses:",
                      padx=10, pady=5, justify="right")
        label.grid(row=10, column=0, sticky=E)
        return label

    def __total_exp_box(self):
        box = Entry(self.top, width=8)
        box.grid(row=10, column=1, padx=10, sticky=W)
        # box is calculated on refresh when user clicks calc button
        box["state"] = DISABLED
        return box

    def __calc_btn(self):
        button = Button(
            self.top, text="Calculate Monthly Total Expenses", wraplength=120, padx=40, borderwidth=4, command=lambda: self.__update_fields())
        button.grid(row=11, column=0, pady=5, padx=5)
        return button

    def __proceed_btn(self):
        button = Button(
            self.top, text="Back to main Menu", wraplength=80, padx=40, borderwidth=4, command=lambda: self.top.destroy())
        button.grid(row=11, column=1, padx=5, pady=20)
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

    def __delete_boxes(self):
        self.tax_exp_box.delete(0, "end")
        self.insurance_exp_box.delete(0, "end")
        self.utilities_exp_box.delete(0, "end")
        self.hoa_exp_box.delete(0, "end")
        self.lawn_exp_box.delete(0, "end")
        self.vacancy_exp_box.delete(0, "end")
        self.repair_exp_box.delete(0, "end")
        self.capex_exp_box.delete(0, "end")
        self.prop_man_exp_box.delete(0, "end")
        self.mortgage_exp_box.delete(0, "end")
        self.total_exp_box["state"] = NORMAL
        self.total_exp_box.delete(0, "end")

    def __populate_boxes(self):
        recordset = self.db.expense_query()
        record_list = [x for x in recordset[0]]
        self.tax_exp_box.insert(0, record_list[0])
        self.tax_exp_box.select_range(0, "end")
        self.insurance_exp_box.insert(0, record_list[1])
        self.utilities_exp_box.insert(0, record_list[2])
        self.hoa_exp_box.insert(0, record_list[3])
        self.lawn_exp_box.insert(0, record_list[4])
        self.vacancy_exp_box.insert(0, record_list[5])
        self.repair_exp_box.insert(0, record_list[6])
        self.capex_exp_box.insert(0, record_list[7])
        self.prop_man_exp_box.insert(0, record_list[8])
        self.mortgage_exp_box.insert(0, record_list[9])
        self.total_exp_box.insert(0, self.__get_total_expenses())
        self.total_exp_box["state"] = DISABLED

    ########################################################
    ########## Database Calls###############################
    ########################################################

    def __update_db(self):
        expense_dict = {
            0: int(self.tax_exp_box.get()),
            1: int(self.insurance_exp_box.get()),
            2: int(self.utilities_exp_box.get()),
            3: int(self.hoa_exp_box.get()),
            4: int(self.lawn_exp_box.get()),
            5: int(self.vacancy_exp_box.get()),
            6: int(self.repair_exp_box.get()),
            7: int(self.capex_exp_box.get()),
            8: int(self.prop_man_exp_box.get()),
            9: int(self.mortgage_exp_box.get()),
        }
        self.db.update_expenses(expense_dict)

    def __get_total_expenses(self):
        recordset = self.db.expense_query()
        result = sum([int(i) for i in recordset[0]])
        return result

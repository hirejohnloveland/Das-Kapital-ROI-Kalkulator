import os
import sqlite3


class DB_Connect():
    """Create an SQLite3 database object with query and insert methods"""

    def __init__(self):
        self.is_new_instance = self.__is_new_instance()
        self.connection = self.__get_connect()
        self.cursor = self.__get_cursor(self.connection)
        self.__write_tables()
        self.__write_zero_rows()

    ####################################################################
    ############Private methods to establish db connect/cursor##########
    ####################################################################

    # check if data exists
    def __is_new_instance(self):
        # Delete old SQLite3 Database if existant, this is for
        # a single record project, when extending for multi-property
        # this code needs to be modified
        if os.path.exists("my_property.db"):
            os.remove("my_property.db")  # delete when extending
            return True
        else:
            return True  # change to False when extening

    # Esatblish a connection to SQLite DB / create new instance
    def __get_connect(self):
        connection = sqlite3.connect("my_property.db")
        return connection

    # Establish a cursor for operations
    def __get_cursor(self, connection):
        cursor = connection.cursor()
        return cursor

    # Create the tables if new instance of this database
    def __write_tables(self):
        if self.is_new_instance:
            # Write database tables
            # table1 - Revenue
            self.cursor.execute("""CREATE TABLE income (
            rental_income integer,
            laundry_income integer,
            storage_income integer,
            misc_income integer)""")

            # table2 - Expenses
            self.cursor.execute("""CREATE TABLE expenses (
            tax_exp integer,
            insurance_exp integer,
            utility_exp integer,
            hoa_fees integer,
            lawn_exp integer,
            vacancy_exp integer,
            repair_exp integer,
            capex_exp integer,
            property_man integer,
            mortgage_exp integer 
            )   """)

            # table3 - Investment
            self.cursor.execute("""CREATE TABLE investment (
            down_payment integer,
            closing_costs integer,
            rehab_expense integer,
            misc_investment integer
            )   """)
    ####################################################################
    ############Public methods to add data to database##################
    ####################################################################
    # Will need to handle oid on extension

    def insert_income(self, income_fields: dict):
        """Inserts new record into the income table, takes a dictionary with the following values in
        in order, 
        0: rental income 
        1: laundry income
        2: storage income
        3: misc income"""
        self.cursor.execute("INSERT INTO income VALUES (:rental_inc, :laund_inc, :stor_inc, :misc_inc)",
                            {
                                'rental_inc': income_fields[0],
                                'laund_inc': income_fields[1],
                                'stor_inc': income_fields[2],
                                'misc_inc': income_fields[3]
                            })

    # oid is set to one automatically until extension
    def update_income(self, income_fields: dict):
        """Updates the current record (CURRENTLY OID=1 until extension) with input from the boxes
        0: rental income 
        1: laundry income
        2: storage income
        3: misc income"""
        self.cursor.execute("""UPDATE income SET
                    rental_income = :rental_inc,
                    laundry_income = :laund_inc,
                    storage_income = :stor_inc,
                    misc_income = :misc_inc

                    WHERE oid = 1""",
                            {
                                'rental_inc': income_fields[0],
                                'laund_inc': income_fields[1],
                                'stor_inc': income_fields[2],
                                'misc_inc': income_fields[3]
                            })

    def insert_expenses(self, expense_fields: dict):
        """Inserts new record into the expense table, takes a dictionary with the following values in
        in order, 
        0: tax expense
        1: insurance expense
        2: utility expense
        3: hoa expense
        4: lawn expense
        5: vacancy expense
        6: repair expense
        7: capital expense
        8: property management expense
        9: mortgage expense"""
        self.cursor.execute("INSERT INTO expenses VALUES (:tax,:ins,:util,:hoa,:lawn,:vac,:rep,:capex,:mgmt,:mort)",
                            {
                                "tax": expense_fields[0],
                                "ins": expense_fields[1],
                                "util": expense_fields[2],
                                "hoa": expense_fields[3],
                                "lawn": expense_fields[4],
                                "vac": expense_fields[5],
                                "rep": expense_fields[6],
                                "capex": expense_fields[7],
                                "mgmt": expense_fields[8],
                                "mort": expense_fields[9],
                            })

    # oid is set to one automatically until extension
    def update_expenses(self, expense_fields: dict):
        """Updates the current record (CURRENTLY OID=1 until extension) with input from the boxes
        0: tax expense
        1: insurance expense
        2: utility expense
        3: hoa expense
        4: lawn expense
        5: vacancy expense
        6: repair expense
        7: capital expense
        8: property management expense
        9: mortgage expense"""
        self.cursor.execute("""UPDATE expenses SET
                    tax_exp = :tax,
                    insurance_exp = :ins,
                    utility_exp = :util,
                    hoa_fees = :hoa,
                    lawn_exp = :lawn,
                    vacancy_exp = :vac,
                    repair_exp = :rep,
                    capex_exp = :capex,
                    property_man = :mgmt,
                    mortgage_exp = :mort 

                    WHERE oid = 1""",
                            {
                                "tax": expense_fields[0],
                                "ins": expense_fields[1],
                                "util": expense_fields[2],
                                "hoa": expense_fields[3],
                                "lawn": expense_fields[4],
                                "vac": expense_fields[5],
                                "rep": expense_fields[6],
                                "capex": expense_fields[7],
                                "mgmt": expense_fields[8],
                                "mort": expense_fields[9],
                            })

    def insert_investment(self, investment_fields: dict):
        """Inserts new record into the investment table, takes a dictionary with the following values in
        in order, 
        0: down payment
        1: closing cost
        2: rehabilitation expense
        3: misc expense"""
        self.cursor.execute("INSERT INTO investment VALUES (:dp,:close,:rehab,:misc)",
                            {
                                "dp": investment_fields[0],
                                "close": investment_fields[1],
                                "rehab": investment_fields[2],
                                "misc": investment_fields[3]
                            })

    # oid is set to one automatically until extension

    def update_investment(self, investment_fields: dict):
        """Updates the current record (CURRENTLY OID=1 until extension) with input from the boxes
        in order, 
        0: down payment
        1: closing cost
        2: rehabilitation expense
        3: misc expense"""
        self.cursor.execute("""UPDATE investment SET
                    down_payment = :dp,
                    closing_costs = :close,
                    rehab_expense = :rehab,
                    misc_investment = :misc

                    WHERE oid = 1""",
                            {
                                "dp": investment_fields[0],
                                "close": investment_fields[1],
                                "rehab": investment_fields[2],
                                "misc": investment_fields[3]
                            })

    ####################################################################
    ############Public methods to query the database####################
    ####################################################################
    # ALL query methods currently use fetchall, as this is a single record database
    # upon extension to multi-record, query will need to be extended to search by
    # primary key

    def income_query(self):
        """Returns a recordset of type list[tuples] representing all records in the income table"""
        self.cursor.execute("SELECT * FROM income")
        recordset = self.cursor.fetchall()
        return recordset

    def expense_query(self):
        """Returns a recordset of type list[tuples] representing all records in the expense table"""
        self.cursor.execute("SELECT * FROM expenses")
        recordset = self.cursor.fetchall()
        return recordset

    def investment_query(self):
        """Returns a recordset of type list[tuples] representing all records in the investment table"""
        self.cursor.execute("SELECT * FROM investment")
        recordset = self.cursor.fetchall()
        return recordset

    ###################################################################
    #### Pre-Extension methods to enable single record operation#######
    ###################################################################
    # inserts a zero row with an OID of 1 at the start of database, remove when extending
    def __write_zero_rows(self):
        income_zero_dict = {
            0: 0,
            1: 0,
            2: 0,
            3: 0
        }
        self.insert_income(income_zero_dict)

        expense_zero_dict = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
        self.insert_expenses(expense_zero_dict)

        invest_zero_dict = {
            0: 0,
            1: 0,
            2: 0,
            3: 0
        }
        self.insert_investment(invest_zero_dict)

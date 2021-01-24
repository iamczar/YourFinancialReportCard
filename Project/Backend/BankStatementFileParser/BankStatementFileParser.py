import csv
import pdb
from pathlib import Path
from dateutil import parser
import re
import datetime
from collections import namedtuple

"""

This module is to handle parsing bankstatements

"""

class BankStatementDataParserException(Exception):
    def __init__(self, exception_message):
        self.exception_message = exception_message

class BankStatementDataParser:
    
    def __init__(self):
        pass
        #print("Created a instance of BankStatementDataParser")

    def parse_bankstatement(self, csv_full_file_path):

        bank_statement_data = open(csv_full_file_path)
        bank_statement_csv_data = csv.reader(bank_statement_data)

        list_of_line_items = list(bank_statement_csv_data)

        list_of_invalid_transactions = []
        list_of_valid_transactions = []

        TransactionInfo = namedtuple('TransactionInfo',
                                     'Date Type Description Value Balance Account_Name Account_Number CategoryID')

        for each_line_item in list_of_line_items:

            if True == self.is_line_item_valid(each_line_item):

                tansaction_info_instance = TransactionInfo(*each_line_item)

                a_transaction_object = Transaction.from_tuple(
                    tansaction_info_instance)

                # This converts the date member into epoch value i.e. number of
                # seconds since jan 1 1970
                a_transaction_object.normalise_date()

                list_of_valid_transactions.append(a_transaction_object)
            else:
                list_of_invalid_transactions.append(each_line_item)

        bank_statement_data.close()

        return (list_of_valid_transactions, list_of_invalid_transactions)

    def is_line_item_valid(self, line_item):

        isAValidLineItem = True
        valid_number_of_line_item = 7
        if (len(line_item) < valid_number_of_line_item):
            #print(f"line item has less than {valid_number_of_line_item} it is " + str(len(line_item)))
            isAValidLineItem = False
        elif ([] == line_item):  # if line item is empty
            #print("BankStatementDataParser: line item is empty")
            isAValidLineItem = False
        elif ("Date" == line_item[0] or
              "Type" == line_item[1] or
              "Description" == line_item[2] or
              "Value" == line_item[3] or
              "Balance" == line_item[4] or
              "Account Name" == line_item[5] or
              "Account Number" == line_item[5]
              ):
            #print("BankStatementDataParser: its the header")
            isAValidLineItem = False

        return isAValidLineItem

class Transaction:
    
    def __init__(self, Date=None, Type=None, Description=None, Value=None,
                 Balance=None, Account_Name=None, Account_Number=None):
        self.Date = Date
        self.Type = Type
        self.Description = Description
        self.Value = Value
        self.Balance = Balance
        self.Account_Name = Account_Name
        self.Account_Number = Account_Number
        self.CategoryID = 0

    @classmethod
    def from_list(cls, transaction_as_list):

        if(len(transaction_as_list) < 7):
            raise BankStatementDataParserException(
                "Transaction: list does not contain enough elements")

        return cls(

            Date=transaction_as_list[0],
            Type=transaction_as_list[1],
            Description=transaction_as_list[2],
            Value=transaction_as_list[3],
            Balance=transaction_as_list[4],
            Account_Name=transaction_as_list[5],
            Account_Number=transaction_as_list[6],
        )

    @classmethod
    def from_tuple(cls, data):

        return cls(
            Date=data.Date,
            Type=data.Type,
            Description=data.Description,
            Value=data.Value,
            Balance=data.Balance,
            Account_Name=data.Account_Name,
            Account_Number=data.Account_Number
        )

    def convert_date_string_into_epoch(self, date):

        # regular expression for this pattern -> 02 Dec 2019
        firstDateFormat = r'\d{2}\s\D{3}\s\d{4}'

        # regular expression forthis pattern ->  02/12/2019
        secondDateFormat = r'\d{2}/\d{2}/\d{4}'

        if re.search(firstDateFormat, date) is not None:
            # this format -> 02 Dec 2019
            for each_date_element in date.splitlines():
                date = parser.parse(each_date_element)

            year = int(date.strftime("%Y"))
            month = int(date.strftime("%m"))
            date = int(date.strftime("%d"))

            epoch_equivalend = datetime.datetime(
                year, month, date, 0, 0).timestamp()

        elif re.search(secondDateFormat, date) is not None:
            # this format -> 02/12/2019

            for each_date_element in date.splitlines():
                date = parser.parse(each_date_element, dayfirst=True)

            year = int(date.strftime("%Y"))
            month = int(date.strftime("%m"))
            date = int(date.strftime("%d"))

            epoch_equivalend = datetime.datetime(
                year, month, date, 0, 0).timestamp()

        return epoch_equivalend

    def normalise_date(self):
        self.Date = self.convert_date_string_into_epoch(self.Date)

# class ManageCategoryId:

#     def __init__(self,TransactionDatabase,CategoryDatabase):
#         self.TransactionDatabase = TransactionDatabase
#         self.CategoryDatabase = CategoryDatabase

#     def assign_category_id_to_transaction(self):
#         pass

#         # for each 
#         # if re.search(transport_pattern,self.Description):
#         #     self.CategoryID = 1
#         # elif re.search()
    

#     def get_category_id_regex_dictionary(self,database_name):
#         pass
#         # # quiry the data base and store it on this dictionary

#         # category_regex_id_dictionary = {"Regex1":1,"Regex2":2}

#         # return category_regex_id_dictionary

import csv
import pdb
from pathlib import Path

"""

This module is to handle parsing bankstatements  

"""

class BankStatementDataParserException(Exception):
    def __init__(self,exception_message):
        self.exception_message = exception_message

class Transaction:
    
    def __init__(self,Date,Type,Description,Value,Balance,Account_Name,Account_Number):
        self.Date = Date 
        self.Type = Type 
        self.Description = Description
        self.Value = Value
        self.Balance = Balance
        self.Account_Name = Account_Name
        self.Account_Number = Account_Number
    
    @classmethod
    def from_list(cls,transaction_as_list):
        
        if(len(transaction_as_list) < 7):
            raise BankStatementDataParserException("Transaction: list does not contain enough elements")

        Date = transaction_as_list[0]
        Type = transaction_as_list[1] 
        Description = transaction_as_list[2]
        Value = transaction_as_list[3]
        Balance = transaction_as_list[4]
        Account_Name = transaction_as_list[5]
        Account_Number = transaction_as_list[6]

        transaction_object = cls(Date,Type,Description,Value,Balance,Account_Name,Account_Number)

        return transaction_object

    def normalise_date(self,date):
        # we have a scenario where the dates can be in a format of 
        # 02 Dec 2019
        # 02/12/2019
        normalised_date = date

        return normalised_date

class BankStatementDataParser:

    def __init__(self):
        print("Created a instance of BankStatementDataParser")

    def parse_bankstatement(self,csv_full_file_path):

        bank_statement_data = open(csv_full_file_path)
        bank_statement_csv_data = csv.reader(bank_statement_data)

        list_of_line_items = list(bank_statement_csv_data)

        list_of_invalid_transactions = []
        list_of_valid_transactions = []

        for each_line_item in list_of_line_items:
            if True == self.is_line_item_valid(each_line_item):
                a_transaction_object = Transaction.from_list(each_line_item)
                list_of_valid_transactions.append(a_transaction_object)

            else:
                list_of_invalid_transactions.append(each_line_item)

        bank_statement_data.close()

        return (list_of_valid_transactions,list_of_invalid_transactions)

    def is_line_item_valid(self,line_item):

        isAValidLineItem = True
        valid_number_of_line_item = 7
        if (len(line_item) < valid_number_of_line_item):
            print(f"line item has less than {valid_number_of_line_item} it is " + str(len(line_item)))
            isAValidLineItem = False
        elif ([] == line_item): # if line item is empty
            print("BankStatementDataParser: line item is empty")
            isAValidLineItem = False
        elif ("Date" == line_item[0] or 
            "Type" == line_item[1] or 
            "Description" == line_item[2] or
            "Value" == line_item[3] or 
            "Balance" == line_item[4] or
            "Account Name" == line_item[5] or 
            "Account Number" == line_item[5]
            ):
            print("BankStatementDataParser: its the header")
            isAValidLineItem = False

        return isAValidLineItem
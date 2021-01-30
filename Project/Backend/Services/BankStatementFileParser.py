import csv
from ..Models.Transaction import Transaction
from collections import namedtuple

"""
This module is to handle parsing bankstatements
"""


class BankStatementDataParser:

    def __init__(self):
        pass

    def parse_statement(self, csv_full_file_path):

        bank_statement_data = open(csv_full_file_path)
        bank_statement_csv_data = csv.reader(bank_statement_data)

        list_of_line_items = list(bank_statement_csv_data)

        list_of_invalid_transactions = []
        list_of_valid_transactions = []

        TransactionInfo = namedtuple('TransactionInfo',
                                     'Date Type Description Value Balance Account_Name Account_Number CategoryID')

        for each_line_item in list_of_line_items:

            if self.is_line_item_valid(each_line_item):

                transaction_info_instance = TransactionInfo(*each_line_item)

                a_transaction_object = Transaction.from_tuple(
                    transaction_info_instance)

                # This converts the date member into epoch value i.e. number of
                # seconds since jan 1 1970
                a_transaction_object.normalise_date()

                list_of_valid_transactions.append(a_transaction_object)
            else:
                list_of_invalid_transactions.append(each_line_item)

        bank_statement_data.close()

        return (list_of_valid_transactions, list_of_invalid_transactions)

    def is_line_item_valid(self, line_item):

        is_a_valid_line_item = True
        valid_number_of_line_item = 7
        if (len(line_item) < valid_number_of_line_item):
            # print(f"line item has less than {valid_number_of_line_item} it is " + str(len(line_item)))
            is_a_valid_line_item = False
        elif ([] == line_item):  # if line item is empty
            # print("BankStatementDataParser: line item is empty")
            is_a_valid_line_item = False
        elif ("Date" == line_item[0] or
              "Type" == line_item[1] or
              "Description" == line_item[2] or
              "Value" == line_item[3] or
              "Balance" == line_item[4] or
              "Account Name" == line_item[5] or
              "Account Number" == line_item[5]
        ):
            # print("BankStatementDataParser: its the header")
            is_a_valid_line_item = False

        return is_a_valid_line_item

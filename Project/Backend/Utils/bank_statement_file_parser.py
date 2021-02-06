import csv
from Project.Backend.Models.transaction import Transaction
from collections import namedtuple

class BankStatementDataParser:

    """
    this module is responsible for parsing a given bank statement
    """

    def __init__(self):
        pass

    def parse_statement(self, csv_full_file_path):
        """
        it returns valid and invalid transactions
        :param csv_full_file_path:
        :return: a tuple of list
        """

        bank_statement_data = open(csv_full_file_path)
        bank_statement_csv_data = csv.reader(bank_statement_data)

        list_of_line_items = list(bank_statement_csv_data)

        list_of_invalid_transactions = []
        list_of_valid_transactions = []

        TransactionInfo = namedtuple('TransactionInfo',
                                     'date type description value balance account_name account_number category_id')

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

        return list_of_valid_transactions, list_of_invalid_transactions

    def is_line_item_valid(self, line_item):

        is_a_valid_line_item = True
        valid_number_of_line_item = 7
        if len(line_item) < valid_number_of_line_item:
            is_a_valid_line_item = False
        elif not line_item:  # if line item is empty
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

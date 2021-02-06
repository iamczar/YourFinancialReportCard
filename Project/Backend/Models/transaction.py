import re
import datetime
from dateutil import parser
from Project.Backend.Models.transaction_exeptions import TransactionException


class Transaction:

    def __init__(self, date=None, type=None, description=None, value=None,
                 balance=None, account_name=None, account_number=None):
        self.date = date
        self.type = type
        self.description = description
        self.value = value
        self.balance = balance
        self.account_name = account_name
        self.account_number = account_number
        self.category_id = 0

    @classmethod
    def from_list(cls, transaction_as_list):

        if len(transaction_as_list) < 7:
            raise TransactionException("Transaction: list does not contain enough elements")

        return cls(

            date=transaction_as_list[0],
            type=transaction_as_list[1],
            description=transaction_as_list[2],
            value=transaction_as_list[3],
            balance=transaction_as_list[4],
            account_name=transaction_as_list[5],
            account_number=transaction_as_list[6],
        )

    @classmethod
    def from_tuple(cls, data):

        return cls(
            date=data.date,
            type=data.type,
            description=data.description,
            value=data.value,
            balance=data.balance,
            account_name=data.account_name,
            account_number=data.account_number
        )

    def convert_date_string_into_epoch(self, date):

        # regular expression for this pattern -> 02 Dec 2019
        first_date_format = r'\d{2}\s\D{3}\s\d{4}'

        # regular expression forthis pattern ->  02/12/2019
        second_date_format = r'\d{2}/\d{2}/\d{4}'

        if re.search(first_date_format, date) is not None:
            # this format -> 02 Dec 2019
            for each_date_element in date.splitlines():
                date = parser.parse(each_date_element)

            year = int(date.strftime("%Y"))
            month = int(date.strftime("%m"))
            date = int(date.strftime("%d"))

            epoch_equivalent = datetime.datetime(
                year, month, date, 0, 0).timestamp()

        elif re.search(second_date_format, date) is not None:
            # this format -> 02/12/2019

            for each_date_element in date.splitlines():
                date = parser.parse(each_date_element, dayfirst=True)

            year = int(date.strftime("%Y"))
            month = int(date.strftime("%m"))
            date = int(date.strftime("%d"))

            epoch_equivalent = datetime.datetime(
                year, month, date, 0, 0).timestamp()

        return epoch_equivalent

    def normalise_date(self):
        self.date = self.convert_date_string_into_epoch(self.date)

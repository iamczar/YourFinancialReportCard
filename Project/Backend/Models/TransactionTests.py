import unittest
from pathlib import Path
import datetime
from collections import namedtuple
from Transaction import Transaction


class TransactionTest(unittest.TestCase):

    # @unittest.skip("reason for skipping")
    def test_TransactionObjectTest(self):
        valid_transaction_as_a_list = [
            '01 Jan 2020',
            'Purchase',
            "'LADY GODIVA BARS LONDON SE15",
            '17.99',
            '',
            "'C B BALANGUE",
            "'552213******9444"]

        a_transaction_object_from_a_list = Transaction.from_list(
            valid_transaction_as_a_list)

        a_transaction_object = Transaction(
            '01 Jan 2020',
            'Purchase',
            "'LADY GODIVA BARS LONDON SE15",
            '17.99',
            '',
            "'C B BALANGUE",
            "'552213******9444")

        # check for the type - must be the same
        self.assertEqual(
            type(a_transaction_object),
            type(a_transaction_object_from_a_list))

        # check against each element
        self.assertEqual(
            a_transaction_object.Date,
            valid_transaction_as_a_list[0])
        self.assertEqual(
            a_transaction_object.Type,
            valid_transaction_as_a_list[1])
        self.assertEqual(
            a_transaction_object.Description,
            valid_transaction_as_a_list[2])
        self.assertEqual(
            a_transaction_object.Value,
            valid_transaction_as_a_list[3])
        self.assertEqual(
            a_transaction_object.Balance,
            valid_transaction_as_a_list[4])
        self.assertEqual(
            a_transaction_object.Account_Name,
            valid_transaction_as_a_list[5])
        self.assertEqual(
            a_transaction_object.Account_Number,
            valid_transaction_as_a_list[6])

        # check against each element from a other contructor
        self.assertEqual(
            a_transaction_object.Date,
            a_transaction_object_from_a_list.Date)
        self.assertEqual(
            a_transaction_object.Type,
            a_transaction_object_from_a_list.Type)
        self.assertEqual(
            a_transaction_object.Description,
            a_transaction_object_from_a_list.Description)
        self.assertEqual(
            a_transaction_object.Value,
            a_transaction_object_from_a_list.Value)
        self.assertEqual(
            a_transaction_object.Balance,
            a_transaction_object_from_a_list.Balance)
        self.assertEqual(
            a_transaction_object.Account_Name,
            a_transaction_object_from_a_list.Account_Name)
        self.assertEqual(
            a_transaction_object.Account_Number,
            a_transaction_object_from_a_list.Account_Number)

    def test_TransactionObjectConstructorIsTheSameType(self):
        '''
        This is using the namedtuple "overload"
        '''

        a_transaction_object = Transaction(
            '01 Jan 2020',
            'Purchase',
            "'LADY GODIVA BARS LONDON SE15",
            '17.99',
            '',
            "'C B BALANGUE",
            "'552213******9444")

        valid_transaction_as_a_list = [
            '01 Jan 2020',
            'Purchase',
            "'LADY GODIVA BARS LONDON SE15",
            '17.99',
            '',
            "'C B BALANGUE",
            "'552213******9444",
            ""]

        TransactionInfo = namedtuple('TransactionInfo',
                                     'Date Type Description Value Balance Account_Name Account_Number blank')

        tansaction_info_instance = TransactionInfo(
            *valid_transaction_as_a_list)

        a_transaction_object_from_a_namedtuple = Transaction.from_tuple(
            tansaction_info_instance)

        self.assertEqual(
            type(a_transaction_object),
            type(a_transaction_object_from_a_namedtuple))

        # check against each element from a other contructor
        self.assertEqual(
            a_transaction_object.Date,
            a_transaction_object_from_a_namedtuple.Date)
        self.assertEqual(
            a_transaction_object.Type,
            a_transaction_object_from_a_namedtuple.Type)
        self.assertEqual(
            a_transaction_object.Description,
            a_transaction_object_from_a_namedtuple.Description)
        self.assertEqual(
            a_transaction_object.Value,
            a_transaction_object_from_a_namedtuple.Value)
        self.assertEqual(
            a_transaction_object.Balance,
            a_transaction_object_from_a_namedtuple.Balance)
        self.assertEqual(
            a_transaction_object.Account_Name,
            a_transaction_object_from_a_namedtuple.Account_Name)
        self.assertEqual(
            a_transaction_object.Account_Number,
            a_transaction_object_from_a_namedtuple.Account_Number)

    # @unittest.skip("reason for skipping")
    def test_normalise_date_first_format(self):

        a_transaction_object = Transaction()

        first_date_format = '23 Dec 2020'

        actual_epoch_time = a_transaction_object.convert_date_string_into_epoch(
            first_date_format)

        year = 2020
        month = 12
        date = 23
        expected_epoch_time = datetime.datetime(
            year, month, date, 0, 0).timestamp()

        self.assertEqual(expected_epoch_time, actual_epoch_time)

    # @unittest.skip("reason for skipping")
    def test_normalise_date_second_format(self):

        a_transaction_object = Transaction()

        second_date_format = '02/12/2019'

        actual_epoch_time = a_transaction_object.convert_date_string_into_epoch(
            second_date_format)

        year = 2019
        month = 12
        date = 2
        expected_epoch_time = datetime.datetime(
            year, month, date, 0, 0).timestamp()

        self.assertEqual(expected_epoch_time, actual_epoch_time)


if __name__ == '__main__':
    unittest.main()

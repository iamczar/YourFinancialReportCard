import unittest
import datetime
from collections import namedtuple
from Project.Backend.Models.transaction import Transaction


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
            a_transaction_object.date,
            valid_transaction_as_a_list[0])
        self.assertEqual(
            a_transaction_object.type,
            valid_transaction_as_a_list[1])
        self.assertEqual(
            a_transaction_object.description,
            valid_transaction_as_a_list[2])
        self.assertEqual(
            a_transaction_object.value,
            valid_transaction_as_a_list[3])
        self.assertEqual(
            a_transaction_object.balance,
            valid_transaction_as_a_list[4])
        self.assertEqual(
            a_transaction_object.account_name,
            valid_transaction_as_a_list[5])
        self.assertEqual(
            a_transaction_object.account_number,
            valid_transaction_as_a_list[6])

        # check against each element from a other contructor
        self.assertEqual(
            a_transaction_object.date,
            a_transaction_object_from_a_list.date)
        self.assertEqual(
            a_transaction_object.type,
            a_transaction_object_from_a_list.type)
        self.assertEqual(
            a_transaction_object.description,
            a_transaction_object_from_a_list.description)
        self.assertEqual(
            a_transaction_object.value,
            a_transaction_object_from_a_list.value)
        self.assertEqual(
            a_transaction_object.balance,
            a_transaction_object_from_a_list.balance)
        self.assertEqual(
            a_transaction_object.account_name,
            a_transaction_object_from_a_list.account_name)
        self.assertEqual(
            a_transaction_object.account_number,
            a_transaction_object_from_a_list.account_number)

    def test_TransactionObjectConstructorIsTheSameType(self):
        """
        This is using the namedtuple "overload"
        """

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
                                     'date type description value balance account_name account_number blank')

        transaction_info_instance = TransactionInfo(
            *valid_transaction_as_a_list)

        a_transaction_object_from_a_namedtuple = Transaction.from_tuple(
            transaction_info_instance)

        self.assertEqual(
            type(a_transaction_object),
            type(a_transaction_object_from_a_namedtuple))

        # check against each element from a other constructor
        self.assertEqual(
            a_transaction_object.date,
            a_transaction_object_from_a_namedtuple.date)
        self.assertEqual(
            a_transaction_object.type,
            a_transaction_object_from_a_namedtuple.type)
        self.assertEqual(
            a_transaction_object.description,
            a_transaction_object_from_a_namedtuple.description)
        self.assertEqual(
            a_transaction_object.value,
            a_transaction_object_from_a_namedtuple.value)
        self.assertEqual(
            a_transaction_object.balance,
            a_transaction_object_from_a_namedtuple.balance)
        self.assertEqual(
            a_transaction_object.account_name,
            a_transaction_object_from_a_namedtuple.account_name)
        self.assertEqual(
            a_transaction_object.account_number,
            a_transaction_object_from_a_namedtuple.account_number)

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

import unittest
from .Services.BankStatementFileParser import BankStatementDataParser
from pathlib import Path
import datetime
from collections import namedtuple

class BankStatementParserTest(unittest.TestCase):
    
    # @unittest.skip("reason for skipping")
    def test_parse_bankstatement(self):
        test_file_csv = Path(__file__).parent / \
            "BankStatementFileParserTestFile.csv"
        bank_statement_parser = BankStatementDataParser()

        list_of_valid_and_invalid_transactions = bank_statement_parser.parse_bankstatement(
            test_file_csv)

        expected_number_valid_transactions = 92
        expected_number_invalid_transactions = 1

        actual_number_valid_transactions = len(
            list_of_valid_and_invalid_transactions[0])
        actual_number_invalid_transactions = len(
            list_of_valid_and_invalid_transactions[1])

        # expected number of valid transaction
        self.assertEqual(
            expected_number_valid_transactions,
            actual_number_valid_transactions)

        # expected number of invalid transaction
        self.assertEqual(
            expected_number_invalid_transactions,
            actual_number_invalid_transactions)

    # @unittest.skip("reason for skipping")
    def test_is_line_item_valid(self):

        valid_transaction_as_a_list = [
            '01 Jan 2020',
            'Purchase',
            "'LADY GODIVA BARS LONDON SE15",
            '17.99',
            '',
            "'C B BALANGUE",
            "'552213******9444"]

        bank_statement_parser = BankStatementDataParser()

        is_line_item_valid = bank_statement_parser.is_line_item_valid(
            valid_transaction_as_a_list)
        self.assertTrue(is_line_item_valid)

        invalid_transaction_as_a_list = [
            'Date',
            'Type',
            "Description",
            'Value',
            'Balance',
            "Account Name",
            "Account Number"]
        is_line_item_valid = bank_statement_parser.is_line_item_valid(
            invalid_transaction_as_a_list)
        self.assertFalse(is_line_item_valid)

        invalid_transaction_as_a_list = []
        is_line_item_valid = bank_statement_parser.is_line_item_valid(
            invalid_transaction_as_a_list)
        self.assertFalse(is_line_item_valid)


if __name__ == '__main__':
    unittest.main()

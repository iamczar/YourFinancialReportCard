import unittest
import sqlite3 as sql
import os

from Project.Backend.DataAccess.transaction_repository import TransactionRepository


class TransactionRepositoryTest(unittest.TestCase):

    # @unittest.skip("reason for skipping")
    def test_get_category_dictionary(self):

        dir_name = os.path.dirname(__file__)

        test_db_path = dir_name + "/" + "TestDataBase.db"

        result_dictionary = TransactionRepository.get_category_dictionary(test_db_path)

        expected_category_dictionary = {}
        with sql.connect(test_db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Category")

            rows = cur.fetchall()

            for row in rows:
                expected_category_dictionary[row[2]] = row[0]

        self.assertDictEqual(expected_category_dictionary, result_dictionary)

    # @unittest.skip("reason for skipping")
    def test_get_category_id(self):
        category_dictionary = {"fox": 1, "cat": 2, "test": 3}

        description = "test123test123"

        transaction_repo_object = TransactionRepository()

        result_transaction = transaction_repo_object.get_category_id(description, category_dictionary)

        self.assertEqual(3, result_transaction)

        description = "doesNotContainRegexMatch"

        result_transaction = transaction_repo_object.get_category_id(description, category_dictionary)

        self.assertEqual(999, result_transaction)

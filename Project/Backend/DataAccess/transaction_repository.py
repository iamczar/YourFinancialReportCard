import sqlite3 as sql
from Project.Backend.Utils.constants import *

import re

# this will contain the regex:id pair
category_id_dictionary = {"key": 1}


class TransactionRepository:
    def get_by_category_id(self, category_id, db_path):
        """
        access the transaction table db and filters the
        :param category_id:
        :param db_path:
        :return: list of transaction
        """

        list_of_transactions = []
        return list_of_transactions

    def add_transaction(self, transaction, db_path):

        transaction_id = self.get_category_id(transaction.description, category_id_dictionary)

        with sql.connect(db_path) as con:
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO Transaction (ID,Date,TransactionType,Description,Value,CategoryID)VALUES(?,?,?,?,?,?)",
                (transaction_id,
                 transaction.date,
                 transaction.type,
                 transaction.description,
                 transaction.value,
                 transaction_id))

            con.commit()
            msg = "Record successfully added"

        con.close()

        return msg

    def get_by_time_period(self, start_date, end_date, db_path):

        list_of_transactions = []
        return list_of_transactions

    def get_category_id(self, description, category_ID_dictionary):

        list_of_regex = category_ID_dictionary.keys()

        category_id = 999  # other id
        for each_regex in list_of_regex:
            if re.search(each_regex, description) is not None:
                category_id = category_ID_dictionary[each_regex]

        return category_id

    def get_category_dictionary(db_path):
        """
        It populates the category_dictionary
        :param db_path:
        :return: nothing
        """
        category_dictionary = {}
        with sql.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Category")

            rows = cur.fetchall()

            for row in rows:
                category_dictionary[row[2]] = row[0]

        return category_dictionary

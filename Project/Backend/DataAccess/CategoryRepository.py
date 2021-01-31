import sqlite3 as sql
from ..Utils.constants import *

class CategoryRepository:

    def __init__(self):
        pass

    def get_all(self):

        print(DB_PATH)

        # with sql.connect(DB_PATH) as con:
        #     cursor = con.cursor()

        #     cursor.execute(
        #         "INSERT INTO Transactions (ID,Date,TransactionType,Description,Value,CategoryID)VALUES(?,?,?,?,?,?)",
        #         (ID,
        #         Date,
        #         TransactionType,
        #         Description,
        #         Value,
        #         CategoryID))

        #     con.commit()
        #     msg = "Record successfully added"

        # con.close()
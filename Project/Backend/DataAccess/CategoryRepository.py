import sqlite3 as sql
import Constants

class CategoryRepository:
    def __init__(self):
        print("hello")

    def get_all(self):
        
        db_constants = Constants.Constants()

        with sql.connect(db_constants.DB_PATH) as con:
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO Transactions (ID,Date,TransactionType,Description,Value,CategoryID)VALUES(?,?,?,?,?,?)",
                (ID,
                Date,
                TransactionType,
                Description,
                Value,
                CategoryID))

            con.commit()
            msg = "Record successfully added"

        con.close()

a = CategoryRepository()

a.get_all()
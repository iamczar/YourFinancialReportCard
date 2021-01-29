import os
import shutil
import sqlite3 as sql

myCurrentWorkingDirectory = os.getcwd()
print(myCurrentWorkingDirectory)


ID = 11
Date = 123
TransactionType = "INT"
Description = "Transport"
Value = 22.0
CategoryID = 2

pathToDataBase = 'Transactions.db'

with sql.connect(pathToDataBase) as con:
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

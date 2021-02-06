import sqlite3 as sql

pathToDataBase = "Transactions"

with sql.connect(pathToDataBase) as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Category")

    rows = cur.fetchall()

    for row in rows:
        print(row[2])

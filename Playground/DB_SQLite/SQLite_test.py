import sqlite3 as sl

# Creates the test Database
con = sl.connect('my-test.db')

# Creates a Tables
with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)

# Inserts some records into the Database
sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)' # '?' is used as placeholders for future values
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]

with con:
    con.executemany(sql, data)


# Querying the Table
with con:
    data = con.execute("SELECT * FROM USER WHERE age <= 22")
    for row in data:
        print(row)
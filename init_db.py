import sqlite3


connection = sqlite3.connect('database.db')


with open('db.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO Com (name, comment) VALUES (?, ?)",
            ('LLLLooLLL', 'SHETO TAM')
            )


connection.commit()
connection.close()
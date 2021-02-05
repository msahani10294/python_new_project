import sqlite3

conn = sqlite3.connect("employees.db")

c = conn.cursor()

c.execute("""INSERT INTO  employee VALUES('manoj','kumar', 70000)""")
conn.commit()

c.execute("""INSERT INTO  employee VALUES('Rohit','kumar', 50000)""")
conn.commit()


conn.close()
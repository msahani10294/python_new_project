import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()

c.execute("""CREATE TABLE employee(

            first text,
            last text,
            pay int
            )""")

conn.commit()
conn.close()
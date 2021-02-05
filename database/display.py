import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()

# c.execute("SELECT * FROM employee WHERE last='kumar'")
c.execute("SELECT * FROM employee")

print(c.fetchall())

conn.commit()
conn.close()
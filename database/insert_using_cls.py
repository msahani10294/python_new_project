from emp import Employees
import sqlite3
conn = sqlite3.connect('employees.db')

emp1 = Employees('Rahul', 'Raj', 7000)
emp2 = Employees('Mohit', 'Das', 5000)
emp3 = Employees('MD', 'Asif', 10000)


c = conn.cursor()
c.execute("INSERT INTO employee VALUES ('{}', '{}', '{}')".format(emp1.first, emp1.last, emp1.pay))
conn.commit()

c.execute("INSERT INTO employee VALUES(?, ?, ?)",(emp2.first, emp2.last, emp2.pay))
conn.commit()

c.execute("INSERT INTO employee VALUES(:first, :last, :pay)",{'first':emp3.first, 'last':emp3.last, 'pay':emp3.pay})
conn.commit()

conn.close()
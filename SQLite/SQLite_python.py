import sqlite3 #no need for pip install.
from employee import Employee

conn = sqlite3.connect('employee.db') #it will create employee.db if it doenst exist , else would connect to employee.
cur = conn.cursor() # creates a cursor which helps us to access database and execute command

#creating table

cur.execute(""" CREATE TABLE EMPL(
    first text,
    last text,
    pay real
)""")

def insert_emp(emp):
    with conn: #using context manager no need to use commit
        cur.execute("insert into EMPL values(?,?,?)",(emp.first,emp.last,emp.pay))

def search_by_name(lastname):
    cur.execute('select * from EMPL where last = :last ',{'last':lastname})
    return cur.fetchall()

def update_pay(emp,pay):
    with conn:
        cur.execute(""" UPDATE EMPL SET PAY = ?
        WHERE first = ? and last = ?
        """,(emp.pay,emp.first,emp.last))

def delete_emp(emp):
    with conn:
        cur.execute("DELETE from EMPL where first = ? and last = ?",(emp.first,emp.last))

e1 = Employee('Harsh','Gupta',20000)
e2 = Employee('Karan','Sharma',15000)

delete_emp(e2)
cur.execute('select * from EMPL')
print(cur.fetchall())
#commit your command. for this connection is commited and not cursor. Cursor is just a pointer.
#conn.commit()

conn.close() #  good practice to close your connection 
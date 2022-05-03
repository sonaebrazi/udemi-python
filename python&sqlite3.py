import sqlite3
import sys
import csv

db_conn = sqlite3.connect('mydb.db')
print("Database Created")
the_cursor = db_conn.cursor()


def print_db():
    try:
        result = the_cursor.execute("SELECT ID ,f_name ,l_name ,age ,address ,salary ,hire_date FROM employees;")
        for row in result:
            print("id:", row[0])
            print("f_name:", row[1])
            print("l_name:", row[2])
            print("age:", row[3])
            print("address:", row[4])
            print("salary:", row[5])
            print("hire_date:", row[6])
    except sqlite3.OperationalError:
        print("The table doesn't exist")
    except:
        print("Couldn't retrieve data from database")


try:
    db_conn.execute("CREATE TABLE employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , f_name TEXT NOT NULL , l_name TEXT NOT NULL , "
        "age INT NOT NULL , address TEXT , salary REAL , hire_date TEXT);")
    db_conn.commit()
    print("Table Created")
except sqlite3.OperationalError as e:
    print("Table couldn't be created" , str(e))

db_conn.execute(
    "INSERT INTO employees(f_name , l_name , age , address , salary , hire_date) VALUES ('derek' , 'banas' , 43 , '123 Main St' , 50000 , date('now'));")
db_conn.commit()
print("Employee Entered")

print_db()

try:
    db_conn.execute("UPDATE employees SET address = '321 Main St' WHERE ID=1 ; ")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Database couldn't be updated")

print_db()

try:
    db_conn.execute("DELETE FROM employees WHERE ID=1; ")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Data couldn't be deleted")

print_db()
db_conn.rollback()
print_db()

try:
    db_conn.execute("ALTER TABLE employees ADD COLUMN 'image' BLOB DEFAULT NULL ;")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table couldn't be altered")

the_cursor.execute("PRAGMA TABLE_INFO(employees);")
row_names = [nameTuple[1] for nameTuple in the_cursor.fetchall()]
print(row_names)

the_cursor.execute('SELECT COUNT(*) FROM employees;')
num_of_rows = the_cursor.fetchall()
print("total rows: ", num_of_rows[0][0])

the_cursor.execute("SELECT SQLITE_VERSION();")
print("SQLITE VERSION :",the_cursor.fetchone())

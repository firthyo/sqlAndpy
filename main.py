import sqlite3
con = sqlite3.connect('/Users/firthmaneesuksri/PycharmProjects/pythonProject/chinook.db')
print('success')

cursor = con.execute("SELECT * FROM Customers WHERE CustomerID = 1")


for row in cursor:
    print("Customer", row[1], row[2])
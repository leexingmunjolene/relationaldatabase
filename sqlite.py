import sqlite3
conn = sqlite3.connect('database.db')

c = conn.cursor()

# Create table
c.execute("""CREATE TABLE Product
          (ProductID, Description, Price)""")

c.execute("""CREATE TABLE Orders
          (OrderID, CustomerID, OrderDate)""")

c.execute("""CREATE TABLE OrderLine
          (OrderID, ProductID, Quantity)""")

c.execute("""CREATE TABLE Customer
          (CustomerID, Name, Address, Telephone)""")

# Insert a row of data

c.execute("INSERT INTO Product VALUES ('P001', 'Shirt', 20.00)")
c.execute("INSERT INTO Product VALUES ('P002', 'Books', 15.99)")
c.execute("INSERT INTO Product VALUES ('P003', 'Toothbrush', 1.50)")
c.execute("INSERT INTO Product VALUES ('P004', 'Pouch' , 9.00)")
c.execute("INSERT INTO Product VALUES ('P005', 'Bag', 45.00)")

c.execute("INSERT INTO Customer VALUES ('C001', 'Mary', 'BLK 123, ABC STREET', '91235555')")
c.execute("INSERT INTO Customer VALUES ('C002', 'John', 'BLK 789, XYZ STREET', '98887777')")
c.execute("INSERT INTO Customer VALUES ('C003', 'Jane', 'BLK 555, AAA STREET', '82233445')")

c.execute("INSERT INTO Orders VALUES ('A001', 'C001', '16/01/2013')")
c.execute("INSERT INTO Orders VALUES ('A002', 'C002', '21/01/2013')")
c.execute("INSERT INTO Orders VALUES ('A003', 'C003', '30/01/2013')")

c.execute("INSERT INTO OrderLine VALUES ('A001', 'P005', 8)")
c.execute("INSERT INTO OrderLine VALUES ('A002', 'P003', 20)")
c.execute("INSERT INTO OrderLine VALUES ('A003', 'P002', 1)")
    
# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()

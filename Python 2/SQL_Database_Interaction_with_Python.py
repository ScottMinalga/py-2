#Joseph Picard
#CIT-117
#SQL Database Interaction with Python
import sqlite3
import csv

#Creating SQLite database
conn = sqlite3.connect("retirement_data.db")
cursor = conn.cursor()

def ImportData(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader][1:]

#Function to insert data into table
def Insert(list, table):
    for i in list:
        cursor.execute(f"INSERT INTO {table} VALUES('{i[0]}', '{i[1]}');")

def main():
    #Creating Tables -> DDL
    cursor.execute('CREATE TABLE IF NOT EXISTS Employee (EmployeeID INTEGER PRIMARY KEY, Name TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Pay (EmployeeID INTEGER, Year INTEGER, Earnings REAL, FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID))')
    cursor.execute('CREATE TABLE IF NOT EXISTS SocialSecurityMin (Year INTEGER PRIMARY KEY, Minimum REAL)')

    #Inserting data into table
    lstMain = ImportData('Employee.txt')
    Insert(lstMain, "Employee(EmployeeID, Name)")

    lstMain = ImportData('Pay.txt')
    for i in lstMain:
        cursor.execute(f"INSERT INTO Pay(EmployeeID, Year, Earnings) VALUES('{i[0]}', '{i[1]}', '{i[2]}');")

    lstMain = ImportData('SocialSecurityMinimum.txt')
    Insert(lstMain, "SocialSecurityMin(Year, Minimum)")

    conn.commit()

    cursor.execute("""
    SELECT a.EmployeeID, a.Name, b.Year, b.Earnings, c.Minimum
    FROM Employee AS a
    JOIN Pay AS b
    ON a.EmployeeID = b.EmployeeID
    JOIN SocialSecurityMin AS c
    ON c.Year = b.Year;
    """)

    #Fetching Data
    print(f"{'EmployeeID':<15} {'Name':<20} {'Year':<10} {'Earnings':<11} {'Minimum':<11} {'Include':<10}")

    for tupRow in cursor.fetchall():
        sInclude = "Yes" if float(tupRow[3]) >= float(tupRow[4]) else "No"
        print(f"{tupRow[0]:<15}{tupRow[1]:<20}{tupRow[2]:>6}{tupRow[3]:>15}{tupRow[4]:>11}{sInclude:>8}")

main()

import sqlite3
import csv
import time

def create_tables(conn):
    """ Create tables in the SQLite database """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            EmployeeID INT PRIMARY KEY,
            Name TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pay (
            EmployeeID INT,
            Year INT,
            Earnings REAL,
            FOREIGN KEY (EmployeeID) REFERENCES Employee (EmployeeID)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SocialSecurityMin (
            Year INT PRIMARY KEY,
            Minimum REAL
        );
    """)
    conn.commit()


def import_data(conn, file_path, table_name):
    """ Import data from a CSV file into the specified table, ignoring duplicates """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        rows = [tuple(row) for row in reader]
    cursor = conn.cursor()
    placeholders = ', '.join(['?'] * len(rows[0]))
    insert_query = f'INSERT OR IGNORE INTO {table_name} VALUES ({placeholders})'
    cursor.executemany(insert_query, rows)
    conn.commit()

def clear_table(conn, table_name):
    """ Clear all records from the specified table """
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table_name}')
    conn.commit()

def print_results(results):
    """ Print the results in a tabular format """
    print(f"{'Employee Name':<20} {'Year':<4} {'Earnings':>10} {'Minimum':>10} {'Include':>7}")
    for row in results:
        # Unpack the row for easier formatting
        employee_id, name, year, earnings, minimum, eligible = row
        print(f"{name:<20} {year:<4} {earnings:>10,.2f} {minimum:>10,.2f} {eligible:>7}")


def process_data(conn):
    """ Process and output the data as per requirements """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            e.EmployeeID, 
            e.Name, 
            p.Year, 
            p.Earnings, 
            s.Minimum,
            CASE 
                WHEN p.Earnings >= s.Minimum THEN 'Yes' 
                ELSE 'No' 
            END as RetirementEligible
        FROM 
            Employee e
        JOIN 
            Pay p ON e.EmployeeID = p.EmployeeID
        JOIN 
            SocialSecurityMin s ON p.Year = s.Year
    """)
    results = cursor.fetchall()

    # Print the results in a formatted table
    print_results(results)

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timeit
def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('salary_retirement.db')

    # Create tables
    create_tables(conn)

    # Clear data from tables before importing new data
    clear_table(conn, 'Employee')
    clear_table(conn, 'Pay')
    clear_table(conn, 'SocialSecurityMin')

    # Import data from text files
    import_data(conn, 'Employee.txt', 'Employee')
    import_data(conn, 'Pay.txt', 'Pay')
    import_data(conn, 'SocialSecurityMinimum.txt', 'SocialSecurityMin')

    # Process and output data
    process_data(conn)

    # Close the database connection
    conn.close()



main()

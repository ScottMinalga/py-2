#Author:  Prof. Candido
#Purpose: SQL Basics for the class to learn

import sqlite3

dbConnection = sqlite3.connect("InClassPracticed.db")
dbCursor =     dbConnection.cursor()

# Create Tables...
dbConnection.execute("CREATE TABLE IF NOT EXISTS DOGS(dog_name text, dog_owner_id integer, dog_age real)")
dbConnection.execute("CREATE TABLE IF NOT EXISTS Dog_owners(dog_owner_id integer, dog_owner_name text)")
# Insert Values....
sInsertStatement = "INSERT INTO Dog_owners(dog_owner_id, dog_owner_name) VALUES(1, 'Scott')"
dbConnection.execute(sInsertStatement)
sInsertStatement = "INSERT INTO Dog_owners(dog_owner_id, dog_owner_name) VALUES(2, 'Tiffany')"
dbConnection.execute(sInsertStatement)

dbConnection.commit()

# Show Output....



















'''
CREATE TABLE DOGS
(
dog_name char(30),
dong_owner_id long,
dog_age char(2)
)
'''
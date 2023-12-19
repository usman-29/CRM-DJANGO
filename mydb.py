import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='usman123',
)

# prepare cursor object
cursorObject = database.cursor()

# create database
cursorObject.execute('CREATE DATABASE company')
print('All Done!')

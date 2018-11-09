# Implement a python code for the database CRUD operations.

import mysql.connector
import sys
import getopt
import datetime

global db,cursor1
db=mysql.connector.connect(host="localhost", user="root",password="root")

""" check connection before any funtion"""

def check_connection():
	if db.is_connected():
		return True
	else:
		return False
"""create a database named details"""

def database():
	if check_connection():
			cursor1=db.cursor()
			cursor1.execute("CREATE DATABASE details")
			print(" DATABASE IS CREATED")
	else:
		print("ERROR IS CREATING A DATABASE")

"""function to create register table with id,first_name,last_name and date attributes"""

def table():
	db=mysql.connector.connect(host="localhost",user="root",password="root",database="details")
	if db.is_connected():
		cursor1=db.cursor()
		
		cursor1.execute("CREATE TABLE register(id INT(10) PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50),dob DATE)")
		print("Table created sucessfully\n")
	else:
		print("error in connection\n")
	

"""function for inserting values in register table"""

def insertion():
	db=mysql.connector.connect(host="localhost",user="root",password="root",database="details")
	if db.is_connected():
		cursor1= db.cursor()

		query = "INSERT INTO register(id, first_name, last_name,dob) VALUES (%s,%s,%s,%s) "
		id = input("Enter id\n")
		first_name = input("Enter first name\n")
		last_name = input("Enter last name\n")
		dob=input("Enter dob (yyyy/mm/dd)\n")
		data=(id,first_name,last_name,dob)
		cursor1.execute(query,data)
		db.commit()
		print("sucessfully inserted")

		if not validation(dob):
			print("Incorrect format.Enter in yyyy/mm/dd format")
			sys.exit()


	else:
		print(" connection failed")
	db.close()

def validation(date_input):
    try:
        datetime.datetime.strptime(date_input, '%Y-%m-%d')
        return True
    except ValueError:
        return False	



"""display the content of register table"""

def display():
	db=mysql.connector.connect(host="localhost",user="root",password="root",database="details")
	if db.is_connected():
		cursor1= db.cursor()

		query="SELECT * FROM register"

		cursor1.execute(query)
		result=cursor1.fetchall()
		for x in result:
			print(x)
		
	else:
		print("connection failed")
	db.close()

#to update the table details
def alter():
	db=mysql.connector.connect(host="localhost",user="root",password="root",database="details")
	if db.is_connected():
		cursor1= db.cursor()

		column=input("Enter column name \n")
		query = "ALTER TABLE register add %s VARCHAR(50)" %(column)
		cursor1.execute(query)
		db.commit
		print("added a new column")
	else:
			print("error in connection")
	db.close()





"""function used to truncate register table"""
def delete():
	db=mysql.connector.connect(host="localhost",user="root",password="root",database="details")
	if db.is_connected():
		cursor1= db.cursor()

		query = "DROP TABLE register"
		cursor1.execute(query)
		db.commit()
		print("sucessfully dropped the table")
		
	else:
		print("error in connection")
	db.close()


def main():
	while True:
		print("1----create database")
		print("2-----create table")
		print("3------insert values")
		print("4-------display")
		print("5-------update")
		print("6-------delete")
		print("Enter your choice:\n")

		ch= input("Enter the option :\t")
		if ch=='1':
			database()
		if ch=='2':
			table()
		if ch=='3':
			insertion()
		if ch=='4':
			display()
		if ch=='5':
			alter()
		if ch=='6':
			delete()
		if ch=='q':
			sys.exit()


if __name__ == "__main__":
	main()

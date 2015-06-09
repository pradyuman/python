from mysql.connector import MySQLConnection, Error
from mysql_config import read_db_config

def mysql_fetchone():
	'''Query a MySQL database using fetchone()'''
	try:
		db_config = read_db_config()

		#Creating a new MySQLConnection object
		conn = MySQLConnection(**db_config)
		
		#Creating a new MySQLCursor object from the MySQLConnection object
		cursor = conn.cursor()

		#Selects all rows from the space table
		cursor.execute("SELECT * from space")

		#selects the next row in the cursor result set
		row = cursor.fetchone()
		
		#prints the row out and gets the next row
		while row is not None:
			print(row)
			row = cursor.fetchone()

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	mysql_fetchone()

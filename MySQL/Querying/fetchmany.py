from mysql.connector import MySQLConnection, Error
from mysql_config import read_db_config

def gen_row(cursor, size=10):
	'''Gets a block of rows from the database specified by [size]'''
	while True:
		rows = cursor.fetchmany(size)

		if not rows:
			break
		
		for row in rows:
			yield row

def mysql_fetchmany():
	'''Query a MySQL database using fetchmany()'''
	try:
		db_config = read_db_config()

		#Creating a new MySQLConnection object
		conn = MySQLConnection(**db_config)
		
		#Creating a new MySQLCursor object from the MySQLConnection object
		cursor = conn.cursor()

		#Selects all rows from the space table
		cursor.execute("SELECT * from space")

		#prints the rows out
		for row in gen_row(cursor, 10):
			print(row)

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	mysql_fetchmany()

from mysql.connector import MySQLConnection, Error
from mysql_config import read_db_config

def mysql_fetchall():
	'''Query a MySQL database using fetchall()'''
	try:
		db_config = read_db_config()

		#Creating a new MySQLConnection object
		conn = MySQLConnection(**db_config)
		
		#Creating a new MySQLCursor object from the MySQLConnection object
		cursor = conn.cursor()

		#Selects all rows from the space table
		cursor.execute("SELECT * from space")

		#selects all the rows  in the cursor result set
		rows = cursor.fetchall()
		print('Number of rows: %d' % cursor.rowcount)
		
		#prints the rows out
		for row in rows:
			print(row)

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	mysql_fetchall()

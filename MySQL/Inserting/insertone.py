from mysql.connector import MySQLConnection, Error
from mysql_config import read_db_config

def insert_one(star_name, star_location):
	'''Insert one row into a MySQL database'''
	query = "INSERT INTO space(star_name, star_location)" \ 
			"VALUES(%s, %s)"
	args = (star_name, star_location)

	try:
		db_config = read_db_config()

		#Creating a new MySQLConnection object
		conn = MySQLConnection(**db_config)
		
		#Creating a new MySQLCursor object from the MySQLConnection object
		cursor = conn.cursor()

		#Inserts one row into the database
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('Insert ID: ', cursor.lastrowid)
		else:
			print('Insert Failure')

		conn.commit()

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	insert_one('Proxima Centauri', '14h 29m 42.9487s, -62 40 46.141')

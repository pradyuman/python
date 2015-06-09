from mysql.connector import MySQLConnection, Error
from mysql_config import read_db_config

def insert_many(star_name, star_location):
	'''Insert multiple rows into a MySQL database'''
	query = ("INSERT INTO space(star_name, star_location)" 
			 "VALUES(%s, %s)")
	args = (star_name, star_location)

	try:
		db_config = read_db_config()

		#Creating a new MySQLConnection object
		conn = MySQLConnection(**db_config)
		
		#Creating a new MySQLCursor object from the MySQLConnection object
		cursor = conn.cursor()

		#Inserts many rows into the database
		cursor.executemany(query, args)

		conn.commit()

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	stars = [('Proxima Centauri', '14h 29m 42.9487s, -62 40 46.141'),
			 ('Alpha Centauri', '14h 39m 36.4951s, -60 50 02.308'),
			 ('Beta Centauri', '14h 03m 49.4s, -60 22 23')]

	insert_many(stars)

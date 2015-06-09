from mysql.connector import MySQLConnection, Error
from mysql_config import read_db_config

def update_one(star_id, star_location):
	'''Insert one row into a MySQL database'''
	query = ("UPDATE space" 
			 "SET star_name = %s"
			 "WHERE id = %s")
	args = (star_name, star_id)

	try:
		db_config = read_db_config()

		#Creating a new MySQLConnection object
		conn = MySQLConnection(**db_config)
		
		#Creating a new MySQLCursor object from the MySQLConnection object
		cursor = conn.cursor()

		#Inserts one row into the database
		cursor.execute(query, args)

		conn.commit()

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	update_one(2, 'Alpha Centauri AB')

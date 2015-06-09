from mysql.connector import MySQLConnection, Error
from mysql_config import read_db_config

def delete_one(star_id):
	'''Delete one row of a MySQL database'''
	query = "DELETE FROM space WHERE id = %s"

	try:
		db_config = read_db_config()

		#Creating a new MySQLConnection object
		conn = MySQLConnection(**db_config)
		
		#Creating a new MySQLCursor object from the MySQLConnection object
		cursor = conn.cursor()

		#Deletes one row in the database
		cursor.execute(query, (star_id,))

		conn.commit()

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	delete_one(3)

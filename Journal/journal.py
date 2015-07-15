from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
	
	class Meta:
		database = db

def menu_loop():
	'''Show the menu'''

def add_entry():
	'''Add an entryto the database'''

def view_entries():
	'''View all entries currently in the database'''

def delete_entry(entry):
	'''Delete an entry in the database'''

if __name__=='__main__':
	menu_loop()


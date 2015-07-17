#!/usr/bin/env python3
from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
	content = TextField()
	timestamp = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = db

def initialize():
	'''Create database and content table if they don't exist.'''
	db.connect()
	db.create_tables([Entry], safe=True)

def menu_loop():
	'''Show the menu'''
	choice = None

	while choice != 'q':
		print("\nJOURNAL MENU | Enter 'q' to quit.")
		
		#print menu
		for key, value in menu.items():
			print('{}) {}'.format(key, value.__doc__))
		
		#get user input
		choice = input('Action: ').lower().strip()
		
		#run the function
		if choice in menu:
			menu[choice]()

def add_entry():
	'''Add an entry to the database'''
	print("Write your journal entry. Press ctrl+d when finished.")
	data = sys.stdin.read().strip()

	if data:
		if input('Save entry? [Y/n] ').lower() != 'n':
			Entry.create(content=data)
			print("Saved successfully!")

def view_entries():
	'''View all entries currently in the database'''

def delete_entry(entry):
	'''Delete an entry in the database'''

#OrderedDict of journal functions
menu = OrderedDict([
		('a', add_entry),
		('v', view_entries),
	   ])

if __name__=='__main__':
	initialize()
	menu_loop()


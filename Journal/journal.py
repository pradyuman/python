#!/usr/bin/env python3
from collections import OrderedDict
import datetime
from time import sleep
import os
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


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
	'''Show the menu'''
	choice = None

	while choice != 'q':
		clear()
		print("JOURNAL MENU")
		
		#print menu
		for key, value in menu.items():
			print('{}) {}'.format(key, value.__doc__))
		print("q) Quit application")
		
		#get user input
		choice = input("Action: ").lower().strip()
		
		#run the function
		if choice in menu:
			clear()
			menu[choice]()


def add_entry():
	'''Add an entry to the database'''
	print("Write your journal entry. Press ctrl+d when finished.")
	data = sys.stdin.read().strip()

	if data:
		if input("Save entry? [Y/n] ").lower() != 'n':
			Entry.create(content=data)
			print("Saved successfully!")
			sleep(1)


def view_entries(search_query=None):
	'''View all entries currently in the database'''
	entries = Entry.select().order_by(Entry.timestamp.desc())
	if search_query:
		entries =  entries.where(Entry.content.contains(search_query))

	for entry in entries:
		timestamp = entry.timestamp.strftime('%A %d %B %Y | %I:%M %p')
		clear()
		print(timestamp)
		print('='*len(timestamp))
		print(entry.content)
		print('\n\n'+'='*len(timestamp))
		print("n) Next Entry")
		print("d) Delete Entry")
		print("r) Return to main menu")

		next_action = input("Action [N/d/r]: ").lower().strip()

		if next_action == 'r':
			break
		elif next_action == 'd':
			delete_entry(entry)


def search_entries():
	'''Search through all your journal entries'''
	view_entries(input("Search query: "))

def delete_entry(entry):
	'''Delete an entry in the database'''
	if input("Are you sure? [y/N] ").lower() == 'y':
		entry.delete_instance()
		print("Entry deleted.")
		sleep(1)

#OrderedDict of journal functions
menu = OrderedDict([
		('a', add_entry),
		('v', view_entries),
		('s', search_entries)
	   ])

if __name__=='__main__':
	initialize()
	menu_loop()


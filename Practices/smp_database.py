#!/usr/local/python/bin/python
# coding=utf-8
# a simple database program

import shelve


def store_person(db):
	"""
	Query user for data and store it in the shelf object
	"""

	pid = input('Enter unique ID number: ')
	person = {'name': input('Enter Name: '), 'age': input('Enter Age: '), 'phone': input('Enter Phone: ')}
	db[pid] = person


def lookup_person(db):
	"""
	Query user for ID and desired field, and fetch the corresponding data from the shelf object
	"""
	pid = input('Enter ID Number: ')
	field = input('What would you like to know? (name, age, phone)')
	field = field.strip().lower()
	try:
		print(field.capitalize() + ':', db[pid][field])
	except KeyError:
		print("No The Person!")


def print_help():
	print("The available commands are:")
	print("store  : Store information aboute person")
	print("lookup : Looks up a person from ID number")
	print("quit   : Save changes and exit")
	print("?      : Prints this pages")


def enter_command():
	cmd = input('Enter command (? for help): ')
	cmd = cmd.strip().lower()
	return cmd


def main():
	database = shelve.open('E:\Codes\Python\confusion\Documents\database.dat')
	try:
		while True:
			cmd = enter_command()
			if cmd == 'store':
				store_person(database)
			elif cmd == 'lookup':
				lookup_person(database)
			elif cmd == '?':
				print_help()
			elif cmd == 'quit':
				return
	finally:
		database.close()


if __name__ == '__main__':
	main()


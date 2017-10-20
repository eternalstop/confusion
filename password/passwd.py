#!/usr/local/python/bin/python
# coding=utf-8
# a simple database program

import shelve


def store_passwd(db):
	"""
	Query user for data and store it in the shelf object
	"""

	pid = input('Enter Mark: ')
	pid = pid.lower()
	passwd_dic = {'sign': input('Enter sign: '),
	              'user': input('Enter user: '),
	              'passwd': input('Enter passwd: '),
	              'email': input('Enter email: '),
	              'phone': input('Enter phone: ')}
	db[pid] = passwd_dic


def lookup_passwd(db):
	"""
	Query user for ID and desired field, and fetch the corresponding data from the shelf object
	"""
	pid = input('Enter Mark or all for lookup all data: ')
	# field = input('What would you like to know? (sign, user, passwd, email, phone)')
	# field = input('What would you like to know? (mark for example qq/weibo/weixin)')
	# field = field.strip().lower()
	pid = pid.lower()
	if not db:
		print("Sorry,No Data!")
	try:
		if pid == 'all':
			for key in list(db.keys()):
				# print(key + ": ", db[key])
				print(key)
		else:
			print(pid.capitalize() + ':', db[pid])
	except KeyError:
		print("No The Mark!")


def delete_passwd(db):
	de_mark = input("what passwd do you want delete?(give a mark or all)")
	confirm = input("Are you sure delete it?(yes/no)")
	confirm = confirm.lower()
	if confirm == 'yes' or 'no':
		if confirm == 'yes':
			if de_mark in db:
				print("delete passwd about %s" % de_mark)
				db.pop(de_mark)
			elif de_mark == 'all':
				for key in list(db.keys()):
					print("Delete all data!!")
					db.pop(key)
			else:
				print("No data about %s" % de_mark + " in database")
		else:
			print("Nothing to do!")
	else:
		print("please input yes or no or all")


def print_help():
	print("The available commands are:")
	print("store  : Store passwd information aboute mark")
	print("lookup : Looks up a passwd from mark(give a mark or all)")
	print("delete : Delete a passwd from mark")
	print("quit   : Save changes and exit")
	print("?      : Prints this pages")


def enter_command():
	cmd = input('Enter command (? for help): ')
	cmd = cmd.strip().lower()
	return cmd


def main(file):
	database = shelve.open(file)
	try:
		while True:
			cmd = enter_command()
			if cmd == 'store':
				store_passwd(database)
			elif cmd == 'lookup':
				lookup_passwd(database)
			elif cmd == 'delete':
				delete_passwd(database)
			elif cmd == '?':
				print_help()
			elif cmd == 'quit':
				return
	finally:
		database.close()


if __name__ == '__main__':
	filename = 'passwd.dat'
	main(filename)

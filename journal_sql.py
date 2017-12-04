#!/usr/bin/env python3


"""
=====================================
|		Stores books I've read		|
=====================================
"""

import sqlite3
import re
import datetime
from functions import *
import os

conn = sqlite3.connect('journal_database.db')
c = conn.cursor()
#create table
c.execute("CREATE TABLE IF NOT EXISTS journal(title TEXT, author TEXT, date_started TEXT, date_ended TEXT)")

def add():
	
	#before adding, have to check if index is right.
	print('Welcome to your book journal! I hear you want to add something...\n')
	title = ( input(r'Add title: ') )

	author = ( input(r'Add author: ') )
	
	date_pattern=r'....-..-..'
	date = input(r'When did you start it? Give a date in the format of YYYY-MM-DD: ')
	while True:	
		try:
			if re.match(date_pattern,date):
				date = date.split('-')
				begin = (datetime.date(int(date[0]),int(date[1]),int(date[2])))
				print(begin)
				break
			else:
				print('Try again!! Remember, YYYY-MM-DD')
				date = input('Date started your book? ')
				continue
		except ValueError:
			print('Try again!! Remember, YYYY-MM-DD')
			date = input('Date started your book? ')
			continue
			
	date = input(r'When did you finish it? Give a date in the format of YYYY-MM-DD   OR   give a "-" if you are still reading it: ')
	while True:	
		try:
			if re.match(date_pattern,date):
				date = date.split('-')
				end = (datetime.date(int(date[0]),int(date[1]),int(date[2])))
				print(end)
				break
			elif (date=='-'):
				end = date
				print("Still Reading...")
				break
			else:
				print('Try again!! Remember, YYYY-MM-DD')
				date = input('Date finished your book? ')
				continue		
		except ValueError:
			print('Try again!! Remember, YYYY-MM-DD')
			date = input('Date finished your book? ')
			continue		
	c.execute("INSERT INTO journal (title,author,date_started,date_ended) VALUES(?,?,?,?)",(title,author,begin,end))
	conn.commit()
	

def show():
	clear()
	#get screen resolution
	h,w = get_res()
	#read database
	c.execute("SELECT * FROM journal")
	data = c.fetchall()
	
	_title = ['Title']
	_author = ['Author']
	_begin = ['Started Reading on']
	_end = ['Finished Reading on']
	_days_passed = ['Days Passed']
	
	for row in data:
		_title.append(row[0])
		_author.append(row[1])
		
		_begin.append(row[2])
		date_begin = row[2].split('-')
		date_begin = datetime.date(int(date_begin[0]),int(date_begin[1]),int(date_begin[2]))

		
		_end.append(row[3])
		if row[3]=='-':
			_days_passed.append('Still Reading...')
		else:
			date_end = row[3].split('-')
			date_end = datetime.date(int(date_end[0]),int(date_end[1]),int(date_end[2]))
			_days_passed.append(str(date_end - date_begin))	
	
	print('='*w)
	
	for i in range(len(_title)):
		if (i==0):
				entry = '#'
		else:
			entry = i
		
		string = (str(entry).ljust(2)+'| {0} | {1} | {2} | {3} | {4}').format(_title[i].ljust(get_maxstring(_title)),
																		   _author[i].ljust(get_maxstring(_author)),
																		   str(_begin[i]).ljust(get_maxstring(_begin)),
																		   str(_end[i]).ljust(get_maxstring(_end)),
																		   str(_days_passed[i]))
		endline = w-len(string)
		print(string+'|'.rjust(endline))
		if (i==0):
			print('-'*w)
		
def delete():
	entry = int(input("\nWhich entry you want to delete? #:"))
	c.execute("DELETE FROM journal LIMIT 1 OFFSET "+str(entry-1))
	conn.commit()
	#c.execute("UPDATE journal LIMIT *")
	
def backup_database():
	os.system('cp journal_database.db journal_database.db.bak')
	print('#### DATABASE WAS SUCCESSFULLY BACKED UP ####')

def restore_database():
	os.system('cp journal_database.db.bak journal_database.db')
	print('#### DATABASE WAS SUCCESSFULLY RESTORED ####')
	
def clear():
	os.system('clear')
	
	
	''' DAYS PASSED, den to exw valei akoma sto database
	if (_date=='-'):
		_days_passed.append('Still Reading...')
		print('I see you are still on it... Good for you!!')
	else:
		_days_passed.append( _end[index]-_begin[index] )
		print('So you finished it in '+str(_days_passed[index])+' days, huh? Good job!!')
	'''


clear()
while True:
	action = input(r'Choose action: ')
	if (action=='add'):
		add()
	elif (action=='show'):
		show()
	elif (action=='quit' or action=='exit'):
		c.close()
		conn.close()
		break
	elif (action=='delete'):
		delete()
	elif (action=='backup_database'):
		backup_database()
	elif (action=='restore_database'):
		restore_database()
	else:
		print('No such action. Try again...')
		


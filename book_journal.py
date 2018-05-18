#!/usr/bin/env python3

"""
=====================================
|	Stores books I've read      |
=====================================
"""

import os
import re
import datetime
import csv
import math
from functions import *

_title=[]
_author=[]
_begin=[]
_end=[]
_days_passed=[]
index=0

def initialize():
	_title[:]=[]
	_author[:]=[]
	_begin[:]=[]
	_end[:]=[]
	_days_passed[:]=[]
	index=0
	return index

h,w=get_res()
_s=20

##the result of these lists will be written in a file.
##RUN some code to define what "counter" to use to append to next line.

def clear():
	os.system('clear')

def read_file():
	progress('Reading database')
	clear()
	try:
		count=0
		with open('journal_data.txt') as csvfile:
			textfile = csv.reader(csvfile,delimiter='|')
			
			for i,line in enumerate(textfile):
				count+=1
				_title.append(line[0])
				_author.append(line[1])
				
				if (i==0):
					_begin.append(line[2])
				else:
					_date = line[2].split('-')
					_begin.append(datetime.date(int(_date[0]),int(_date[1]),int(_date[2])))
				
				if (line[3]=='-' or i==0):
					_end.append(line[3])
				else:
					_date = line[3].split('-')
					_end.append(datetime.date(int(_date[0]),int(_date[1]),int(_date[2])))
				
				_days_passed.append(str(line[4]))
				
	except FileNotFoundError:
		print('Error: There is nothing in the database\nTry adding a book first by typing "add" in "Choose action:"')
	return count
			
				
def print2file(i):
	#Needs to be called inside every 'add' action
	file=open('journal_data.txt','a')
	if (i==0):
		file.write('Title|Author|Started Reading on|Finished Reading on|Days Passed\n')
	file.write(_title[i]+'|'+_author[i]+'|'+str(_begin[i])+'|'+str(_end[i])+'|'+str(_days_passed[i])+'\n')		  

def clear_database():
	os.system('rm -i journal_data.txt')
	index=initialize()
	return index
	
			  
class IndexZero(Exception):
	pass

def show(index):
	try:
		index=initialize()
		index=read_file()
		clear()
	
		if (index==0):
			raise IndexZero
		
		print('='*w)
		for i in range(index):
				if (i==0):
					line_number='#'
				else:
					line_number=i
					
				string = (str(line_number).ljust(2)+'| {0} | {1} | {2} | {3} | {4}').format(_title[i].ljust(get_maxstring(_title)),
																			   _author[i].ljust(get_maxstring(_author)),
																			   str(_begin[i]).ljust(get_maxstring(_begin)),
																			   str(_end[i]).ljust(get_maxstring(_end)),
																			   str(_days_passed[i]))
				endline = w-len(string)
				print(string+'|'.rjust(endline))
				if (i==0):
		
		print('-'*w)
				
	except IndexZero:
		print('Error: There is nothing to show\nTry adding a book first by typing "add" in "Choose action:"')
	
	
def add():
	clear()
	
	#before adding, have to check if index is right.
	print('Welcome to your book journal! I hear you want to add something...\n')
	_title.append( input(r'Add title: ') )

	_author.append( input(r'Add author: ') )
	
	date_pattern=r'....-..-..'
	_date = input(r'When did you start it? Give a date in the format of YYYY-MM-DD: ')
	while True:	
		try:
			if re.match(date_pattern,_date):
				_date = _date.split('-')
				_begin.append(datetime.date(int(_date[0]),int(_date[1]),int(_date[2])))
				print(_begin[index])
				break
			else:
				print('Try again!! Remember, YYYY-MM-DD')
				_date = input('Date started your book? ')
				continue
		except ValueError:
			print('Try again!! Remember, YYYY-MM-DD')
			_date = input('Date started your book? ')
			continue
			
	_date = input(r'When did you finish it? Give a date in the format of YYYY-MM-DD   OR   give a "-" if you are still reading it: ')
	while True:	
		try:
			if re.match(date_pattern,_date):
				_date = _date.split('-')
				_end.append(datetime.date(int(_date[0]),int(_date[1]),int(_date[2])))
				print(_end[index])
				break
			elif (_date=='-'):
				_end.append(_date)
				print("Still Reading...")
				break
			else:
				print('Try again!! Remember, YYYY-MM-DD')
				_date = input('Date finished your book? ')
				continue		
		except ValueError:
			print('Try again!! Remember, YYYY-MM-DD')
			_date = input('Date finished your book? ')
			continue		
	
	if (_date=='-'):
		_days_passed.append('Still Reading...')
		print('I see you are still on it... Good for you!!')
	else:
		_days_passed.append( _end[index]-_begin[index] )
		print('So you finished it in '+str(_days_passed[index])+' days, huh? Good job!!')
	
	print2file(index)
	

def delete():
	show(index)
	edit_index = int(input("\nWhich entry you want to delete? #:"))
	
	
	del _title[edit_index]
	del _author[edit_index]
	del _begin[edit_index]
	del _end[edit_index]
	del _days_passed[edit_index]
	
	os.system('rm -i journal_data.txt')
	
	for i in range(index-1):
		print2file(i)
	
	show(index-1)
	print('\nEntry #'+str(edit_index)+' was deleted!\n')
	#Maybe add an undo option here.
	return index-1

def progress(string):
	import sys
	sys.stdout.write(string)
	sys.stdout.flush()
	for i in range(3):
		sys.stdout.write('.')
		sys.stdout.flush()
		os.system('sleep 1')
	sys.stdout.write('\n')

def backup_database():
	os.system('cp journal_data.txt journal_data.txt.bak')
	
	
def which_entry(): 
	print("You're currently in entry "+str(index))
	
clear()
index=read_file()
#print(_title[0])
#print(_author[0])

while True:
	action = input(r'Choose action: ')
	if (action=='add'):
		add()
		index+=1
	elif (action=='show'):
		show(index)
	elif (action=='which_entry'):
		which_entry()
	elif (action=='clear_database'):
		index=clear_database()
	elif (action=='quit' or action=='exit'):
		break
<<<<<<< HEAD
	elif (action=='delete'):
		index=delete()
	elif (action=='backup_database'):
		backup_database()
	else:
		print('No such action. Try again...')
		
		
=======
>>>>>>> 9bffd8e9769c432e98fd6713880029bf85e1f6a7

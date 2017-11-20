#!/usr/bin/env python3

"""
=====================================
|		Stores books I've read		|
=====================================
"""

import os
import re
import datetime
import csv

_title=[]
_author=[]
_begin=[]
_end=[]
_s=30
index=0
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
			
			for line in textfile:
				count+=1
				_title.append(line[0])
				_author.append(line[1])
				_date = line[2].split('-')
				_begin.append(datetime.date(int(_date[0]),int(_date[1]),int(_date[2])))
				if (line[3]=='-'):
					_end.append(line[3])
				else:
					_date = line[3].split('-')
					_end.append(datetime.date(int(_date[0]),int(_date[1]),int(_date[2])))
				
	except FileNotFoundError:
		print('Error: There is nothing in the database\nTry adding a book first by typing "add" in "Choose action:"')
	return count
			
				
def print2file(i):
	#Needs to be called inside every 'add' action
	file=open('journal_data.txt','a')
	file.write(_title[i]+'|'+_author[i]+'|'+str(_begin[i])+'|'+str(_end[i])+'\n')		  
			  
class IndexZero(Exception):
	pass

def show(index):
	try:
		clear()
		print('='*169)
		print( '{0}| {1} | {2} | {3} | {4} | {5} |'
					.format( '#'.ljust(2),
								'Title'.ljust(_s),
								'Author'.ljust(_s),
								'Started Reading on'.ljust(_s),
								'Finished Reading on'.ljust(_s),
								'Days Passed'.ljust(_s)
						   ))
		print('-'*169)
		
		if (index==0):
			raise IndexZero
			
		for i in range(index):
				if(_end[i]=='-'):
					_days_finished = 'Still Reading...'
				else:
					_days_finished = _end[i]-_begin[i]
				print( str(i+1).ljust(2)+'| {0} | {1} | {2} | {3} | {4} |'
					.format( _title[i].ljust(_s), _author[i].ljust(_s), str(_begin[i]).ljust(_s),
							 str(_end[i]).ljust(_s), str(_days_finished).ljust(_s)	))
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
		if re.match(date_pattern,_date):
			_date = _date.split('-')
			_begin.append(datetime.date(int(_date[0]),int(_date[1]),int(_date[2])))
			print(_begin[index])
			break
		else:
			print('Try again!! Remember, YYYY-MM-DD')
			_date = input('Date started your book? ')
			continue
			
	_date = input(r'When did you finish it? Give a date in the format of YYYY-MM-DD   OR   give a "-" if you are still reading it: ')
	while True:	
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
	
	if (_date=='-'):
		_days_finished='Still Reading...'
		print('I see you still on it... Good for you!!')
	else:
		_days_finished = _end[index]-_begin[index]
		print('So you finished it in '+str(_days_finished)+' days, huh? Good job!!')
	
	print2file(index)
	

def progress(string):
	import sys
	sys.stdout.write(string)
	sys.stdout.flush()
	for i in range(3):
		sys.stdout.write('.')
		sys.stdout.flush()
		os.system('sleep 1')
	sys.stdout.write('\n')
	
def which_entry(): 
	print("You're currently in entry "+str(index+1))
	
	
clear()
index=read_file()
while True:
	action = input(r'Choose action: ')
	if (action=='add'):
		add()
		index+=1
	elif (action=='show'):
		progress('Loading')
		show(index)
	elif (action=='which_entry'):
		which_entry()
	elif (action=='quit' or action=='exit'):
		break
	else:
		print('No such action. Try again...')
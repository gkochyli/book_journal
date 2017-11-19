#!/usr/bin/env python3

"""
=====================================
|	Stores books I've read      |
=====================================
"""

import os
import re
import datetime

_title=[]
_author=[]
_begin=[]
_end=[]
_s=30
index=0
##the result of these lists will be written in a file.
##RUN some code to define what "counter" to use to append to next line.

		
def init_write(index):
	with open('init.txt','w') as init:
		init.write('index='+str(index))
			
			
def init_load():
	pattern=r'index=([0-9]*)'
	while True:	
		try:
			with open('init.txt','r') as init:
				text = init.readlines()
				for line in text:
					match = re.match(pattern,line) 
					if match:
						index = match.group(1)	
			return int(index)
		except FileNotFoundError:
			print('Creating init.txt ...')
			os.system('echo "index=0" > init.txt')	
	
def print2file():
	
	#Print frame and titles
	file=open('book_journal.txt','a')
	if(index==0):
		file.write('='*169)
		file.write( '{0}| {1} | {2} | {3} | {4} | {5} |'
					.format( '#'.ljust(2),
								'Title'.ljust(_s),
								'Author'.ljust(_s),
								'Started Reading on'.ljust(_s),
								'Finished Reading in'.ljust(_s),
								'Days Passed'.ljust(_s)
						   ))
		file.write('\n')
	
	for i in range(len(_title)):
		if(_end[i]=='-'):
			_days_finished = 'Still Reading...'
		else:
			_days_finished = _end[i]-_begin[i]
			
		file.write( str(i+1).ljust(2)+'| {0} | {1} | {2} | {3} | {4} |'
				.format( _title[i].ljust(_s), _author[i].ljust(_s), str(_begin[i]).ljust(_s),
					   	 str(_end[i]).ljust(_s), str(_days_finished).ljust(_s)	))	
	file.close()
	init_write(index)
			  
			  
def show():
	#Print to file
	os.system('clear')
	try:
		file=open('book_journal.txt','r')
		print(file.read())
		file.close()
	except FileNotFoundError as err:
		print('Error: There is no book in the database\nTry adding a book by typing "add" in "Choose action:"')
		
	
	
def add():
	
	#before adding, have to check if index is right.
	index = init_load()
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
			
	_date = input(r'When did you finish it? Give a date in the format of YYYY-MM-DD   OR   give a "-" if you still reading it: ')
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
	
	

	
	
while True:
	index=init_load()
	action = input(r'Choose action: ')
	if (action=='add'):
		add()
		index+=1
	elif (action=='show'):
		progress('Loading')
		show()
	elif (action=='print2file'):
		progress('Saving')
		print2file()
	elif (action=='which_entry'):
		which_entry()
	elif (action=='quit' or action=='exit'):
		break

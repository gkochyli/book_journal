import curses

def get_res():
	#returns height and width of current terminal.
	obj = curses.initscr()
	try:
		h,w = obj.getmaxyx()
	finally:
		curses.nocbreak()
		curses.endwin()
	return h,w	

def get_maxstring(_list_const):
	#returns the maximum length of _lists' strings
	_list=_list_const
	max_len=0
	for string in _list:
		if type(string) is not str:
			string=str(string)
		if( len(string)>max_len ):
			max_len=len(string)
	return max_len
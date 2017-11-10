import io
import sys
import string
import os

def file_reader():
	open_carrot = 0;
	forward_slash = 0;
	close_carrot = 0;
	previous_char = '';
	look_for_close = 0;
	
	with open('test3.xml') as file:
		#file = open('test3.xml','r')
		while True:
			c = file.read(1);
			if not c:
				print("");
				print("END");
				break;
			else:
				if (c == '<'):
					open_carrot = 1;
					previous_char = '<';
					print(c,end="");
				elif (c == '/' and previous_char == '<'):
					look_for_close = 1;
					previous_char = '/';
					print(c,end="");
				elif (c == '>' and look_for_close == 1):
					print(c, end="");
					print("");
					look_for_close = 0;
				else:
					print(c,end="");



if __name__ == "__main__":

	file_reader()

import string
import sys
import secrets

specials_set = ['!', '@', '#', '$', '%', '^', '&' , '*' , 
'(' , ')' , '~' , '`' ,  '_'  , '-' ,  '='  , '[' ,  ']' , '{' ,  '}'  ,  '|' ,  ';' ,  ':' , '"'   , '<'  ,  '>',  '?' , ',' , '.' , '/']
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

all_together = []
all_together = all_together + specials_set + lowercase + uppercase


key = []

def key_generator(length=63):
	if(length < 8):
		print("Number is too short to create a WPA/2 key.")
		exit(1)
	for k in range(length):
		key.append( all_together[secrets.randbelow(len(all_together))] )
	k = ''.join(key)
	return k


if __name__ == "__main__":
	k = []
	if(len(sys.argv) == 1):
		k = key_generator()
	else:
		k = key_generator( int(sys.argv[1]) )
	print(k)
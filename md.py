import hashlib, sys, time
from termcolor import colored as color
from pyfiglet import figlet_format as figlet
if len(sys.argv)==2:
		if sys.argv[1]=='gen':
			print (color(figlet('md5'), 'red'))
			str = input(color('Enter string: ', 'blue'))
			result = hashlib.md5(str.encode()) 
			result = result.hexdigest()
			print (color('Hash is : ' + result, 'cyan'))
		elif sys.argv[1]=='crack':
			print (color(figlet('md5'), 'red'))
			print (color('cracking mode...', 'green'))
			hash = input('Enter hash: ')
			wordlist = input(color('Enter wordlist [defult : words.txt] : ', 'green'))
			try:
				words = open(wordlist, 'r')
			except:
				print (color('[-] Wordlist not found', 'red'))
				exit()
			start = time.time()
			for word in words.readlines():
				word = word.strip()
				h = hashlib.md5(word.encode())
				c_hash = h.hexdigest()

				if hash==c_hash:
					print (color('[!] Hash found :  ' + word, 'green'))
					print (color('[+] Hash found in ' + str(time.time()-start), 'red'))
					exit()
				else:
					print (color('[-] Cracking ' + word + ' : ' + hash, 'red'))
			print (color('[!] wordlist empty', 'yellow'))
		else:
			print (color(figlet('md5'), 'red'))
			print (color('\t\tby LuciferPy\n\tUsage~:#\n\t\tusage\t-\tto show this usage\n\t\tgen\t-\tGenerate a hash\n\t\tcrack\t-\tCracking Hash', 'yellow'))
			print (color('Example : \npython md.py gen\npython md.py crack\n', 'red'))
else:
	print (color(figlet('md5'), 'red'))
	print (color('\t\tby LuciferPy\n\tUsage~:#\n\t\tusage\t-\tto show this usage\n\t\tgen\t-\tGenerate a hash\n\t\tcrack\t-\tCracking Hash', 'yellow'))



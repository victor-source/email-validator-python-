
import re
while True:
	try:
		user_input=input('enter a to (a)dd, v to (v)iew emails')
		v={}
		if user_input == 'a':
		
			x={
			1:'',
			2:'',
			3:''
			}
			#collecting statement with email
			str= input('enter first address\n')
			str2=input('enter second address\n')
			str3=input('enter third address\n')
				#implementing the pattern in Regex
			pattern = r"([\w\.-]+)@([\w\-]+)(\.[\w\.]+)"
			#matching pattern
			match1 = re.search(pattern, str)
			match2 = re.search(pattern, str2)
			match3 = re.search(pattern, str3)
			x[1]=(match1.group())
			x[2]=(match2.group())
			x[3]=(match3.group())
			v=(r'1. {(x[1])}  2. {(x[2])}  3. {(x[3])}')
			print('here is a list of your addresses: \n' )
			print(x)
			file = open("emails.txt", "w")
			file.write(v)
			file.close()
			
			file = open("emails.txt", "r")
			print(file.read())
			file.close()
			
		elif user_input == 'v':
			print(v)
			break
		else:
			print('pls enter a valid option')
	except:
		break
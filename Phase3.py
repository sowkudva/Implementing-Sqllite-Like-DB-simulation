import re,os


#from first import useDirectory
# from first import selectTable
# from f4 import updateTable
#global settings
#update 1 working copy
mypath=" "
db_used=" "


#****************************************************************************************
#METHIOD: createDBmethod()
#This method is called when User issues create DB command

#****************************************************************************************
def createDBmethod():
	try:
		os.mkdir(dirName)
		print("Database "+dirName+" created.")
	except FileExistsError:   		# if the directory is already present at the location
		print("!Failed to create database "+dirName+" because it already exists.")




#****************************************************************************************
#METHIOD: createTable()
#This method is called when User issues create table command

#****************************************************************************************
def createTable():
	try:
		if os.path.isdir(db_used):
			try:
				filepath= db_used+"/"+fileName02+".txt" #creates a filepath
				
				if os.path.isfile(filepath):	 			   # checks if the file exists
					print("!Failed to create table " +fileName02 + " because it already exists.")
				else :
					newfile= open(filepath, "w")  				#create a new file
					newfile.write(s2[1:-1].replace(",","|"))	# add the data provided by user as seperated by |
					newfile.close()
					print("Table "+fileName02 +" created.")
			except FileNotFoundError:
				print("!Failed to create table " +fileName02 + " because it already exists.")
			
			
		else :
			db_used == " "										#checks if the directory is selected or not
			print("DB is not selected")
	except:
		print("DB is not selected")
			
			
#****************************************************************************************
#METHIOD: useDirectory(urdir,urpath)
#This method is called when User issues use DB command

#****************************************************************************************
def useDirectory(urdir):
	try:
		if os.path.isdir(urdir):
			global db_used
			db_used =urdir  						# sets the global variable with the Directory selected
			#mypath =urpath+urdir
			
			#print(os.getcwd())
			print("Using database " +db_used +".")
		else:
			print("!Failed to use database "+urdir+" because it does not exist.")
	except : 
		print("Exception:!Failed to use database "+urdir+" because it does not exist.")
		
		
#****************************************************************************************
#METHIOD: selectTable()
#This method is called when User issues select * from Table  command
#this method is modified to handle inner join
#****************************************************************************************
def selectTable():	
	#try:
		if os.path.isdir(db_used):
			try:
				fp1= db_used+"/"+file1+".txt"
				fp2= db_used+"/"+file2+".txt"
				
				if not os.path.isfile(fp1):		#check if file not exists is true
					print("!Failed to query table "+ file1 +" because it does not exist.")
				elif not os.path.isfile(fp2):
					print("!Failed to query table "+ file2 +" because it does not exist.")
				else:
					with open(fp1,'rt') as f1:
						for line1 in f1:
							with open(fp2,'rt') as f2:
								for line2 in f2:
									content=line1.strip('\n')+"|"+line2.strip('\n')
									print(content)
									break
								break #this loop prints the headers from both the table files
					#this loop prints the elements from table file 1 and 2 only if the indexes match
					with open(fp1,'rt') as f1:
						for line1 in f1:
							l1=line1.split('|')[0].strip('\n')
							with open(fp2,'rt') as f2:
								for line2 in f2:
									l2=line2.split('|')[0].strip('\n')
									if (l1==l2):
										content=line1.strip('\n')+'|'+line2.strip('\n')
										print(content.strip('\n'))
									else:
										pass
										
					
			except FileNotFoundError:
				print("!Failed to query table "+ fileName04 +" because it does not exist.")
			
			
		else :
			db_used == " "
			print("DB is not selected")
	#except:
		#print("e :DB is not selected")
		
		
		
#****************************************************************************************
#METHIOD: LeftJoin()
#This method is called when User issues select * from Table  command

#****************************************************************************************
def LeftJoin():	
	#try:
		if os.path.isdir(db_used):
			try:
				fp1= db_used+"/"+file1+".txt"
				fp2= db_used+"/"+file2+".txt"
				
				if not os.path.isfile(fp1):		#check if table 1 file not exists is true
					print("!Failed to query table "+ file1 +" because it does not exist.")
				elif not os.path.isfile(fp2):   #check if table 2 file not exists is true
					print("!Failed to query table "+ file2 +" because it does not exist.")
				else:
					with open(fp1,'rt') as f1:
						for line1 in f1:
							with open(fp2,'rt') as f2:
								for line2 in f2:
									content=line1.strip('\n')+"|"+line2.strip('\n')
									print(content)
									break
								break  #this loop reads first line of file1 and reads first line file 2 and prints them and then breaks
					##this loop reads first index of all lines of file1 and reads first index of all lines of file 2 and prints them if they are equal		
					with open(fp1,'rt') as f1:
						for line1 in f1:
							l1=line1.split('|')[0].strip('\n')
							with open(fp2,'rt') as f2:
								for line2 in f2:
									l2=line2.split('|')[0].strip('\n')
									if (l1==l2):
										content=line1.strip('\n')+'|'+line2.strip('\n')
										print(content.strip('\n'))
						if (l1 != l2):
							content=line1.strip('\n')+'|'+'|'
							print(content.strip('\n'))
							#if indexes are not equal, prints only the line from the left table.		
									
										
					
			except FileNotFoundError:
				print("!Failed to query table "+ fileName04 +" because it does not exist.")
			
			
		else :
			db_used == " "
			print("DB is not selected")
	#except:
		#print("e :DB is not selected")


#****************************************************************************************
#METHIOD: insertInto()()
#This method is called when User issues Inser into  Table  command

#****************************************************************************************			

def insertInto():
	try:
		if os.path.isdir(db_used):
			try:
				filepath= db_used+"/"+filename+".txt"
				if not os.path.isfile(filepath):		#check if file not exists is true
					print("!Failed to insert into table "+ filename +" because it does not exist.")
				else :
					
					values= user_says.strip("insert into").strip(filename).strip(";")
					removeSpace=re.sub(r'(^[\t]+|[ \t]+)', '',values,flags=re.M)	
					onlyValues=removeSpace.lstrip('values').lstrip('(').replace("'",'').replace(",",'|').replace(")",'')
					newfile= open(filepath, "a")		#opens file in read mode
					newfile.write( '\n'+onlyValues)
					newfile.close()
					print("1 new record inserted.")
			
			except FileNotFoundError:
				print("!Failed to insert into table "+ filename +" because it does not exist.")
		else :
			db_used == " "
			print("DB is not selected")
			
	except:
		print("DB is not selected")
		


		



#**************************************************************************************************************

while True:
	try :
		user_says = input().strip() 
		#userInput = input().splitlines()
		#print(user_says)     			#accepts user inputs
		if user_says.lower() == ".exit":			
			print("All done.")
			break
			
		elif "CREATE DATABASE" in user_says.upper(): #input contains createDatabase, calls createdatabase method()
			input_1 = user_says[:-1]
			list1 = input_1.upper().split(" ")
			dirName = list1[2]
			createDBmethod();
					
		elif "USE" in user_says.upper():			#user input contains USE keyword calls method UseDirectory
			input01 = user_says[:-1]
			list01 = input01.upper().split(" ")
			dirName01 = list01[1]
			useDirectory(dirName01)
			
		elif "CREATE TABLE" in user_says.upper():	#user input contains CREATE calls createTable() method
			input02 = user_says[:-1]
			list02 = input02.upper().split(" ")
			f=list02[2].lower()
			sep='('
			fileName02=f.split(sep,1)[0].capitalize()
			s2 = input02.split(None, 2)[2].strip(fileName02)
			#print(s2);								#chops off the first 3 words and considers only the column names and datatypes
			createTable()
		elif "INSERT INTO" in user_says.upper():
			templist=user_says[:-1].split(" ")
			filename=templist[2]
			insertInto()
			
		
		elif "SELECT *" in user_says.upper() and "INNER JOIN" not in user_says.upper() and "LEFT OUTER JOIN" not in user_says.upper():			#user input contains Select , calls select Table method
			input04 = user_says[:-1]
			list04 = input04.upper().split(" ")
			file1=list04[3].capitalize()
			file2 = list04[5].capitalize()
			selectTable()
			
		elif "INNER JOIN" in user_says.upper():			#user input contains Inner Join , calls InnerJoin() method
			input05 = user_says[:-1]
			list05 = input05.upper().split(" ")
			file1=list05[3].capitalize()
			file2 = list05[7].capitalize()
			selectTable()
		
		elif "LEFT OUTER JOIN" in user_says.upper():			#user input contains Left Outer Join , calls LEFT OUTER JOIN method
			input05 = user_says[:-1]
			list05 = input05.upper().split(" ")
			file1=list05[3].capitalize()
			file2 = list05[8].capitalize()
			LeftJoin()
			
		else:
			pass
	except EOFError:
		
		break
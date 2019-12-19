#***************************************************************************************
# CS 657 			:Programming assignment 4
# Author			:Sowmya Kudva
# Date 				:14/05/2019
# Functionalities 	:Transactions
# Language			:Python
#***************************************************************************************
import re,os

mypath=" "
db_used=" "
success=0;

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
					newfile.write(value)	# add the data provided by user as seperated by |
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

#****************************************************************************************
def selectTable(check):	   														#modified select method
	try:
		if os.path.isdir(db_used):
			try:
				filepath= db_used+"/"+fileName04+".txt"
				
				if not os.path.isfile(filepath):								#check if file not exists is true
					print("!Failed to query table "+ fileName04 +" because it does not exist.")
				else :
					if check == " ":   											#if no condition is on select  specified this loop is executed
						newfile= open(filepath, "r")
						contents =newfile.read()
						print(contents.strip("\n"))
						newfile.close()
					else :
						with open(filepath, "rt") as fin:						#if conditions are specifies in select then this loop is executed
							for line in fin:
								if not check in line:      						#checks if the condition does not matche with every line in file
									print((line[1:].lstrip("|")).strip("\n")) 	#then prints the contents on User interface
						#fin.close()		
					
			except FileNotFoundError:
				print("!Failed to query table "+ fileName04 +" because it does not exist.")
			
			
		else :
			db_used == " "
			print("DB is not selected")
	except:
		print("e :DB is not selected")

#****************************************************************************************
#METHIOD: insertInto()()
#This method is called when User issues Inser into  Table  command

#****************************************************************************************			

def insertInto():
	try:
		if os.path.isdir(db_used):
			try:
				filepath= db_used+"/"+filename+".txt"
				if not os.path.isfile(filepath):							#check if file not exists is true
					print("!Failed to insert into table "+ filename +" because it does not exist.")
				else :
					
					values= user_says.strip("insert into").strip(filename).strip(";")
					removeSpace=re.sub(r'(^[\t]+|[ \t]+)', '',values,flags=re.M)	
					onlyValues=removeSpace.lstrip('values').lstrip('(').replace("'",'').replace(",",'|').replace(")",'')
					newfile= open(filepath, "a")							#opens file in read mode
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
		

#****************************************************************************************
#METHIOD: updateTable()
#This method is called when User issues update   Table  command
#Modification to handle transaction
#****************************************************************************************
def updateTable():
	
		if os.path.isdir(db_used):
			#try:
				filepath= db_used+"/"+filename05+".txt"
				out= db_used+"/"+"out.txt"
				transaction= db_used+"/"+"transaction.txt" # a new file transaction path
				if not os.path.isfile(filepath):		#check if file not exists is true
					print("!Failed to insert into table "+ filename05 +" because it does not exist.")
				else :
					col1=List[3]						#stores the values provided by user in variables
					
					col2=List[7]
					
					value1=List[5]
					
					value2=List[9]
					global success
					#checks if the file created by begin transaction has any content, if yes it is used by other process
					if not (os.path.getsize(transaction)==0):
						success=0
						print("Error: Table Flights is locked!")
									
					else: #if size is zero then allows user to update the table
						
						if value2 not in open(filepath).read():
							print("No records found")
							
						else:
							with open(filepath, "rt") as fin:
								with open(out, "wt") as fout:
									for line in fin:
										line=line.split("|")
										if value2 == line[0]:     				#checks if the keyed in value is present in line read from file
											line[1]=value1+'\n'					#keeps the value provided by user to the 2nd index of line read
												#temp = (value2+ "| "+value1).strip("'")
											line1='|'.join(line)
											
											fout.write(line1)					#writes line to the new temp file
										
										else:
											line1='|'.join(line)
											fout.write(line1)	
									#os.remove(filepath)
									#os.rename(out,filepath)	
									success =1;
									with open(transaction, "wt") as fin: #After updating the table file, updates the transaction file as In progress
										fin.write("In progress")			
									print("1 records modified.")
					
					
					
		else :
			db_used == " "
			print("DB is not selected")		


#****************************************************************************************
#METHIOD: commit()
#This method is called when User issues commit command
#This method is to commit transaction
#****************************************************************************************

def commit():
	if (success ==0):	#check the global parameter value
		print("Transaction abort")
	else:
		filepath= db_used+"/"+filename05+".txt"	#persists the changes to the original file which was earlier in temp file
		out= db_used+"/"+"out.txt"
		transaction= db_used+"/"+"transaction.txt"
		os.remove(filepath)
		os.rename(out,filepath)
		os.remove(transaction)
		print("Transaction committed")		

	
#****************************************************************************************
#METHIOD: begin()
#This method is called when User issues Begin Transaction command
#This method is to handle transaction
#****************************************************************************************	

def begin():
	if os.path.isdir(db_used):
		transaction= db_used+"/"+"transaction.txt"
		if not os.path.isfile(transaction):	#creates a file named transaction and inputs nothing so that the size is zero
			with open(transaction, "wt") as fin:
				fin.write("")
		print("Transaction starts")		
	
			
#********************************************************end of methods*********************************************************************

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
			s2 = input02.split(None, 3)[2]
			s3=	s2.split("(")
			fileName02=s3[0] 
			
			values=user_says.split("(")
			value=values[1].strip(";").strip(")").replace("'",'').replace(",",'|') #chops off the first 3 words and considers only the column names and datatypes
			createTable()
		
		elif "SELECT *" in user_says.upper():			#user input contains Select , calls select Table method
			input04 = user_says[:-1]
			list04 = input04.upper().split(" ")
			fileName04 = list04[3]
			check=" "
			selectTable(check)
		
		elif "INSERT INTO" in user_says.upper():    #user input contains Insert Into , calls Inserti nto()  method
			templist=user_says[:-1].split(" ")
			filename=templist[2]
			insertInto()
			
		elif "UPDATE" in user_says.upper():       #user input contains Update Into , calls Update ()  method
			temp=user_says.strip(";")
			List=temp.split(" ")
			filename05=List[1]
			updateTable()
			#print(success)
		
		elif "BEGIN" in user_says.upper():		#user input contains BEGIN keyword, calls begin() method
			begin()
			
			
		elif "COMMIT" in user_says.upper():		#user input contains COMMIT keyword, calls commit() method.
			commit()
			
				
		
			
		else:
			pass
	except EOFError:
		
		break
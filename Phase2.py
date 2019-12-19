#***************************************************************************************
# CS 657 			:Programming assignment 2
# Author			:Sowmya Kudva
# Date 				:14/03/2019
# Functionalities 	:Database table Updating,Inserting, Table deletion, selection
# Language			:Python
#***************************************************************************************
import re,os

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

#****************************************************************************************
def updateTable():
	
		if os.path.isdir(db_used):
			#try:
				filepath= db_used+"/"+filename+".txt"
				out= db_used+"/"+"out.txt"
				if not os.path.isfile(filepath):		#check if file not exists is true
					print("!Failed to insert into table "+ filename +" because it does not exist.")
				else :
					col1=List[3]						#stores the values provided by user in variables
					
					col2=List[7]
					
					newvalue1=List[5]
					value1=newvalue1.strip("'")
					newvalue2=List[9]
					value2=newvalue2.strip("'")
					#print(value2)
					#contents = open(filepath).read()
					#print(contents)
					if col1==col2:
					
						if value2 not in open(filepath).read():
							print("No records found for ()".format(value2))
						else:
							with open(filepath, "rt") as fin:
								with open(out, "wt") as fout:
									for line in fin:
										
										fout.write(line.replace(value2, value1))  #to update with the new value, using replace function
									os.remove(filepath)
									os.rename(out,filepath)
									print("1 record modified.")
					else:
						
						if value2 not in open(filepath).read():
							print("No records found for " +value2)
						else:
							with open(filepath, "rt") as fin:
								with open(out, "wt") as fout:
									for line in fin:
										line=line.split("|")
										if value2 == line[1]:     				#checks if the keyed in value is present in line read from file
											line[2]=value1+'\n'					#keeps the value provided by user to the 2nd index of line read
												#temp = (value2+ "| "+value1).strip("'")
											line1='|'.join(line)
											
											fout.write(line1)					#writes line to the new file
										
										else:
											line1='|'.join(line)
											fout.write(line1)	
									os.remove(filepath)
									os.rename(out,filepath)						#renames the new file after deleting the old file
									print("2 records modified.")
					
					
					
		else :
			db_used == " "
			print("DB is not selected")



#****************************************************************************************
#METHIOD: DeleteFrom()
#This method is called when User issues Delete from table command

#****************************************************************************************
def DeleteFrom():
	
		if os.path.isdir(db_used):
			#try:
				filepath= db_used+"/"+filename+".txt"
				out=db_used+"/"+"out.txt"
				if not os.path.isfile(filepath):		#check if file not exists is true
					print("!Failed to insert into table "+ filename +" because it does not exist.")
				elif List[4]=='name':  
					
					newvalue1=List[6]
					value1=newvalue1.strip("'")
					
					if value1 not in open(filepath).read():
						print("No records found for ()".format(value2))
					else:
						with open(filepath, "rt") as fin:   #opens to read file  
							with open(out, "wt") as fout:   #open to write to a new file out.txt
								for line in fin:
									line=line.split("|")
									
									if value1 != line[1]:    # checks if the column value passed by query is not present in the line read
										line='|'.join(line)
										fout.write(line)     #then writes that line to the new file
										
							
								os.remove(filepath)          #deletes the old file
								os.rename(out,filepath)      #renames the new file
								print("2 records deleted.")
				elif List[4] =='price':
				 	
					newvalue=List[6]
					value1=newvalue.strip("'")
					with open(filepath, "rt") as fin:       #open the file
						with open(out, "wt") as fout:       #opens another file to write
							for line in fin:
								line=line.split("|")
						
								
								if ('price' in line[2]):    
									line='|'.join(line)
									fout.write(line)
								elif float(line[2]) < float(value1):  #checks if the the price is less that value passed
									line='|'.join(line)
									fout.write(line)				  #then writes that line to new file
										 
							os.remove(filepath)						  #removes old file
							os.rename(out,filepath)					  #renames new file
							print("1 record deleted.")
									
									
									
								
										
				else:
						pass
		else :
			db_used == " "
			print("DB is not selected")
		



#************************************************* end of deleteFrom() method ********************************************************

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
			fileName02 = list02[2].lower()
			s2 = input02.split(None, 3)[3]	#chops off the first 3 words and considers only the column names and datatypes
			createTable()
		elif ("SELECT NAME") in user_says.upper():	#user input contains Select column names , calls select ()  method
			input01 = user_says[:-1]
			list = input01.upper().split(" ")
			fileName04= list[4]
			check =list[8]
			selectTable(check)
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
			filename=List[1]
			updateTable()
		elif "DELETE FROM" in user_says.upper():     #user input contains delete from table , calls delete ()  method
			temp=user_says.strip(";")
			List=temp.split(" ")
			filename=List[2]
			DeleteFrom()
			
		else:
			pass
	except EOFError:
		
		break
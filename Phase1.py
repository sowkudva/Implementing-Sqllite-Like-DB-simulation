
#***************************************************************************************
# CS 657 			:Programming assignment 1
# Author			:Sowmya Kudva
# Date 				:21/02/2019
# Functionalities 	:Database creation,deletion, Table creation, Deletion, Alteration, Query
# Language			:Python
#***************************************************************************************
import os

#global settings
mypath="/Users/sk/Documents/CS657/PA1/"
db_used=" "

#****************************************************************************************
#METHIOD: createDBmethod()
#This method is called when User issues create DB command

#****************************************************************************************
def createDBmethod():
	try:
		os.mkdir(mypath+dirName)
		print("Database "+dirName+" created.")
	except FileExistsError:   		# if the directory is already present at the location
		print("!Failed to create database "+dirName+" because it already exists.")



#****************************************************************************************
#METHIOD: dropDBmethod()
#This method is called when User issues drop DB command

#****************************************************************************************
def dropDBmethod():
	try:
		os.rmdir(mypath+dirName)
		print("Database "+ dirName +" deleted.")
	except : 
		print("!Failed to delete  "+dirName+" because it does not exist.")


#****************************************************************************************
#METHIOD: createTable()
#This method is called when User issues create table command

#****************************************************************************************
def createTable():
	try:
		if os.path.isdir(mypath+db_used):
			try:
				filepath= mypath+db_used+"/"+fileName02+".txt" #creates a filepath
				
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
#METHIOD: dropTable()
#This method is called when User issues drop table command

#****************************************************************************************
def dropTable():
	try:
		if os.path.isdir(mypath+db_used):
			try:
				filepath= mypath+db_used+"/"+fileName03+".txt"
				
				if not (os.path.isfile(filepath)):			 # checks if the file does not exist is true
					print("!Failed to delete table " + fileName03 +" because it does not exists.")
				else : 										 #removes the file from the directory path
					os.remove(filepath)
					print("Table "+fileName03 +" deleted.")
			except FileNotFoundError:
				print("!Failed to delete table " + fileName03 +" because it does not exists.")
			
			
		else :
			db_used == " "
			print("DB is not selected")
	except:
		print("e :DB is not selected")	
		
#****************************************************************************************
#METHIOD: selectTable()
#This method is called when User issues select * from Table  command

#****************************************************************************************
def selectTable():	
	try:
		if os.path.isdir(mypath+db_used):
			try:
				filepath= mypath+db_used+"/"+fileName04+".txt"
				
				if not os.path.isfile(filepath):		#check if file not exists is true
					print("!Failed to query table "+ fileName04 +" because it does not exist.")
				else :
					newfile= open(filepath, "r")		#opens file in read mode
					if newfile.mode == 'r':
						contents =newfile.read()        #reads the contents of the opened file
						print(contents)					#prints the contents of the file to console
						newfile.close()

						
					
			except FileNotFoundError:
				print("!Failed to query table "+ fileName04 +" because it does not exist.")
			
			
		else :
			db_used == " "
			print("DB is not selected")
	except:
		print("e :DB is not selected")
		

#****************************************************************************************
#METHIOD: useDirectory(urdir,urpath)
#This method is called when User issues use DB command

#****************************************************************************************
def useDirectory(urdir,urpath):
	try:
		if os.path.isdir(urpath+urdir):
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
#METHIOD: alterTable()
#This method is called when User issues alter table command

#****************************************************************************************
def alterTable():
	try:
		if os.path.isdir(mypath+db_used):
			try:
				filepath= mypath+db_used+"/"+fileName05+".txt"
				
				if not os.path.isfile(filepath):	
					print("!Failed to alter "+ fileName05 +"because it does not exists.")
				
				#if the file exists but is null, then add the value provided by the user without first character as |	
				elif os.path.exists(filepath) and os.path.getsize(filepath)==0:
					newfile= open(filepath, "a")
					newfile.write(s3.replace(",","|"))
					print("Table "+ fileName05 +" modified.")
				#if file exists then appends the file contents with the user provided values with a | as seperator
				else :
					newfile= open(filepath, "a")
					newfile.write("| "+s3.replace(",","|"))
					print("Table "+ fileName05 +" modified.")
			except FileNotFoundError:
				print("!Failed to alter "+ fileName05 +"because it does not exists.")			
		else :
			db_used == " "
			print("DB is not selected")
	except:
		print("DB is not selected")


while True:
	try :
		user_says = input().strip()      			#accepts user inputs
		if user_says.lower() == ".exit":			
			print("All done.")
			break
		
		elif "USE" in user_says.upper():			#user input contains USE keyword calls method UseDirectory
			input01 = user_says[:-1]
			list01 = input01.upper().split(" ")
			dirName01 = list01[1].lower()
			useDirectory(dirName01, mypath)
			
		
		elif "CREATE TABLE" in user_says.upper():	#user input contains CREATE calls createTable() method
			input02 = user_says[:-1]
			list02 = input02.upper().split(" ")
			fileName02 = list02[2].lower()
			s2 = input02.split(None, 3)[3]
			createTable()
		
		elif "DROP TABLE" in user_says.upper():		#user input contains DROP table, calls DropTable method
			input03 = user_says[:-1]
			list03 = input03.upper().split(" ")
			fileName03 = list03[2].lower()
			dropTable()
		elif "SELECT" in user_says.upper():			#user input contains Select , calls select Table method
			input04 = user_says[:-1]
			list04 = input04.upper().split(" ")
			fileName04 = list04[3].lower()
			selectTable()
		elif "ALTER TABLE" in user_says.upper():	#user input contains ALTER table, calls alter tablemethod
			input05 = user_says[:-1]
			list05 = input05.upper().split(" ")
			fileName05 = list05[2].lower()
			s3 = input05.split(None, 4)[4]
			alterTable()
			
		elif "CREATE DATABASE" in user_says.upper(): #input contains createDatabase, calls createdatabase method()
			input_1 = user_says[:-1]
			list1 = input_1.upper().split(" ")
			dirName = list1[2].lower()
			createDBmethod();			 
		elif "DROP DATABASE" in user_says.upper(): #input contains drop database, calls drop database method
			input_1 = user_says[:-1]
			list1 = input_1.upper().split(" ")
			dirName = list1[2].lower()
			dropDBmethod();
			
		else: #anything other than the stated keywords, will be passed on to obtain next input
			pass
	except EOFError:
		
		break
		


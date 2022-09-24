import os

listofiledict={}
directoryName=""
path=""
def showfiles():
	directoryName=input("Enter your directory name with full path")
	#print(os.system(('ls %s -l')% directoryName))
	listFiles=os.listdir(directoryName)
	i=1;
	for f in listFiles:
		path=directoryName + "/" + f
		#print(i,os.system(('ls -l %s')% '"'+path+'"'))
		listofiledict[i]=path
		i+=1
		
def delfileaction():
	delyes=input("Do you want to delte file Enter yes or no ")
	if(delyes == "yes" or delyes == "y"):
			delfileNum=input("Enter the seq number to delete the file")
			delfile(delfileNum)
	if(delyes == "no" or delyes == "n"):
			exit()
def choosefuncrtion():
	action=input("Enter your action: showlist or delete")
	print(action)
	if(action == "showlist"):
		showfiles()
	if(action == "delete"):
		showfiles()
		delfileaction()

def delfile(delfileNum):
	print(listofiledict)
	filestodel=listofiledict[int(delfileNum)]
	delaction=os.system(('rm %s -f')% filestodel)
	delyes=input("Do you want to delte more file Enter yes or no")
	if(delyes == "yes" or delyes == "y"):
			delfileNum=input("Enter the seq number to delete the file")
			delfile(delfileNum)
	if(delyes == "no" or delyes == "n"):
			exit()


choosefuncrtion()



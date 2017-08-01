import os
from sys import argv

script, srcfolder, destination = argv




#Creates list of names based on file names in the folder
names = os.listdir(srcfolder)
###print names
###print (srcfolder + names[8])



# if file contains parenthesis, delete it
for file in names:
	if "(" in file:
		print destination + file
		os.rename(srcfolder + file, destination + file)


print "end"


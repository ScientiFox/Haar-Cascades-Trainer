###
#
# Create BG
#  A quick script to generate a BG file for a Haar Cascade trainer
#
#
###

#Standard imports
import math,time,random

#File handling
import glob

#Load in source files from sample img folder
files = glob.glob("img//*")

#File string
f_str = ""
for a in files: #For each file
    f_str = f_str + a + "\n" #add to the string for bg filr

#Open up the file, write, and close
f_op = open("bg.txt",'w')
f_op.write(f_str)
f_op.close()








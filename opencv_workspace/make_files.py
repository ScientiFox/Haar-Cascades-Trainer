import cv2

import math,time,random

import glob

files = glob.glob("other neg/*")

N = 500

bg_f = open("bg.txt",'w+')

for a in range(500):
	r = random.randint(0,len(files)-1)
	f = files[r]
	files = files[:r] + files[r+1:]
	img = cv2.imread(f)
	imout = cv2.imwrite("neg/"+f.split("/")[-1],img)
	bg_f.write("neg/"+f.split("/")[-1] + "\n")

bg_f.close()

###
#
# Haar Cascade test
#  This script tests a generated set of Haar Cascades against 
#  a set of positive and negative target images. This particular
#  test structure assumes a set of more than one target cascade,
#  because the original system was designed to detect pushbars
#  on doors, and needed to detect multiple styles, for which
#  generating a cascade for each type is faster and more efficient.
#
###

#Standard imports
import math,time,random

#Math libraries
import numpy as np
import cv2

#File imports
import glob

#Number of positive and negative samples
N_pos = 30
N_neg = 30

#Negative examples file load
negs = glob.glob("neg/*.jpg")

#List of negative images
imgs_negs = []

#FOr the number of negatives to pull
for a in range(N_neg):
	r = random.randint(0,len(negs)-1) #Grab a random number
	imgs_negs = imgs_negs + [(negs[r],cv2.imread(negs[r]))] #Pull in that randome number- keep its index
	negs = negs[:r]+negs[r+1:] #remove that negative so it doesn't get re-used

#Load the positive image list
pos_file = open("info/info.lst",'r')
pos_lines = pos_file.readlines() #Read in the positives

#Make a list of the positives
imgs_pos = []

#For the positives
for a in range(N_pos):
	r = random.randint(0,len(pos_lines)-1) #Grab a random number
	p_tag = pos_lines[r] #Grab the rth indexed positive element
	pos_lines = pos_lines[:r] + pos_lines[r+1:] #Remove them from the lost for no reuse

        #Process the tage
	p_tag = p_tag.split(" ") #Split by spaces
	p_img = cv2.imread("info/"+p_tag[0]) #Grab the image itself
	p_region = p_tag[2:] #Get the noted positive location value
	p_region = [int(b) for b in p_region] #Convert the target region coords from strings

        #Make the positive list with labels, image and region of interest
	imgs_pos = imgs_pos + [(p_tag[0],p_img,p_region)]

#Load in the cascade xml
cascades = glob.glob("cascades/pushbarCascade*.xml")
c_l  = 1.0*len(cascades) #float index for iterative coloring

#Initial color value
color = 0

#For each cascade we have (each covers a different pushbar style)
for casc in cascades:
	pb_cascade = cv2.CascadeClassifier(casc) #Make a classifier

        #Print out negative tests
	print(casc+"--------")
	print("  negs")

        #For each negative
	for img in imgs_negs:
		print("  "+img[0]) #Print the image
		print("  (-)")
		pbs = pb_cascade.detectMultiScale(img[1],1.05,1) #Do Haar Cascade detection
		for box in pbs: #For each ID'd box, print the coords
			print("    "+str(box))

        #Now for the positive tests
	print("  pos")
	for img in imgs_pos:
		print("  "+img[0]) #Print the image
		print("  "+str(img[2]))
		pbs = pb_cascade.detectMultiScale(img[1],1.05,1) #Do Haar Cascade detection
		im_out = np.copy(img[1]) #Copy output image

                #for each detected box
		for box in pbs:
                        #Draw the boxes detected and print the coords- box drawn in different colors for each cascade
			cv2.rectangle(im_out,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),(int(255-200*(color/c_l)),0,int(200*(color/c_l))),2)
			print("    "+str(box))

                #Display output image and label text
		im_out = cv2.resize(im_out,(300,300))
		cv2.putText(im_out,casc,(10,290),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
		cv2.imshow("Cascade_output",im_out)
		cv2.waitKey(500) #2Hz update rate

        #Increment the color
	color+=1

#Clear the windows and note done
cv2.destroyAllWindows()
print("Done")		
		
	




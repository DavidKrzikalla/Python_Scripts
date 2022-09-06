# -*- coding: utf-8 -*-
"""
The script takes all pictures in a specified folder and crops them according to specified rectangle. 
The rectagular area is maintained. The area is specified in px. The cropped pictured then replace the original ones.
Author: David Krzikalla

"""


#Import required Image library
from PIL import Image
import os 


# Set corners of the cropping rectangle
left = 1 
top = 200
right = 5545
bottom = 2560



os.chdir('C:/Users/david.krzikalla/Desktop/image_crop/figs') # set current directory

folder_content = os.listdir() # gets content of the current directory

for i in range (len(folder_content)):


    #Create an Image Object from an Image
    im = Image.open(folder_content[i])
    
    #Display actual image
    #im.show()
    
    
    #Crop
    cropped = im.crop((left,top,right,bottom))
    
    #Display the cropped portion
    #cropped.show()
    
    #Save the cropped image (overwrite the original image)
    cropped.save(folder_content[i]) 
    

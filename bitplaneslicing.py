#Code contributors
#Sharvil Bhatt
#Shubham Pandey
#Shreyansh Jain
#We took help from the official documentanions and github repository of opencv and numpy.
#We also took help from stackoverflow and stackexchange for assisting in development of this code
#We also performed various tests on this piece of code and applied this on various images and of different scales quality assesment done by sharvil bhatt
import numpy as np
import cv2
# to convert the colored image into grayscale
colorimg = cv2.imread('lena_color.tif')
img = cv2.cvtColor(colorimg, cv2.COLOR_BGR2GRAY)



#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8)) # width = no. of bits

# We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.
eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])


#adding up the bitplane images to create respective final images
bit_78_img = eight_bit_img+seven_bit_img
bit_678_img = six_bit_img+seven_bit_img+eight_bit_img
bit_5678_img = five_bit_img+six_bit_img+seven_bit_img+eight_bit_img





#Concatenate this images using cv2.hconcat (horizontal concatenation) to easily display this images
final = cv2.hconcat([bit_78_img,bit_678_img,bit_5678_img])


#scale operation so the image can be visible in a presentable way
scale_percent = 150 # percent of original size
width = int(final.shape[1] * scale_percent / 100)
height = int(final.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(final, dim, interpolation = cv2.INTER_AREA)
 

# Displaying the final resized image
cv2.imshow('a',resized)
#image would be displayed indefinetly until a key is pressed
cv2.waitKey(0) 

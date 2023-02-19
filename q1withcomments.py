import cv2
import numpy as np
image=cv2.imread("lena_color.tif")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


while(1): # 
    print("for orignal image press 1")  
    print("for zoomed image by replication press 2")
    print("for zoomed image by interpolation press 3")
    print("for shrink image using replication press 4")
    print("for shrink image using interpolation press 5")
    print("for exit press 0")
    print("please close the image before pressing another key otherwise next image may not load sometimes") #when we use waitkey(0) the image should close as soon as we press a key but sometimes the image was not closing so on that case close the image manually
    x=int(input());
    if(x==1): #will display orignal image
        cv2.imshow("orignalimage",image)
        cv2.waitKey(0);#closes the image only when a key is pressed,the parameter in waitkey defines for how long the image need to be displayed in milli seconds
    elif(x==2):#replication-zoom
        h=image.shape[0]; # shape return a array of image which stores height at index 0
        w=image.shape[1]; # and width at index 1
        h=h*2;            #here we are magnifying the image by a factor of two so we multiply by two
        w=w*2;
        p=0;q=0;
        imagezoomed=np.zeros((h,w),dtype=np.uint8) #creates an image of size h,w of datatypr uint8=8 bits number
        for i in range(0,h,2) :                   #we are filling the alternate pixels of the image with the pixels of orignal image  
            for j in range(0,w,2):                
                imagezoomed[i,j]=image[p,q]
                q=q+1
        
            p=p+1
    
            q=0  
        for i in range(0,h,2):                  #assigning the same value to neighbouring pixels 
            for j in range(1,w,2):
                imagezoomed[i,j]=imagezoomed[i,j-1];    #ab             aabb 
        for i in range(1,h,2):                          #de   ------->  aabb      
            for j in range(0,w,1):                      #               ddee
                imagezoomed[i,j]=imagezoomed[i-1,j];    #               ddee
 
        
        cv2.imshow("zoomedimage",imagezoomed);
        cv2.waitKey(0);
    elif(x==3):   #zoom-interpolation
        h=image.shape[0];   # shape return a array of image which stores height at index 0
        w=image.shape[1];   # and width at index 1
        h=h*2;              #here we are magnifying the image by a factor of two so we multiply by two
        w=w*2;
        p=0;q=0;
        imagezoomed=np.zeros((h,w),dtype=np.uint8)    #creates an image of size h,w of datatypr uint8=8 bits number
        for i in range(0,h,2) :                        #we are filling the alternate pixels of the image with the pixels of orignal image  
            for j in range(0,w,2):
                imagezoomed[i,j]=image[p,q]
                q=q+1
        
            p=p+1
    
            q=0  
        for i in range(0,h,2):
            for j in range(1,w,2):
                if(j==w-1):
                    imagezoomed[i,j]=imagezoomed[i,j-1]/2;     #for last pixel of a row pixel 
                else:
                    imagezoomed[i,j]=imagezoomed[i,j-1]/2+imagezoomed[i,j+1]/2; #setting the value of pixel as the average of the value of adjacent pixel in the same row
        for i in range(1,h,2):
             for j in range(0,w,1):
                if(i==h-1):
                    imagezoomed[i,j]=imagezoomed[i-1,j]/2;   #for pixels in the last row 
                else:
                    imagezoomed[i,j]=imagezoomed[i-1,j]/2+imagezoomed[i+1,j]/2;   #setting the value of pixel as the average of the value of adjacent pixel in the same column 
 
        #image zoomed by interpolation will be of better quality than tha obtained by replication
        cv2.imshow("output",imagezoomed);
        cv2.waitKey(0);
    elif(x==4):   #shrink-replication
        h=image.shape[0];
        w=image.shape[1];
        h=h//2;    # height and width of the new image are half of the size of orignal image as we are scalin down by a factor if two
        w=w//2;
        p=0;q=0;
        imageshrink=np.zeros((h,w),dtype=np.uint8)
        for i in range(0,h) :            #assigning value to pixels of new image
            for j in range(0,w):
                imageshrink[i,j]=image[p,q]            #abcd
                q=q+2                                  #efgh                 ac
                                                       #ijkl          ------>ik                                           #mnop
            p=p+2                                      #mnop
    
            q=0  
        cv2.imshow("output",imageshrink);
        cv2.waitKey(0);
    elif(x==5):     #shrink-interpolation
        h=image.shape[0];
        w=image.shape[1];
        h=h//2;
        w=w//2;
        p=0;q=0;
        imageshrink=np.zeros((h,w),dtype=np.uint8)
        cv2.imshow("output",imageshrink);
        for i in range(0,h) :
            for j in range(0,w):
                if(q==w-1):
                    imageshrink[i,j]=image[p,q]/2              #for last pixel of row
                else:
                    imageshrink[i,j]=image[p,q]/2+image[p,q+1]/2  # instead of simply skipping the pixel we are assigning the average value of adjacent pixel to the new image
                q=q+2
        
            p=p+2
    
            q=0  
 
        
    
        cv2.imshow("output",imageshrink);
        cv2.waitKey(0);
    elif(x==0):
        break
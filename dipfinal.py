import cv2
import numpy as np
image=cv2.imread("C:\DIP\lena_color.tif")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


while(1):
    print("for orignal image press 1")
    print("for zoomed image by replication press 2")
    print("for zoomed image by interpolation press 3")
    print("for shrink image using replication press 4")
    print("for shrink image using interpolation press 5")
    print("for exit press 0")
    print("please close the image before pressing another key otherwise next image may not load sometimes")
    x=int(input());
    if(x==1):
        cv2.imshow("orignalimage",image)
        cv2.waitKey(0);
    elif(x==2):
        h=image.shape[0];
        w=image.shape[1];
        h=h*2;
        w=w*2;
        p=0;q=0;
        imagezoomed=np.zeros((h,w),dtype=np.uint8)
        for i in range(0,h,2) :
            for j in range(0,w,2):
                imagezoomed[i,j]=image[p,q]
                q=q+1
        
            p=p+1
    
            q=0  
        for i in range(0,h,2):
            for j in range(1,w,2):
                imagezoomed[i,j]=imagezoomed[i,j-1];


        for i in range(1,h,2):
            for j in range(0,w,1):
                imagezoomed[i,j]=imagezoomed[i-1,j];
 
        

        cv2.imshow("zoomedimage",imagezoomed);

        cv2.waitKey(0);
    elif(x==3):
        h=image.shape[0];
        w=image.shape[1];
        h=h*2;
        w=w*2;
        p=0;q=0;
        imagezoomed=np.zeros((h,w),dtype=np.uint8)
        for i in range(0,h,2) :
            for j in range(0,w,2):
                imagezoomed[i,j]=image[p,q]
                q=q+1
        
            p=p+1
    
            q=0  
        for i in range(0,h,2):
            for j in range(1,w,2):
                if(j==w-1):
                    imagezoomed[i,j]=imagezoomed[i,j-1]/2;
                else:
                    imagezoomed[i,j]=imagezoomed[i,j-1]/2+imagezoomed[i,j+1]/2;


        for i in range(1,h,2):
             for j in range(0,w,1):
                if(i==h-1):
                    imagezoomed[i,j]=imagezoomed[i-1,j]/2;
                else:
                    imagezoomed[i,j]=imagezoomed[i-1,j]/2+imagezoomed[i+1,j]/2;
 
        

        cv2.imshow("output",imagezoomed);

        cv2.waitKey(0);
    elif(x==4):
        h=image.shape[0];
        w=image.shape[1];
        h=h//2;
        w=w//2;
        p=0;q=0;
        imageshrink=np.zeros((h,w),dtype=np.uint8)

        for i in range(0,h) :
            for j in range(0,w):
                imageshrink[i,j]=image[p,q]
                q=q+2
        
            p=p+2
    
            q=0  

        cv2.imshow("output",imageshrink);

        cv2.waitKey(0);
    elif(x==5):
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
                    imageshrink[i,j]=image[p,q]/2
                else:
                    imageshrink[i,j]=image[p,q]/2+image[p,q+1]/2
                q=q+2
        
            p=p+2
    
            q=0  

 
        
    
        cv2.imshow("output",imageshrink);

        cv2.waitKey(0);
    elif(x==0):
        break
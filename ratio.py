import cv2
import numpy as np
import sys

def main(tes):
    img = cv2.imread(''+tes+'')
    	 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    sensitivity = 50
    lower = np.array([0,0,255-sensitivity])
    upper = np.array([255,sensitivity,255])
    
    
    mask = cv2.inRange(hsv,lower, upper)
    target = cv2.bitwise_and(img,img, mask=mask)
    
    cv2.imshow("Piece", target)
    
    #Count how many of each pixel , eg : Black & White Ratio
    cv2.waitKey(0)
    
    #img[img!= 0] = 0
    
    #print(target[767,1023])
    
    
    np.set_printoptions(threshold=np.inf)
    
    a = np.any(target == [0, 0, 0], axis=-1)
    
    contador_w = 0
    contador_b = 0
    
    for row in range(0,target.shape[0]):
        for col in range (0,target.shape[1]):
        	if a[row,col] == True:
        		contador_b+=1
        		#print (row,col)
        		#print(target[row,col], row, col)
        	else:
        		contador_w+=1	
    
    
    #print(contador)
    #print(img.shape)
    
    
    #TOTAL BLACK  1681
    #TOTAL PIXELS 22033
    #TOTAL WHITE  3406
    
    black = contador_b*100	
    
    total = contador_w + contador_b
    
    print(black)
    print(total)
    
    print("B&W Ratio : ", round(black/total),"%")


if __name__ ==  "__main__":   
    main(sys.argv[1])
        


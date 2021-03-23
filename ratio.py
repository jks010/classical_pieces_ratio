import cv2
import numpy as np
import sys, time
def main(tes):
    start_time = time.time()
    img = cv2.imread(''+tes+'')
    	 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    sensitivity = 50
    lower = np.array([0,0,255-sensitivity])
    upper = np.array([255,sensitivity,255])
    
    
    mask = cv2.inRange(hsv,lower, upper)
    target = cv2.bitwise_and(img,img, mask=mask)
    
    #cv2.imshow("Piece", target)
    
    #cv2.waitKey(0)
    
    
    
    total = np.prod(target.shape)
    x = np.reshape(target, (total,))
    
    np.set_printoptions(threshold=np.inf)
    
    
    
    x.sort()
    
    
    i = total-1
    contei = 0
    while (i >0):
        if(x[i]==0):
            contei=i
            break
        i = i-200
    
    gg =  total - contei
    print(round((contei*100)/total),"%")
    print("--- %.3s seconds ---" % (time.time() - start_time))
    

if __name__ ==  "__main__":   
    main(sys.argv[1])
        


# To convert colored images into grayscale (Black and White)
# This will remove RGB channels from your images 

import cv2 as cv2
import os

path = input("Enter path of source folder(with / at the end): ")
outPath = input("Enter path of destination folder(with / at the end): ")
done = 0        # for counting number of images
cnt = 1         # counter variable for naming
int(cnt)        # conversion of str to int datatype
for img in os.listdir(path):
    try:
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)   # grayscale conversion 
        outName = (outPath + "img" + str(cnt))      # naming new image 
        cv2.imwrite(outName +".jpg", img_array)     # writing new image in the given directory  
        cnt = cnt + 1       
        print(outName +".jpg :" + " ✅")     # for printing result in after successful conversion 
        done = done + 1     
    except Exception as e:
                pass
print("👍🏻 " + str(done) + " images are successfuly converted into gray scale.")


# Written by Ishan Jawade
# email: ishankjawade@gmail.com

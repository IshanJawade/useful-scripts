import cv2 as cv2
import os

path = input("Enter path of source folder(with / at the end): ")
outPath = input("Enter path of destination folder(with / at the end): ")
done = 0
cnt = 1
int(cnt)
for img in os.listdir(path):
    try:
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        outName = (outPath + "img" + str(cnt))
        cv2.imwrite(outName +".jpg", img_array) 
        cnt=cnt+1
        print(outName +".jpg :" + " ✅")
        done = done + 1
    except Exception as e:
                pass
print("👍🏻 " + str(done) + " images are successfuly converted into gray scale.")


# Written by Ishan Jawade
# email: ishankjawade@gmail.com
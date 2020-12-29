import os
import re
import shutil 

path = input("Enter path of source folder: ")
one = input("What is your division factor? ")
desPath_one = input("Enter the path for first class: ")
desPath_two = input("Enter the path for second class: ")
classOneCount = 0
classTwoCount = 0

for img in os.listdir(path):
    try:
       cat_match = re.match(one, img)
       if cat_match:
           shutil.copy2(os.path.join(path, img), desPath_one)
           print(img + " >>> " + desPath_one + " ✅")
           classOneCount = classOneCount + 1
       else:
            shutil.copy2(os.path.join(path, img), desPath_two)
            print(img + " >>> " + desPath_two + " ✅")
            classTwoCount = classTwoCount + 1
    except Exception as e:
              pass

print("Results:")
print(int(classOneCount), " >>> " + desPath_one)
print(int(classTwoCount), " >>> " + desPath_two)

# Written by Ishan Jawade
# email: ishankjawade@gmail.com
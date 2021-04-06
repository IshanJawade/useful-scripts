# If google allocated T4 or not

!nvidia-smi -L >> test.txt
f = open("test.txt", "r")
outLine = f.readline()
index = outLine.find("T4")
if (index > -1):
  print("Maderchod Google! BC")
else:
  print("Nahi Changlay BC !")
import re
k = ("Hello")
m = re.findall("Hello", k) #----- method 1
if m:
  print("True")
else:
  print("False")


c = ("Corona")
k = re.search("Carona", c)
if k:
  print("True")
else:
  print("False")

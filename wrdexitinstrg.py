import re
k = ("Hello")
m = re.findall("Hello", k) #----- method 1
if m:
  print("True")
else:
  print("False")
#---------------------------------------------------

c = ("Corona")
k = re.search("Carona", c) #------  Method 2
if k:
  print("True")
else:
  print("False")

#--------------------------------------------------

def search(word, sentence):    #  method 3
  if word in sentence:
    return True
  else:
    return False

print(search('ssh', 'secure shell hashing is also known as ssh'))

#------------------------------------------------------------


import re
def using_regex(word, sentence):
  match = re.search(word, sentence)  # method 4
  if match:
    return True
  else:
    return False

print(using_regex('ssh', 'secure shell hashing is also known as ssh'))
#-------------------------------------------------------------------------

def using_string_find_method(word, sentence): # method 5
  match = sentence.find(word)
  if match != -1:
    return True
  else:
    return False
print(using_string_find_method("ssh", "secure shell hashing is also known as ssh"))

# ---------------------------------------------------------------------------------------

import operator
def using_operator(word, sentence):
  if not operator.contains(word, sentence): # method 6
    return False
  else:
    return True
print(using_operator("secure shell hasing is also known as ssh", "ssh"))

#--------------------------------------------------------------------------

def using_string_index(word, sentence):
  try:
    if sentence.index(word): # method 7
      return True
    else:
      return False
  except ValueError as e:
    print(e.message, "cannot find a index for the given word => {}, hence returning None".format(word))
print(using_string_index("ssh", "secure shell hashing is also known as ssh"))

#-----------------------------------------------------------------------------------




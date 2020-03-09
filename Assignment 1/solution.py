import sys
def caeser(operation, key, inFile, outFile):
  #convert the key from string to int
  key = int(key)
  #msg will contain the message
  msg = ""
  #Read the text from the input file
  f=open(inFile, "r")
  #ensure that the file is open
  if f.mode == 'r':
    content = f.read()
    #for every char in the input file
    for c in content:
      #get the ascii of the char
      c = ord(c)
      if(operation == "decrypt"):
        c = caeserDec(c, key)
      else:
        c = caeserEnc(c, key)
      #get back the char of its ascii
      c = chr(c)
      #append to the msg
      msg += c
    f.close()
  #Write the text in the output file
  f = open(outFile, "w")
  if f.mode == 'w':
    f.write(msg)
    f.close()
  if operation == "decrypt":
    print("Decryption is done!\n")
  else:
    print("Encryption is done!\n")


def caeserDec(c, key):
  #the char is small
  if(c >= a and c <= z):
    c = ((c-a - key+26)%26)+a         #Wigo core equation
  #the char is capital
  elif (c >= A and c <= Z):
    c = ((c-A - key+26)%26)+A         #Wigo core equation
  return c
    

def caeserEnc(c, key):
  #the char is small
  if(c >= a and c <= z):
    c = ((c-a + key)%26)+a            #Wigo core equation
  #the char is capital
  elif (c >= A and c <= Z):
    c = ((c-A + key)%26)+A            #Wigo core equation
  return c

def affine(operation, keya, keyb, inFile, outFile):
  #convert the key from string to int
  keya, keyb, invkeya = int(keya), int(keyb), 0
  if(operation == "decrypt"):
    for i in range(26):
      if(keya*i%26 == 1):
        invkeya = i
        break
    #print(invkeya)
  #msg will contain the encrypted message
  msg = ""
  #Read the plain text from the input file
  f=open(inFile, "r")
  #ensure that the file is open
  if f.mode == 'r':
    content = f.read()
    #for every char in the input file
    for c in content:
      #get the ascii of the char
      c = ord(c)
      if(operation == "decrypt"):
        c = affineDec(invkeya, keyb, c)
      else:
        c = affineEnc(keya, keyb, c)
      #get back the char of its ascii
      c = chr(c)
      #append to the msg
      msg += c
    #print(msg)
    f.close()
  #Write the encrypted text in the output file
  f = open(outFile, "w")
  if f.mode == 'w':
    f.write(msg)
    f.close()
  print("Encryption is done!")


def affineDec(invkeya, keyb, c):
  #the char is small
  if(c >= a and c <= z):
    c = (invkeya*(c-a+keyb))%26+a     #Wigo core equation
  #the char is capital
  elif (c >= A and c <= Z):
    c = (invkeya*(c-A+keyb))%26+A     #Wigo core equation
  return c

def affineEnc(keya, keyb, c):
  #the char is small
  if(c >= a and c <= z):
    c = (keya*(c-a)+keyb)%26+a        #Wigo core equation
  #the char is capital
  elif (c >= A and c <= Z):
    c = (keya*(c-A)+keyb)%26+A        #Wigo core equation
  return c

def vigenere(operation, key, inFile, outFile):
  key = key.lower()
  #msg will contain the message
  msg = ""
  #Read the text from the input file
  f=open(inFile, "r")
  #ensure that the file is open
  if f.mode == 'r':
    content = f.read()
    #for every char in the input file
    i = 0
    for c in content:
      #corresponding chr in key
      b = key[i%len(key)]
      c = ord(c)
      if(operation == "decrypt"):
        c = vigDec(c, b)
      else:
        c = vigEnc(c, b)
      #append to the msg
      msg += c
      i+=1
    f.close()
  #Write the text in the output file
  f = open(outFile, "w")
  if f.mode == 'w':
    f.write(msg)
    f.close()
  if operation == "decrypt":
    print("Decryption is done!\n")
  else:
    print("Encryption is done!\n")

def vigDec(c, b):
  #the char is small
  if(c >= a and c <= z):
    shiftAmount = ord(b)-a
    c = chr((c-a-shiftAmount+26)%26+a)
  #the char is capital
  elif (c >= A and c <= Z):
    shiftAmount = ord(b)-a
    c = chr((c-A-shiftAmount+26)%26+A)
  return c

def vigEnc(c, b):
  #the char is small
  if(c >= a and c <= z):
    shiftAmount = ord(b)-a
    c = chr((c-a+shiftAmount)%26+a)
  #the char is capital
  elif (c >= A and c <= Z):
    shiftAmount = ord(b)-a
    c = chr((c-A+shiftAmount)%26+A)
  return c

def main(argv):
  if argv[1] == "shift":
    operation, inFile, outFile, key = argv[2:]
    caeser(operation, key, inFile, outFile)
  elif argv[1] == "affine":
    operation, inFile, outFile, keya, keyb = argv[2:]
    affine(operation, keya, keyb, inFile, outFile)
  elif argv[1] == "vigenere":
    operation, inFile, outFile, key = argv[2:]
    vigenere(operation, key, inFile, outFile)

#get the ascii of needed chars
a, A, z, Z = ord('a'), ord('A'), ord('z'), ord('Z')
main(sys.argv)

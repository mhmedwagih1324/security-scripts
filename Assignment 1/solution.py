import sys

def ceaserDec(key, inFile, outFile):
  #convert the key from string to int
  key = int(key)
  #msg will contain the decrypted message
  msg = ""
  #Read the cipher text from the input file
  f=open(inFile, "r")
  #ensure that the file is open
  if f.mode == 'r':
    content = f.read()
    #get the ascii of needed chars
    a, A, z, Z = ord('a'), ord('A'), ord('z'), ord('Z')
    #for every char in the input file
    for c in content:
      #get the ascii of the char
      c = ord(c)
      #the char is small
      if(c >= a and c <= z):
        c = ((c-a - key+26)%26)+a         #Wigo core equation
      #the char is capital
      elif (c >= A and c <= Z):
        c = ((c-A - key+26)%26)+A         #Wigo core equation
      #get back the char of its ascii
      c = chr(c)
      #append to the msg
      msg += c
    #print(msg)
    f.close()
  #Write the decrpted text in the output file
  f = open(outFile, "w")
  if f.mode == 'w':
    f.write(msg)
    f.close()
  print("Decryption is done!")

def ceaserEnc(key, inFile, outFile):
  #convert the key from string to int
  key = int(key)
  #msg will contain the encrypted message
  msg = ""
  #Read the plain text from the input file
  f=open(inFile, "r")
  #ensure that the file is open
  if f.mode == 'r':
    content = f.read()
    #get the ascii of needed chars
    a, A, z, Z = ord('a'), ord('A'), ord('z'), ord('Z')
    #for every char in the input file
    for c in content:
      #get the ascii of the char
      c = ord(c)
      #the char is small
      if(c >= a and c <= z):
        c = ((c-a + key)%26)+a            #Wigo core equation
      #the char is capital
      elif (c >= A and c <= Z):
        c = ((c-A + key)%26)+A            #Wigo core equation
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

def affineDec(keya, keyb, inFile, outFile):
  #convert the key from string to int
  keya, keyb, invkeya = int(keya), int(keyb), 0
  #get the inverse of the a key
  for i in range(26):
    if(keya*i%26 == 1):
      invkeya = i
      break
  #msg will contain the decrypted message
  msg = ""
  #Read the cipher text from the input file
  f=open(inFile, "r")
  #ensure that the file is open
  if f.mode == 'r':
    content = f.read()
    #get the ascii of needed chars
    a, A, z, Z = ord('a'), ord('A'), ord('z'), ord('Z')
    #for every char in the input file
    for c in content:
      #get the ascii of the char
      c = ord(c)
      #the char is small
      if(c >= a and c <= z):
        c = (invkeya*(c-a+keyb))%26+a     #Wigo core equation
      #the char is capital
      elif (c >= A and c <= Z):
        c = (invkeya*(c-A+keyb))%26+A     #Wigo core equation
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
  print("Decryption is done!")

def affineEnc(keya, keyb, inFile, outFile):
  #convert the key from string to int
  keya, keyb = int(keya), int(keyb)
  #msg will contain the encrypted message
  msg = ""
  #Read the plain text from the input file
  f=open(inFile, "r")
  #ensure that the file is open
  if f.mode == 'r':
    content = f.read()
    #get the ascii of needed chars
    a, A, z, Z = ord('a'), ord('A'), ord('z'), ord('Z')
    #for every char in the input file
    for c in content:
      #get the ascii of the char
      c = ord(c)
      #the char is small
      if(c >= a and c <= z):
        c = (keya*(c-a)+keyb)%26+a        #Wigo core equation
      #the char is capital
      elif (c >= A and c <= Z):
        c = (keya*(c-A)+keyb)%26+A        #Wigo core equation
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


def main(argv):
  if(argv[1] == "shift"):
    inFile, outFile, key = argv[3:]
    if(argv[2] == "decrypt"):
      ceaserDec(key, inFile, outFile)
    elif(argv[2] == "encrypt"):
      ceaserEnc(key, inFile, outFile)
  elif(argv[1] == "affine"):
    inFile, outFile, keya, keyb = argv[3:]
    if(argv[2] == "decrypt"):
      affineDec(keya, keyb, inFile, outFile)
    elif(argv[2] == "encrypt"):
      affineEnc(keya, keyb, inFile, outFile)
main(sys.argv)

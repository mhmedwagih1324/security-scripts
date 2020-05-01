# What was required?
Write a complete python program to encrypt and decrypt messages using classical ciphers (shift, affine & vigenere)
# What the folder contains?
1. a file which contains the shift, affine and vigenere ciphers encryptors and decryptors ([solution.py](https://github.com/mhmedwagih1324/security-scripts/blob/master/Assignment%201/solution.py)).
2. a file that contains input([in.txt](https://github.com/mhmedwagih1324/security-scripts/blob/master/Assignment%201/in.txt)).
# Usage
You can try this solution by clonning this repo and calling the following lines:
```
#for shift cipher
python solution.py shift encrypt in.txt out.txt k
python solution.py shift decrypt in.txt out.txt k

#for affine cipher
python solution.py affine encrypt in.txt out.txt a b
python solution.py affine decrypt in.txt out.txt a b

#for vigenere cipher
python solution.py vigenere encrypt in.txt out.txt keyword
python solution.py vigenere decrypt in.txt out.txt keyword
```
# A quick demo
you can try also the this [colab notebook](https://colab.research.google.com/drive/1X4AxCszFdQkKsHK2cAehBPKprG9pgkqM)

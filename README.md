# security-scripts
It will contain some python implementations of security ciphers (encryption &amp; decryption)

## Assignment 1
contains a file named solution.py which contains the shift and affine ciphers encryptors and decryptors. You can try the file by calling the following lines:
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
you can try also the this colab notebook https://colab.research.google.com/drive/1X4AxCszFdQkKsHK2cAehBPKprG9pgkqM

# Main concept
The main idea 💡 of the challenge is the XOR operation that is: `A^B^B = A`  

# Explaining 'encrypt.py'  
Encyption steps:  
- Ensure that the number of characters to encrypt is divisible by 16, because the encryption algorithm deals with a block of 16 characters, so we add some `#` symbols to make the last block is 16 characters.
- Digging into the encrypt function, there we see unpack process which translates some bytes to `unsigned integers` and save the resulted 4 integers into `a, b, c, d`.  
- after that we do some XOR operations on these integers for 32 times.  
- then we repack the 4 integers into bytes and add them to the string.  
- we continue encrypting other blocks of characters.
- we save the string to a file named flag.enc.  

# Explaining 'decrypt.py'  
Decryption steps:  
- we open the file flag.enc with the parameter 'rb' which indicates that we are reading bytes.
- we make an empty string then walk through the cipher text as blocks of 16 bytes and call the function decrypt(block), which should decrypt the block and return with the plain text.  
- each time we call the decrypt function, we start by unpacking the block into 4 `unsigned integers`.  
- After that we should reverse the XOR operations for 32 times. 
- then we repack the integers into bytes and put them into a string and cut the string to return only the plain text without "b''" of the string "b'text'"  
- We append all plain texts that were decrypted and print them.

# The function F(w)
a good point that should be remarked while thinking about decrypting the file is the use of function F(w) in the Encryption process, we just need to make sure that the value w that is passed to the function F while decryption is the same value that was used while Encryption to get the same output of that function in the decryption process.  

# More explanation
in the Encrption process the last operation that was done to `a, b, c, d` is the following:  
```
a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337
```
we can break this line into 4 lines but make sure that any change in the values of `a, b, c, d` doesn't affect on the computation of other values, that is a change on a shouldn't affect the computation of b (b should use the old version of a), we can say that the above line is equal to the following 5 lines:  
```
tempa = a
a = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a)
b = b ^ F(d ^ F(tempa) ^ (d | tempa))
c = tempa ^ F(d | F(d) ^ d)
d = d ^ 1337
```
So, we can reverse this line by the following code:
```
# keep a in a temp to use later
tempa = a
# get the old d from the new d
d = d ^ 1337
# get the old a from the new c and the old d
a = c ^ (F(d | F(d) ^ d))
# get the old b from the new b, the old d and a
b = b ^ (F(d ^ F(a) ^ (d | a)))
# get the old c from the new a, the old d, b and a
c = tempa ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
```
the comments on the code should give a sense of the idea behind the solution.

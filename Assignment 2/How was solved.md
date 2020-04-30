# Main concept
The main idea 💡 of the challenge is the XOR operation that is: `A^B^B = A'  

# Explaining 'encrypt.py'  
Encyption steps:  
- Ensure that the number of characters to encrypt is divisible by 16, because the encryption algorithm deals with a block of 16 characters, 
so we add some `#` symbols to make the last block is 16 characters.
- Digging into the encrypt function, there we see unpack process which translates some bytes to `unsigned integers` and save the resulted 4 
integers into `a, b, c, d`.  
- after that we do some XOR operations on these integers for 32 times.  
- then we repack the 4 integers into bytes and add them to the string.  
- we continue encrypting other blocks of characters.
- we save the string to a file named flag.enc.  

# Explaining 'decrypt.py'  
Decryption steps:  
- we open the file flag.enc with the parameter 'rb' which indicates that we are reading bytes.
- we make an empty string then walk through the cipher text as blocks of 16 bytes and call the function decrypt(block), which should decrypt the
block and return with the plain text.  
- each time we call the decrypt function, we start by unpacking the block into 4 `unsigned integers`.  
- After that we should reverse the XOR operations for 32 times. 
- then we repack the integers into bytes and put them into a string and cut the string to return only the plain text without "b''" of the string 
"b'text'"  
- We append all plain texts that were decrypted and print them.

###ASCII

Description - ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

Solution script - ascii.py

Flag - crypto{ASCII_pr1nt4bl3}


###Hex 

Description - When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.
Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.
Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d

Solution script - hex.py

Flag - crypto{You_will_be_working_with_hex_strings_a_lot}


###Base64 

Description - Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.
Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.
Take the below hex string, decode it into bytes and then encode it into Base64.
72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

Solution script - b64.py

Flag - crypto/Base+64+Encoding+is+Web+Safe/


###Bytes and Big Integers 

Description - Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?
The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.
Convert the following integer back into a message:
11515195063862318899931685488813747395775516287289682636499965282714637259206269

Solution script - bytes.py

Flag - crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
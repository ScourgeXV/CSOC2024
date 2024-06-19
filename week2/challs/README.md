###Challenge-1 CSOC23

File - source.enc
       output.txt

Solution - We are given a file source.enc which is basse64 encrypted text. on decrypting we get a python program which is encrypting a file flag.txt with some XOR operation and storing the output in the file output.txt. This program is dividing the flag into blocks of four characters and xoring the first two characters with the four characters for each block and giving the output. Therefore a solution script was written doing this same operation again on the output to give back the input as XOR is a symmetric operation. this gave us hexadecimal ordinals which in ASCII gave the flag.

Flag - CSOC23{345y_ba5364_4nd_x0r?}



###Challenge-2 CSOC23

File - encoded.txt

Solution - We are given a file having some numbers and text. On observing this file contents we can notice that first few numbers are binary data, then we have some hexadecimal data, then some base64 encoded data and lastly some octal numeric data. On converting all these to ASCII text we get 

Flag - CSOC23{ju57_d1ff3r3n7_3nc0d1n65_l0l}
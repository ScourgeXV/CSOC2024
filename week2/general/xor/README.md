###XOR Starter

Description - We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.
Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.

Solution script - starter.py

Flag - crypto{aloha}


###XOR Properties

Description - In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.
Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

Solution script - properties.py

Flag - crypto{x0r_i5_ass0c1at1v3}


###Favourite byte

Description - For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

Solution script - fav_byte.py

Flag - crypto{0x10_15_my_f4v0ur173_by7e}


###You either know, XOR you don't

Description - I've encrypted the flag with my secret key, you'll never be able to guess it.
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

Solution script - key.py
                  flag.py

Flag - crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}


###Lemur XOR 

Description - I've hidden two cool images by XOR with the same secret key so you can't see them!

File - lemur_ed66878c338e662d3473f0d98eedbd0d.png
       flag_7ae18c704272532658c10b5faad06d74.png

Solution script - lemur.py

Flag - crypto{X0Rly_n0t!}
       flag.png
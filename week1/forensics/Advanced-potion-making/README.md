Advanced-potion-making

Description - Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

File - advanced-potion-making

Solution - Upon opening th file in a hex editor we can see that its headers are similar to a png file. So we fix the headers of the file from '89 50 42 11 0D 0A 1A 0A 00 12 13 14' to '89 50 4E 47 0D 0A 1A 0A 00 00 00 0D'. After this we get an image which is completely red and does not have any flag. On converting it to black and white online we get the flag.

Flag - picoCTF{w1z4rdry}

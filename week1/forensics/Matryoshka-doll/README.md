Matryoshka doll

Description - Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? 

File - dolls.jpg

Solution - We are given an image dolls.jpg which on extracting using binwalk gives us a directory base images. Inside we have another image 2_c.jpgwhich on extracting using binwalk gives another image 3_c.jpg which again on extracting using binwalk gives another image 4_c.jpg which finally on extracting give us flag.txt having the flag.

Flag - picoCTF{4f11048e83ffc7d342a15bd2309b47de}

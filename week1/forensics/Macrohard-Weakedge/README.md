MacroHard WeakEdge

Description - I've hidden a flag in this file. Can you find it?

File - Forensics is fun.ppt

Solution - We are given a Microsoft Powerpoint which is blank on opening. After extracting the ppt using binwalk we get three directories. After looking through each directory and their sub-directories we find a suspecious file 'hidden' in the ppt directory. On decoding the text inside the file with base64 we get our flag. 

Flag - picoCTF{D1d_u_kn0w_ppts_r_z1p5}

tunn3l v1s10n

Description - We found this file. Recover the flag.

File - tunn3l_v1s10n

Solution - We are given a file of unknown type. After opening it in hex editor we get the headers as 42 4D which means it is a bmp bitmap file. But it could not open due errorneous headers. So the headers were changed from '42 4D 8E 26 2C 00 00 00 00 00 BA D0 00 00 BA D0' to '42 4D 8E 26 2C 00 00 00 00 00 36 00 00 00 28 00'. This gives us an image but it does not have any flag. After increasing the size of image using hex editor from '32 01' to '52 03' we get flag.

Flag - picoCTF{qu1t3_a_v13w_2020}

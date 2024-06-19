#!/usr/bin/env python3

e = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
flag = ''

for i in range(0,len(e),2) :
    flag += chr(int(e[i:i+2],16))

print(flag)

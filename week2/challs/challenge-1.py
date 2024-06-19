e = '43104f0c32017b48340179266203350636025f6b6e0a5f2730423f42'
s = ''
for i in range(0,len(e),4) :
    s += str(format(int(e[i:i+2], 16) ^ int(e[i:i+4], 16),'02x'))

print(s)

flag = ''
for i in range(0,len(s),2) :
    flag += chr(int(s[i:i+2],16))

print(flag)

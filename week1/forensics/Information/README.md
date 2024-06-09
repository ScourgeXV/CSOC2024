Information 

Description - Files can always be changed in a secret way. Can you find the flag?

File - cat.jpg

Solution - Using the exiftool on the given image we get some wierd sort of liscence - 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'. It is a base64 encoded string which on decoding gives us the flag.

Flag - picoCTF{the_m3tadata_1s_modified}

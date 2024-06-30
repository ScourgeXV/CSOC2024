# Java Script Kiddie

## Description 
The image link appears broken...

## Challenge link 
https://jupiter.challenges.picoctf.org/problem/17205

## Solution 
We are given a website which takes some text input. Upon looking at its source code it can be concluded that this text input is being used a key which converts a given set of bytes into a new set and assemble a PNG image from this new bytes data. It involves some sort of shifter which shifts each byte down a column in hex headers of image. We already know the first 16 bytes of PNG format is fixed. Using this we can recreate the key just entering the shift of first 16 bytes in the headers. This gives us 36 keys out of which this key 5108180345363640 when entered gives us a QR code. On scanning this code we get the flag.
![screenshot](screenshot1.png)

## Flag 
picoCTF{066cad9e69c5c7e5d2784185c0feb30b}


# Java Script Kiddie 2

## Description 
The image link appears broken... twice as badly...

## Challenge link 
https://jupiter.challenges.picoctf.org/problem/51400

## Solution 
We are given a website which takes some text input. Like previous challenge its source code is also assembling an image using the preset byte data and this input as a key. But this time every second element of the key is being used to shift the bytes. So we have to create the input just like previous challenge and add any character (I added 0) in between them to get the key. This gave us the key 60005030108010709050702060300090. On entering this key we get a QR code which gives us the flag.
![screenshot](screenshot2.png)

## Flag 
picoCTF{59d5db659865190a07120652e6c77f84}

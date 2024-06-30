# Who are you? 

## Description 
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn

## Challenge link 
http://mercury.picoctf.net:46199/

## Solution 
We are given a website which denies access because we are not from PicoBrowser. So we change the value of User-Agent to PicoBrowser. After this it blocks access because we are from another site. So we add a `Referer` header with value `http://mercury.picoctf.net`. After this it blocks access because site worked only in 2018. So we add `Date` header with value `Sat, 29 June 2018 08:49:37 GMT`. After this it blocks access because we can be tracked. So we added `DNT` header with value `1`. After this it blocks access because we are not in Sweden. So we added `X-forwarded-for` header with a value of IP address of Sweden `109.228.128.0`. After this it blocks access because our request language is not Swedish. So we add `Accept-Language` header with value `sv` which is the code for Swedish. After this we finally get the flag.

## Flag 
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_8d5d8d77}
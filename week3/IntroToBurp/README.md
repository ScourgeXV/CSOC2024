# IntroToBurp

## Description 
Try here to find the flag

## Challenge link 
http://titan.picoctf.net:57943/

## Solution  
We are given a website which asks us some fields like name, username, password etc. When we enter these values we get a page of 2fa authentication which asks us OTP. We can just change the value of request headers `Accept` and `Content-Type` to `application/json`. This gives us the flag. 

## Flag 
picoCTF{#0TP_Bypvss_SuCc3$S_9090d63c}
###Greatest Common Divisor

Description - 
The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b).
For a = 12, b = 8 we can calculate the divisors of a: {1,2,3,4,6,12} and the divisors of b: {1,2,4,8}. Comparing these two, we see that gcd(a,b) = 4.
Now imagine we take a = 11, b = 17. Both a and b are prime numbers. As a prime number has only itself and 1 as divisors, gcd(a,b) = 1.
We say that for any two integers a,b, if gcd(a,b) = 1 then a and b are coprime integers.
If a and b are prime, they are also coprime. If a is prime and b < a then a and b are coprime.
There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.
Try coding it up; it's only a couple of lines. Use a = 12, b = 8 to test it.
Now calculate gcd(a,b) for a = 66528, b = 52920 and enter it below.

Solution script - gcd.py

Flag - 1512


###Extended GCD 

Description - Let a and b be positive integers.
The extended Euclidean algorithm is an efficient way to find integers u,v such that
a * u + b * v = gcd(a,b)
Using the two primes p = 26513, q = 32321, find the integers u,v such that
p * u + q * v = gcd(p,q)
Enter whichever of u and v is the lower number as the flag.

Solution script - extd_gcd.py

Flag - -8404


###Modular Arithmatic 1

Description - Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a ≡ b mod m.
Another way of saying this, is that when we divide the integer a by m, the remainder is b. This tells you that if m divides a (this can be written as m | a) then a ≡ 0 mod m.
Calculate the following integers:
11 ≡ x mod 6
8146798528947 ≡ y mod 17
The solution is the smaller of the two integers.

Solution script - ma1.py

Flag - 4


###Modular Arithmatic 2 

Description - We'll pick up from the last challenge and imagine we've picked a modulus p, and we will restrict ourselves to the case when p is prime.
The integers modulo p define a field, denoted Fp.
A finite field Fp is the set of integers {0,1,...,p-1}, and under both addition and multiplication there is an inverse element b for every element a in the set, such that a + b = 0 and a * b = 1.
Lets say we pick p = 17. Calculate 317 mod 17. Now do the same but with 517 mod 17.
What would you expect to get for 716 mod 17? Try calculating that.
This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.
Now take the prime p = 65537. Calculate 27324678765465536 mod 65537.
Did you need a calculator?

Solution script - ma2.py

Flag - 1


###Modular Inverting

Description - As we've seen, we can work within a finite field Fp, adding and multiplying elements, and always obtain another element of the field.
For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p.
This is the multiplicative inverse of g.
Example: 7 * 8 = 56 ≡ 1 mod 11
What is the inverse element: 3 * d ≡ 1 mod 13?

Solution script - mi.py

Flag - 9
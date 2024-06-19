###RSA Starter 1

Description - 
All operations in RSA involve modular exponentiation.
Modular exponentiation is an operation that is used extensively in cryptography and is normally written like: 210 mod 17
You can think of this as raising some number to a certain power (210 = 1024), and then taking the remainder of the division by some other number (1024 mod 17 = 4). In Python there's a built-in operator for performing this operation: pow(base, exponent, modulus)
In RSA, modular exponentiation, together with the problem of prime factorisation, helps us to build a "trapdoor function". This is a function that is easy to compute in one direction, but hard to do in reverse unless you have the right information. It allows us to encrypt a message, and only the person with the key can perform the inverse operation to decrypt it.
Find the solution to 10117 mod 22663

Solution script - rsa1.py

Flag - 19906


###RSA Starter 2

Description - 
RSA encryption is modular exponentiation of a message with an exponent e and a modulus N which is normally a product of two primes: N = p * q.
Together the exponent and modulus form an RSA "public key" (N, e). The most common value for e is 0x10001 or 65537.
"Encrypt" the number 12 using the exponent e = 65537 and the primes p = 17 and q = 23. What number do you get as the ciphertext?

Solution script - rsa2.py

Flag - 301


###RSA Starter 3 

Description - 
RSA relies on the difficulty of the factorisation of the modulus N. If the primes can be found then we can calculate the Euler totient of N and thus decrypt the ciphertext.
Given N = p*q and two primes:
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
What is the totient of N?

Solution script - rsa3.py

Flag - 882564595536224140639625987657529300394956519977044270821168


###RSA Starter 4

Description -
The private key d is used to decrypt ciphertexts created with the corresponding public key (it's also used to "sign" a message but we'll get to that later).
The private key is the secret piece of information or "trapdoor" which allows us to quickly invert the encryption function. If RSA is implemented well, if you do not have the private key the fastest way to decrypt the ciphertext is to first factorise the modulus.
In RSA the private key is the modular multiplicative inverse of the exponent e modulo the totient of N.
Given the two primes:
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
and the exponent:
e = 65537

Solution script - rsa4.py

Flag - 121832886702415731577073962957377780195510499965398469843281


###RSA Starter 5

Description - 
I've encrypted a secret number for your eyes only using your public key parameters:
N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
Use the private key that you found for these parameters in the previous challenge to decrypt this ciphertext:
c = 77578995801157823671636298847186723593814843845525223303932

Solution script - rsa5.py

Flag - 13371337


###RSA Starter 6

Description - 
How can you ensure that the person receiving your message knows that you wrote it?
You've been asked out on a date, and you want to send a message telling them that you'd love to go, however a jealous lover isn't so happy about this.
When you send your message saying yes, your jealous lover intercepts the message and corrupts it so it now says no!
We can protect against these attacks by signing the message.
Imagine you write a message M. You encrypt this message with your friend's public key: C = Me0 mod N0.
To sign this message, you calculate the hash of the message: H(M) and "encrypt" this with your private key: S = H(M)d1 mod N1.
Your friend can decrypt the message using their private key: m = Cd0 mod N0. Using your public key they calculate s = Se1 mod N1.
Now by computing H(m) and comparing it to s: assert H(m) == s, they can ensure that the message you sent them, is the message that they received!
Sign the flag crypto{Immut4ble_m3ssag1ng} using your private key and the SHA256 hash function.

File - private_0a1880d1fffce9403686130a1f932b10.key

Solution script - rsa6.py

Flag - 13480738404590090803339831649238454376183189744970683129909766078877706583282422686710545217275797376709672358894231550335007974983458408620258478729775647818876610072903021235573923300070103666940534047644900475773318682585772698155617451477448441198150710420818995347235921111812068656782998168064960965451719491072569057636701190429760047193261886092862024118487826452766513533860734724124228305158914225250488399673645732882077575252662461860972889771112594906884441454355959482925283992539925713424132009768721389828848907099772040836383856524605008942907083490383109757406940540866978237471686296661685839083475
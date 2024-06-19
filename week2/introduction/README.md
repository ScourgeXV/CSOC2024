###Great Snakes 

Description - 
Modern cryptography involves code, and code involves coding. CryptoHack provides a good opportunity to sharpen your skills.
Of all modern programming languages, Python 3 stands out as ideal for quickly writing cryptographic scripts and attacks. For more information about why we think Python is so great for this, please see the FAQ.
Run the attached Python script and it will output your flag.

Challenge Script - great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py

Solution -  Just run the script

Flag - crypto{z3n_0f_pyth0n}


###Network Attacks 

Description - 
Several of the challenges are dynamic and require you to talk to our challenge servers over the network. This allows you to perform man-in-the-middle attacks on people trying to communicate, or directly attack a vulnerable service. To keep things consistent, our interactive servers always send and receive JSON objects.
Such network communication can be made easy in Python with the pwntools module. This is not part of the Python standard library, so needs to be installed with pip using the command line pip install pwntools.
For this challenge, connect to socket.cryptohack.org on port 11112. Send a JSON object with the key buy and value flag

Solution - We are given a challenge script. We just need to change the value of 'buy' key from 'clothes' to 'flag' in the json send request.

Solution Script - pwntools_example_72a60ff13df200692898bb14a316ee0b.py

Flag - crypto{sh0pp1ng_f0r_fl4g5}
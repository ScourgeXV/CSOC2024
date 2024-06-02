Bandit0 --> Bandit1

command - ssh bandit0@bandit.labs.overthewire.org -p 2220
	  cat readme

password - NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL


Bandit1 --> Bandit2

command - ssh bandit1@bandit.labs.overthewire.org -p 2220
	  cat < -

password - rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi


Bandit2 --> Bandit3

command - ssh bandit2@bandit.labs.overthewire.org -p 2220
	  cat 'spaces in this filename'

password - aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG


Bandit3 --> Bandit4

command - ssh bandit3@bandit.labs.overthewire.org -p 2220
	  cd inhere
	  cat .hidden

passowrd - 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe


Bandit4 --> Bandit5

description - The only human readable file in the directory in -file07. Therefore our password is in this file.

command - ssh bandit4@bandit.labs.overthewire.org -p 2220
	  cd inhere
	  cat < -file07

password - lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR


Bandit5 --> Bandit6

description - We will use find command to find the file of size given in the challenge. this file has our password. 

command - ssh bandit5@bandit.labs.overthewire.org -p 2220
	  find -size 1033c
	  cat < .file2

password - P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU


Bandit6 --> Bandit7

description - 

command - ssh bandit6@bandit.labs.overthewire.org -p 2220
	  cd /
	  find -user bandit7 -size 33c
	  cat < ./var/lib/dpkg/info/bandit7.password

password - z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S


Bandit7 --> Bandit8

command - ssh bandit7@bandit.labs.overthewire.org -p 2220
	  cat data.txt | grep millionth

password - TESKZC0XvTetK0S9xNwm25STk5iWrBvP


Bandit8 --> Bandit9

description - We need to look out for the line which occurs only once. Therefore we first sort it then we use uniq command to get the count of each line. In the end we get the line which has occured only once.

command - ssh bandit8@bandit.labs.overthewire.org -p 2220
	  sort data.txt | uniq -c

password - EN632PlfYiZbn3PhVK3XOGSlNInNE00t


Bandit9 --> Bandit10

command - ssh bandit9@bandit.labs.overthewire.org -p 2220
	  strings data.txt | grep ===

password - G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s


Bandit10 --> Bandit11

command - ssh bandit10@bandit.labs.overthewire.org -p 2220
	  base64 -d data.txt

password - 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM


Bandit11 --> Bandit12

description - To perform rotation 13 we have just translated each letter of the file to their correspondingly thirteenth letter. This is done using tr command.

command - ssh bandit11@bandit.labs.overthewire.org -p 2220
	  cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'

password - JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


Bandit12 --> Bandit13

description - 

command - ssh bandit12@bandit.labs.overthewire.org -p 2220
	  mktemp -d
	  cp data.txt /tmp/tmp.ZsC4HgapPd
	  cd /tmp/tmp.ZsC4HgapPd
	  xxd -r data.txt data1
	  file data1
	  mv data1 data1.gz
	  gzip -d data1.gz
	  file data1
	  mv data1 data1.bz2
	  bzip2 -d data1.bz2
	  file data1
	  mv data1 data1.gz
	  gzip -d data1.gz
	  file data1
	  mv data1 data1.tar
	  tar -xf data1.tar
	  file data5.bin
	  mv data5.bin data5.tar
	  tar -xf data5.tar
	  file data6.bin
	  mv data6.bin data6.bz2
	  bzip2 -d data6.bz2
	  file data6
	  mv data6 data6.tar
	  tar -xf data6.tar
	  mv data8.bin data8.gz
	  gzip -d data8.gz
	  file data8
	  cat data8

password - wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw


Bandit13 --> Bandit14

command - ssh bandit13@bandit.labs.overthewire.org -p 2220
	  ssh bandit14@bandit.labs.overthewire.org -p 2220 -i sshkey.private
	  cat /etc/bandit_pass/bandit14

password - fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq


Bandit14 --> Bandit15

command - nc localhost 30000

password - jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt


Bandit15 --> Bandit16

command - ssh bandit15@bandit.labs.overthewire.org -p 2220
	  cat /etc/bandit_pass/bandit15
	  ncat --ssl localhost 30001

password - JQttfApK4SeyHwDlI9SXGR50qclOAil1


Bandit16 --> Bandit17

command - nmap localhost -p 31000-32000
	  nmap -A localhost -p 31046,31518,31691,31790,31960
	  ncat --ssl localhost 31790
	  vim key
	  chmod 400 key
	  ssh -i key bandit17@bandit.labs.overthewire.org -p 2220

password - It is a private RSA key (As such no password)


Bandit17 --> Bandit18

command - diff passwords.old passwords.new

password - hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg


Bandit18 --> Bandit19

command - ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh
	  cat readme

password - awhqfNnAbc1naukrpqDYcF95h7HoMTrC


Bandit19 --> Bandit20

command - ssh bandit19@bandit.labs.overthewire.org -p 2220
	  ./bandit20-do cat /etc/bandit_pass/bandit20

password - VxCazJaVykI6W36BkBU0mJTCM8rR95XT


Bandit20 --> Bandit21

command - ssh bandit20@bandit.labs.overthewire.org -p 2220
	  nc -lvp 1234
	  ./suconnect 1234
	  VxCazJaVykI6W36BkBU0mJTCM8rR95XT (enter above password)

password - NvEJF7oVjkddltPSrdKEFOllh9V1IBcq


Bandit21 --> Bandit22

command - ssh bandit21@bandit.labs.overthewire.org -p 2220
	  ls /etc/cron.d/
	  cat /etc/cron.d/cronjob_bandit22
	  cat /usr/bin/cronjob_bandit22.sh
	  cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

password - WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff


Bandit22 --> Bandit23

command - ssh bandit22@bandit.labs.overthewire.org -p 2220
	  ls /etc/cron.d/
	  cat /etc/cron.d/cronjob_bandit23
	  cat /usr/bin/cronjob_bandit23.sh
	  echo I am user bandit23 | md5sum | cut -d ' ' -f 1
	  cat /tmp/8ca319486bfbbc3663ea0fbe81326349

password - QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G


Bandit23 --> Bandit24

script - #!/bin/bash

	 cat /etc/bandit_pass/bandit24 > /tmp/saat/password 

command - ssh bandit23@bandit.labs.overthewire.org -p 2220
	  cat /etc/cron.d/cronjob_bandit24
	  cat /usr/bin/cronjob_bandit24.sh
	  mkdir /tmp/saat
	  cd /tmp/saat
	  vim script
	  mv script script.sh
	  touch password
	  chmod 777 script.sh
	  chmod 777 password
	  cp script.sh cd /var/spool/bandit24/foo
	  cat password

password - VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar


Bandit24 --> Bandit25

script - #!/bin/bash

	 for pin in {0000..9999} ;
	 do
        	 echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $pin"
	 done | nc localhost 30002

command - ssh bandit24@bandit.labs.overthewire.org -p 2220
	  mkdir /tmp/saat2
	  cd /tmp/saat2
	  vim script25.sh
	  chmod 777 script25.sh
	  ./script25.sh

password - p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d


Bandit25 --> Bandit26

command - cat /etc/passwd
	  cat /usr/bin/showtext
	  ssh -i bandit26.sshkey bandit25@localhost -p 2220
	  (increase th size of text big enough to distort bandit26 ASCII art)
	  vi
	  :set shell?
	  :set shell=/bin/bash/
	  :shell
	  cat /etc/bandit_pass/bandit26

password - c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1


Bandit26 --> Bandit27

command - ./bandit27-do cat /etc/bandit_pass/bandit27

password - YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS


Bandit27 --> Bandit28

command - ssh bandit27@bandit.labs.overthewire.org -p 2220
	  mkdir /tmp/saat3
	  cd /tmp/saat3
	  git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
	  cd repo
	  ls
	  cat README

password - AVanL161y9rsbcJIsFHuw35rjaOM19nR


Bandit28 --> Bandit29

command - ssh bandit28@bandit.labs.overthewire.org -p 2220
	  mkdir /tmp/saat4
	  cd /tmp/saat4
	  git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
	  cd repo
	  git log
	  git checkout f08b9cc63fa1a4602fb065257633c2dae6e5651b
	  cat README.md

password - tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S


Bandit29 --> Bandit30

command - ssh bandit29@bandit.labs.overthewire.org -p 2220
	  mkdir /tmp/saat5
	  cd /tmp/saat5
	  git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
	  cd repo
	  git checkout dev
	  git log
	  cat README.md

password - xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS


Bandit30 --> Bandit31

command - ssh bandit30@bandit.labs.overthewire.org -p 2220
	  mkdir /tmp/saat6
          cd /tmp/saat6
          git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
          cd repo
          git tag
          git show secret

password - OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt


Bandit31 --> Bandit32

command - ssh bandit30@bandit.labs.overthewire.org -p 2220
	  mkdir /tmp/saat7
    	  cd /tmp/saat7
    	  git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
    	  cd repo
    	  cat README.md
    	  cat .gitignore
    	  rm .gitignore
   	  echo 'May I come in?' > key.txt
   	  git add key.txt
   	  git commit -m "key added"
   	  git push

password - rmCBvG56y58BXzv98yZGdO7ATVL5dW8y


Bandit32 --> Bandit33

command - ssh bandit32@bandit.labs.overthewire.org -p 2220
	  $SHELL
	  $0
	  export SHELL=/bin/bash
	  $SHELL
	  cat /etc/bandit_pass/bandit33

password - odHo63fHiFqcWWJG9rLiLDtPm45KzUKy


Bandit33 --> Bandit34

command - ssh bandit33@bandit.labs.overthewire.org -p 2220
	  cat README.txt

text - 

Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know! 
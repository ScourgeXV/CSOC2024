File types 

Description - This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

File - Flag.pdf

Solution - We are given a .pdf file which is not opening. file command tells us that it is a shell script having a shell archive. on running the shell script we get a file 'flag' which is ar compressed file. On decompressing we get a  cpio compressed file. Again on decommpressing we get bzip2 commpressed file wchich gives us a gzip commpressed file which gives us an lzip compressed file which gives us an LZ4 compressed file which gives us an LZMA compressed file which gives us an lzop compessed file which gives us anagin an lzip compressed file which gives us an XZ compressed file which on decompressing finally gives us a text file having some hexadecimal text. this hexadecimal in ascii gives us the flag. Command involved are - 

	mv Flag.pdf flag.sh
	./flag.sh
	file flag
	ar -x flag
	mv flag flag.cpio
	cpio -iv < flag.cpio
	mv flag flag.bz2
	bzip2 -d flag.bz2
	mv flag flag.gz
	gzip -d flag.gz
	mv flag flag.lz
	lzip -d flag.lz
	mv flag flag.lz4
	lz4 -d flag.lz4 flag
	mv flag flag.xz
	lzma -d flag.xz
	mv flag flag.suf
	lzop -S suf -d flag.suf
	mv flag flag.lz
	lzip -d flag.lz
	mv flag flag.xz
	xz -d flag.xz
	cat flag 

Flag - picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}

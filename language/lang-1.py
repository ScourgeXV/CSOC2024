'''
This is Song-Lang which is mostly based on bollywood
songs. It is based on python and contains very few 
basic and simple commands as of now as it is still
at developing stage.
'''

__author__ = "Saatvic Sehgal"


def bol_do_na_zara(x) :
    '''
    Used as print command to display output
    '''
    print(x)

def sun_raha_hai_na(x) :
    '''
    Used as input command to take user input
    '''
    input(x)

def main_agar_kahoon(cond,command) :
    '''
    Used as if conditional
    '''
    if cond :
        command

def phir_bhi(cond,command) :
    '''
    Used as else conditional
    '''
    if not cond :
        command

def jab_tak(cond,command) :
    '''
    Used as while loop
    '''
    while cond :
        command

def such_keh_raha(cond) :
    '''
    Used as bool True
    '''
    if cond == True :
        return 1
    else :
        return 0

def jhootha_hai(cond) :
    '''
    Used as bool False
    '''
    return not sach(cond)

def yun_hi_chala_chal() :
    '''
    Used as continue command
    '''
    continue

def ruk_jana() :
    '''
    Used as break command
    '''
    break

def tu_hai_wahan(a,b) :
    '''
    Used as in command
    '''
    c = a in b
    return c

def aur(a,b) :
    '''
    Used as and logical operateor between two arguments only
    '''
    c = a and b
    return c

def ya(a,b) :
    '''
    Used as or logical operator between two arguments only
    '''
    c = a or b
    return c

def nahi(x) :
    '''
    Used as not logical operator
    '''
    return not x


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:56:01 2021

@author: bing
"""

import random
import string



def caesarEncrypt(message, codebook, shift):
    '''
    - you can compute the index of a character, or,
    - you can convert the codebook into a dictionary
    '''
    codebook_dic_en={}
    encrypted = ""
    for i in range(len(codebook)):
        before_shift=codebook[i]
        after_shift=codebook[(i+shift)%52]
        codebook_dic_en[before_shift]=after_shift
    
    for m in message:
        try:
            encrypted+=codebook_dic_en[m]
        except:
            encrypted+=m
    return encrypted


def caesarDecrypt(message, codebook, shift):
    decrypted = ""
    codebook_dic_de={}
    for i in range(len(codebook)):
        before_shift=codebook[i]
        after_shift=codebook[(i+shift)%52]
        codebook_dic_de[after_shift]=before_shift
    
    for m in message:
        try:
            decrypted+=codebook_dic_de[m]
        except:
            decrypted+=m
    return decrypted


if __name__ == "__main__":
    ##The following several lines generate the codebook
    ##Please don't change it
    random.seed("Caesar")
    
    codebook = []
    for e in string.ascii_letters:
        codebook.append(e)
        
    random.shuffle(codebook)
    print("Your codebook:")
    print(codebook)
    ## end of the codebook generation
    
    m = "Hello Kitty!"
    shift = 3
    encoded = caesarEncrypt(m, codebook, shift)
    decoded = caesarDecrypt(encoded, codebook, shift)
    print("Origin:", m)
    print("Encoded:", encoded)
    print("Decoded", decoded)
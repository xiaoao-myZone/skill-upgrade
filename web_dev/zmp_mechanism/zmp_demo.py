#-*- coding: utf-8 -*-

import random, threading, time, zmp
B = 32

# TOOD random.getrandbits lstrip
# lstrip = leading strip
def ones_and_zeros(digits):
    return bin(random.getrandbits(digits).lstrip("0b")).zfill(digits)

def bitsource(zcontext, url):
    zsock = zcontext.socket(zmp.PUB)
    zsock.bind(url)
    while True:
        zsock.send_string(ones_and_zeros(B * 2))
        time.sleep(0.1)
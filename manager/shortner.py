from math import floor
import string

base = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def base62(num, bs):
    if bs <= 0 or bs > 62:
        return 0    
    rem = num % bs
    res = base[rem];
    qou = floor(num / bs)
    while qou:
        rem = qou % bs
        qou = floor(qou / bs)
        res = base[int(rem)] + res
    return res

def base10(num, bs = 62):
    res = 0
    for i in range(len(num)):
        res = bs * res + base.find(num[i])
    return res
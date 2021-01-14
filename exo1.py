#!/bin/env python3

import hashlib

mdp = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

f = open('./phpbb.txt', 'r')
arr = f.read().split('\n')

for i in arr:
    h = hashlib.sha256(i.encode('utf-8')).hexdigest()
    if (h == mdp):
        print(i)
#!/usr/bin/env python3

import sys
from GT2S import GT2S

gt2s = GT2S(save_path="./")
counter = 1

print("Using \"quit\" or ctrl+c to exit!")
print("Input: ",end='', flush=True)
for line in sys.stdin:
    if line.rstrip() == "quit":
        break
    elif len(line.rstrip()) > 0:
        gt2s.text2speechfile(line.rstrip(), str(counter)+".mp3", speed=1.2)
        counter += 1
    print("Input: ",end='', flush=True)

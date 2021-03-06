#!/usr/bin/python
import sys

def solve(N):
    if N < 0:
        return "Negative numbers not supported"
    elif N == 0:
        return "1/2"
    result = ""
    while N != 1:
        if N == 10:
            result = "*3*3*3*3/2/2/2" + result
            N /= 10
        elif N % 3 == 0:
            result = "*3" + result
            N /= 3
        else:
            result = "/2" + result
            N = N*2+2-N%3
    return "1" + result

if __name__ == "__main__":
    print solve(int(sys.argv[1]))

"""
Usage:

  python wpc40.py <number>

Examples:

$ python wpc40.py 1
1

$ python wpc40.py 8
1*3*3*3*3/2/2/2/2*3*3/2/2*3/2/2

$ python wpc40.py 100
1*3*3*3*3/2/2/2/2*3*3*3/2*3/2

$ python wpc40.py 100000000000000000
1*3*3*3/2*3/2*3*3/2*3/2*3/2/2*3/2/2*3*3*3/2/2*3/2/2*3/2/2*3*3*3*3/2/2*3/2/2*3*3/2/2*3*3*3*3*3/2/2*3/2*3/2*3/2*3/2/2*3/2*3/2*3/2*3/2/2*3*3*3/2/2*3*3/2/2*3*3/2*3/2*3/2*3/2/2*3/2/2*3*3/2/2*3/2*3/2/2*3/2*3/2*3/2/2*3/2*3*3/2*3*3/2/2*3/2/2*3*3/2/2*3*3/2*3/2/2*3/2/2*3/2*3/2*3*3/2*3/2/2*3*3/2*3/2*3*3*3/2/2*3*3*3/2*3/2/2*3/2/2*3/2/2*3/2/2*3/2*3/2/2*3/2/2*3*3/2/2*3/2/2*3/2/2*3*3*3/2*3/2/2*3*3/2/2*3/2*3/2*3/2/2*3/2*3/2*3/2/2*3*3/2/2*3/2/2*3*3/2*3/2
"""

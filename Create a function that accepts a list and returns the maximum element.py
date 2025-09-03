
import sys

def list_maxm(list):
    maxm = -(sys.maxsize-1)

    for i in list:
        if maxm<i:
            maxm=i

    return maxm

list = [122,12,42,3,1,6,789,1000,112]
print(list_maxm(list))

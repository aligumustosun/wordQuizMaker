import csv
import sys
import linecache
import os
from random import randint
import random

aradakifark=3

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num-1] = text
    out = open(file_name, 'w')
   # print("it is replaced")
    out.writelines(lines)
    out.close()
#satir sayisini döndürür.
def read_line(file_name,line_num):
    lines=open(file_name, 'r').readlines()
    return lines[line_num-1]
def satirSayisi(adres):
    lines=open(adres, 'r').readlines()
    return len(lines)


i=1
while (i<satirSayisi('kelimeler.txt')+1):
    a,b,c,d = read_line('kelimeler.txt',i).split(',')
    replace_line('kelimeler.txt',i,a+","+b+",0,"+str(int((aradakifark)*-1))+"\n")
    print(i)
    i+=1
    

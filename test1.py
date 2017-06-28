import csv
import sys
import linecache
import os
from random import randint
import random
#satir sayisini döndürür.
def satirSayisi(adres):
    lines=open(adres, 'r').readlines()
    return len(lines)
#asil soru sorma işlemi burada gerçekleşir.
def soruSor():
    lines=open('kelimeler.txt','r').readlines() 
    x=int(satirSayisi('kelimeler.txt'))
    my_list = [None] * 4
    sayac=0
    while(sayac<4):
        my_list[sayac]= random.randint(1,satirSayisi('kelimeler.txt') )
        sayac=sayac+1
        if(sayac is 4):
            if(my_list[0] is my_list[1] or my_list[0] is my_list[2] or my_list[0] is my_list[3] or my_list[1] is my_list[2] or my_list[1] is my_list[3] or my_list[2] is my_list[3] ):
                sayac=0    
    with open('kelimeler.txt','r') as f:
        icerik=f.readlines()
        icerik=[x.strip() for x in icerik]        
    s1,c1,y1=icerik[(my_list[0]-1)].split(',')
    i1=my_list[0]-1
    s2,c2,y2=icerik[(my_list[1]-1)].split(',')
    i2=my_list[1]-1
    s3,c3,y3=icerik[(my_list[2]-1)].split(',')
    i3=my_list[2]-1
    s4,c4,y4=icerik[(my_list[3]-1)].split(',')
    i4=my_list[3]-1
    answers= [c1,c2,c3,c4]
    rastgele=random.randint(1,4)
    if(rastgele%4==0):
      print(s1,' ? ')
      print('\n\nA - ',c1)
      print('\n\nB - ',c2)
      print('\n\nC - ',c3)
      print('\n\nD - ',c4)
      answer = input()
      if(answer=='A' or answer =='a'):
        print('true')
      else:
        print('false')
    elif(rastgele%4==1):
      print(s1,' ? ')
      print('\n\nA - ',c2)
      print('\n\nB - ',c1)
      print('\n\nC - ',c3)
      print('\n\nD - ',c4)
      answer = input()
      if(answer=='B' or answer =='b'):
        print('true')
      else:
        print('false')
    elif(rastgele%4==2):
      print(s1,' ? ')
      print('\n\nA - ',c2)
      print('\n\nB - ',c3)
      print('\n\nC - ',c1)
      print('\n\nD - ',c4)
      answer = input()
      if(answer=='C' or answer =='c'):
        print('true')
      else:
        print('false')     
    elif(rastgele%4==1):
      print(s1,' ? ')
      print('\n\nA - ',c2)
      print('\n\nB - ',c4)
      print('\n\nC - ',c3)
      print('\n\nD - ',c1)
      answer = input()
      if(answer=='D' or answer =='d'):
        print('true')
      else:
        print('false')

while(1):
    soruSor()
    

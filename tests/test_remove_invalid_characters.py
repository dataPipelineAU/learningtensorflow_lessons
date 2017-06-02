#!python3
#coding: utf8
symbols = '.'
D = str.maketrans('','',symbols)
with open('All12.txt','a',encoding='utf8') as t, open('All11.txt','r',encoding='utf8') as n:
    for line in n:
        t.write(line.translate(D))

#!python3
#coding: utf8
symbols = '.'
D = str.maketrans('','',symbols)
with open('test_3D_one.py','a',encoding='utf8') as t, open('test_3D_one.py','r',encoding='utf8') as n:
    for line in n:
        t.write(line.translate(D))

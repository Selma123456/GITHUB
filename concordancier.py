#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:22:03 2019

@author: prof
"""

'''
programme qui :
    0. lit un fichier texte contenant la liste des mots clés (un mot par ligne)
    et construit une expression reguliere
    1. lit un fichier texte (format tsv)
    2. recherche dans le texte de chaque ligne une expression reguliere
    3. et affiche l'expression recherchee, 50 caractères à gauche et à droite et l'url
'''


import re
import sys

print(sys.argv[1])
exit()


def lire_liste(fn):
    '''lit un fichier contenant des mots et transforme en expression reguliere'''
    er = '('
    f = open(fn, mode="r",encoding="utf8")
    for line in f:
        er = er + line.strip() + '|'
        #print(line.strip())
    er = er.strip('|') + ')'
    return er

keyword = '(' + sys.argv[1] + ')'
ctx_g = sys.argv[2]
ctx_d = sys.argv[3]


# 1. lecture du fichier texte

f = open("lemonde.tsv", mode="r",encoding="utf8")
for line in f:
    res = re.split("\t",line)
    match = re.search('(.{0,' + ctx_g +'})'+ keyword + '(.{0,' + ctx_d +'})',line,re.I)
    if match:
        print(match.group(1) + "\t"+ match.group(2) + "\t" + match.group(3))
    print(res[1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
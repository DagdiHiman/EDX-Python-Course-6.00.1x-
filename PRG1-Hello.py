# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 22:50:48 2017
@author: dagdi
"""
s="himanshu dagdi rakesh"
print(len(s))
count=0
for l in s:
        if (l=='a' or l=='e' or l=='i' or l=='o' or l=='u'):
           count+=1
print("Number of vowels: " + str(count))


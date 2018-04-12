__author__ = 'zhaoruowei'
#! /usr/env python
#-*-coding:utf-8-*-

#######################################################
####       count TCGA data(get information)        ####
#######################################################

import os
import re

project = "/Users/zhaoruowei/tmp/TCGA-information/"

software = "/Users/zhaoruowei/tmp/TCGA-information/Download_data_script/"

RNAseq = 'Gene_Expression_Quantification/'

downloads = 'rawdata/'
clean = 'clean/'
analysis = 'analysis/'

json_file = raw_input('json file name:\n') + '.json'

os.chdir(software)

json = open(json_file)
json_lines = json.read()
age_key = r'"age_at_diagnosis": (.*),'
birth_key = r'"year_of_birth": (.*),'
age_list = re.findall(re.compile(age_key),json_lines)
birth_list = re.findall(re.compile(birth_key),json_lines)
print age_list
print len(age_list)
print birth_list
print len(birth_list),'\n'

for y in age_list:
    if y == 'null':
        age_list.remove(y)
print 'no null numbers:',len(age_list),'\n'

age_list = map(float,age_list)

print 'min:',min(age_list),'\t',min(age_list)/365,'\n','max:',max(age_list),'\t',max(age_list)/365,'\n'

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []

for x in age_list:
    if x >= 0 and x <= 3650.0:
        a.append(x)
    elif x >= 3651.0 and x <= 7300.0:
        b.append(x)
    elif x >= 7301.0 and x <= 10950.0:
        c.append(x)
    elif x >= 10951.0 and x <= 14600.0:
        d.append(x)
    elif x >= 14601.0 and x <= 18250.0:
        e.append(x)
    elif x >= 18251.0 and x <= 21900.0:
        f.append(x)
    elif x >= 21901.0 and x <= 25550.0:
        g.append(x)
    elif x >= 25551.0 and x <= 29200.0:
        h.append(x)
    elif x >= 29201.0 and x <= 32850.0:
        i.append(x)
    elif x >= 32851.0:
        j.append(x)
print '1-10:\t',len(a)
print '11-20:\t',len(b)
print '21-30:\t',len(c)
print '31-40:\t',len(d)
print '41-50:\t',len(e)
print '51-60:\t',len(f)
print '61-70:\t',len(g)
print '71-80:\t',len(h)
print '81-90:\t',len(i)
print '90+:\t',len(j)

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

manifest = raw_input('Manifest file name:\n') + '.txt'
json_file = raw_input('json file name:\n') + '.json'

os.chdir(software)

file_namelist = []
counts_file = open(manifest)
mani_lines = counts_file.readlines()
counts_file_number = len(mani_lines) - 1
print "counts_file_number =", counts_file_number
for line in mani_lines:
    file_namelist.append(line.split("\t",4)[1])
del(file_namelist[0])
print "file_namelist:\t" , file_namelist

json = open(json_file)
json_lines = json.read()
submitter_id_key = r'"entity_submitter_id": "(.*)",'
stage_name_key = r'"tumor_stage": "(.*)",'
tcga_name = re.findall(re.compile(submitter_id_key),json_lines)
stage_name = re.findall(re.compile(stage_name_key),json_lines)
print tcga_name
print len(tcga_name)
print stage_name
print len(stage_name)

stage0 = []
stagei = []
stageia = []
stageib = []
stageii = []
stageiia =[]
stageiib = []
stageiic = []
stageiii = []
stageiiia = []
stageiiib = []
stageiiic = []
stageiv = []
stageiva = []
stageivb = []
stageivc = []
stageis = []
stagex = []
stagei_ii_nos = []
not_reported = []

#target
target_stage4 = []
target_stage2b= []
target_stage4s= []
target_stage3 = []
target_i = []
target_ii = []
target_iii = []
target_iiib = []
target_iii_iv = []
target_iiib_v = []
target_iv = []
target_iv_v = []

x = 0

#target
if "stage 2b" not in stage_name:
    print "stage 2b is NA\n"
if "stage 3" not in stage_name:
    print "stage 3 is NA\n"
if "stage 4" not in stage_name:
    print "stage 4 is NA\n"
if "stage 4s" not in stage_name:
    print "stage 4s is NA\n"

if "i" not in stage_name:
    print "i is NA\n"
if "ii" not in stage_name:
    print "ii is NA\n"
if "iii" not in stage_name:
    print "iii is NA\n"
if "iiib" not in stage_name:
    print "iiib is NA\n"
if "iii/iv" not in stage_name:
    print "iii_iv is NA\n"
if "iiib/v" not in stage_name:
    print "iiib/v is NA\n"
if "iv" not in stage_name:
    print "iv is NA\n"
if "iv/v" not in stage_name:
    print "iv/v is NA\n"

#tcga
if "stage 0" not in stage_name:
    print "stage 0 is NA\n"
if "stage i" not in stage_name:
    print "stage i is NA\n"
if "stage ia" not in stage_name:
    print "stage ia is NA\n"
if "stage ib" not in stage_name:
    print "stage ib is NA\n"
if "stage ii" not in stage_name:
    print "stage ii is NA\n"
if "stage iia" not in stage_name:
    print "stage iia is NA\n"
if "stage iib" not in stage_name:
    print "stage iib is NA\n"
if "stage iic" not in stage_name:
    print "stage iic is NA\n"
if "stage iii" not in stage_name:
    print "stage iii is NA\n"
if "stage iiia" not in stage_name:
    print "stage iiia is NA\n"
if "stage iiib" not in stage_name:
    print "stage iiib is NA\n"
if "stage iiic" not in stage_name:
    print "stage iiic is NA\n"
if "stage iv" not in stage_name:
    print "stage iv is NA\n"
if "stage iva" not in stage_name:
    print "stage iva is NA\n"
if "stage ivb" not in stage_name:
    print "stage ivb is NA\n"
if "stage ivc" not in stage_name:
    print "stage ivc is NA\n"
if "is" not in stage_name:
    print "is is NA\n"
if "stage x" not in stage_name:
    print "stage x is NA\n"
if "i/ii nos" not in stage_name:
    print "i/ii nos is NA\n"
if "not reported" not in stage_name:
    print "not reported is NA\n"

for i in stage_name:
    if i == "stage 0":
        stage0.append(tcga_name[x])
    elif i == "stage i":
        stagei.append(tcga_name[x])
    elif i == "stage ia":
        stageia.append(tcga_name[x])
    elif i == "stage ib":
        stageib.append(tcga_name[x])
    elif i == "stage ii":
        stageii.append(tcga_name[x])
    elif i == "stage iia":
        stageiia.append(tcga_name[x])
    elif i == "stage iib":
        stageiib.append(tcga_name[x])
    elif i == "stage iic":
        stageiic.append(tcga_name[x])
    elif i == "stage iii":
        stageiii.append(tcga_name[x])
    elif i == "stage iiia":
        stageiiia.append(tcga_name[x])
    elif i == "stage iiib":
        stageiiib.append(tcga_name[x])
    elif i == "stage iiic":
        stageiiic.append(tcga_name[x])
    elif i == "stage iv":
        stageiv.append(tcga_name[x])
    elif i == "stage iva":
        stageiva.append(tcga_name[x])
    elif i == "stage ivb":
        stageivb.append(tcga_name[x])
    elif i == "stage ivc":
        stageivc.append(tcga_name[x])
    elif i == "is":
        stageis.append(tcga_name[x])
    elif i == "stage x":
        stagex.append(tcga_name[x])
    elif i == "i/ii nos":
        stagei_ii_nos.append(tcga_name[x])
    #target
    elif i == "stage 2b":
        target_stage2b.append(tcga_name[x])
    elif i == "stage 3":
        target_stage3.append(tcga_name[x])
    elif i == "stage 4":
        target_stage4.append(tcga_name[x])
    elif i == "stage 4s":
        target_stage4s.append(tcga_name[x])

    elif i == "i":
        target_i.append(tcga_name[x])
    elif i == "ii":
        target_ii.append(tcga_name[x])
    elif i == "iii":
        target_iii.append(tcga_name[x])
    elif i == "iiib":
        target_iiib.append(tcga_name[x])
    elif i == "iii/iv":
        target_iii_iv.append(tcga_name[x])
    elif i == "iiib/v":
        target_iiib_v.append(tcga_name[x])
    elif i == "iv":
        target_iv.append(tcga_name[x])
    elif i == "iv/v":
        target_iv_v.append(tcga_name[x])

    else:
        not_reported.append(tcga_name[x])
        print i

    x = x +1

print 'stage0:\n' , len(stage0)
print 'stagei:\n' , len(stagei)
print 'stageia:\n' , len(stageia)
print 'stageib:\n' , len(stageib)
print 'stageii:\n' , len(stageii)
print 'stageiia:\n' , len(stageiia)
print 'stageiib:\n' , len(stageiib)
print 'stageiic:\n' , len(stageiic)
print 'stageiii:\n' , len(stageiii)
print 'stageiiia:\n' , len(stageiiia)
print 'stageiiib:\n' , len(stageiiib)
print 'stageiiic:\n' , len(stageiiic)
print 'stageiv:\n' , len(stageiv)
print 'stageiva:\n' , len(stageiva)
print 'stageivb:\n' , len(stageivb)
print 'stageivc:\n' , len(stageivc)
print 'is:\n' , len(stageis)
print 'stagex:\n' , len(stagex)
print 'i/ii nos\n' , len(stagei_ii_nos)
print 'not_reported:\n' , len(not_reported) , '\n'

#target
print 'stage2b:\n' , len(target_stage2b)
print 'stage3:\n' , len(target_stage3)
print 'stage4:\n' , len(target_stage4)
print 'stage4s:\n' , len(target_stage4s)
print 'i:\n' , len(target_i)
print 'ii:\n' , len(target_ii)
print 'iii:\n' , len(target_iii)
print 'iiib:\n' , len(target_iiib)
print 'iii/iv:\n' , len(target_iii_iv)
print 'iiib/v:\n' , len(target_iiib_v)
print 'iv:\n' , len(target_iv)
print 'iv/v:\n' , len(target_iv_v)

for m in xrange(0,32):
    if m == 0 :
        stage_list = stage0
        print 'stage0'
    elif m == 1 :
        stage_list = stagei
        print 'stagei'
    elif m == 2:
        stage_list = stageia
        print 'stageia'
    elif m == 3:
        stage_list = stageib
        print 'stageib'
    elif m == 4:
        stage_list = stageii
        print 'stageii'
    elif m == 5:
        stage_list = stageiia
        print 'stageiia'
    elif m == 6:
        stage_list = stageiib
        print 'stageiib'
    elif m == 7:
        stage_list = stageiic
        print 'stageiic'
    elif m == 8:
        stage_list = stageiii
        print 'stageiii'
    elif m == 9:
        stage_list = stageiiia
        print 'stageiiia'
    elif m == 10:
        stage_list = stageiiib
        print 'stageiiib'
    elif m == 11:
        stage_list = stageiiic
        print 'stageiiic'
    elif m == 12:
        stage_list = stageiv
        print 'stageiv'
    elif m == 13:
        stage_list = stageiva
        print 'stageiva'
    elif m == 14:
        stage_list = stageivb
        print 'stageivb'
    elif m == 15:
        stage_list = stageivc
        print 'stageivc'
    elif m == 16:
        stage_list = stageis
        print 'is'
    elif m == 17 :
        stage_list = stagex
        print 'stagex'
    elif m == 18:
        stage_list = stagei_ii_nos
        print 'i/ii nos'
    elif m == 19:
        stage_list = not_reported
        print 'not_reported'
    #target
    elif m == 20:
        stage_list = target_stage2b
        print 'target_stage2b'
    elif m == 21:
        stage_list = target_stage3
        print 'target_stage3'
    elif m == 22:
        stage_list = target_stage4
        print 'target_stage4'
    elif m == 23:
        stage_list = target_stage4s
        print 'target_stage4s'
    elif m == 24:
        stage_list = target_i
        print 'target_i'
    elif m == 25:
        stage_list = target_ii
        print 'target_ii'
    elif m == 26:
        stage_list = target_iii
        print 'target_iii'
    elif m == 27:
        stage_list = target_iiib
        print 'target_iiib'
    elif m == 28:
        stage_list = target_iii_iv
        print 'target_iii_iv'
    elif m == 29:
        stage_list = target_iiib_v
        print 'target_iiib_v'
    elif m == 30:
        stage_list = target_iv
        print 'target_iv'
    elif m == 31:
        stage_list = target_iv_v
        print 'target_iv_v'

    stage_cancer = []
    stage_near = []
    stage_contrast = []
    for i in stage_list:
        organize_number = i.split("-",7)[3]
        number = organize_number[0]
        if int(number) < 1:
            stage_cancer.append(i)
        elif int(number) == 1:
            stage_near.append(i)
        elif int(number) >1:
            stage_contrast.append(i)

    print 'cancer:\t',len(stage_cancer)
    print 'near:\t',len(stage_near)
    print 'contrast\t',len(stage_contrast),'\n'











#gdc_manifest_20170807_054456.txt
#metadata.cart.2017-08-07T05_45_09.652126.json

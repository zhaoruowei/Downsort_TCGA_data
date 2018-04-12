# Downsort_TCGA_data
Filter your Clean RNA-Seq Expression Data

__author__ = 'zhaoruowei'
#! /usr/env python
#-*-coding:utf-8-*-

#######################################################
####      Filter TCGA cleandata(by rename.py)      ####
#######################################################

import os

# project = 'Your working directory', which is one layer upper than 'Gene_Expression_Quantification' etc ...
project = "/Users/zhaoruowei/tmp/TCGA-LIHC/"

# script = '*.json directory', which is one storage download_script etc ...
script = "/Users/zhaoruowei/tmp/TCGA-LIHC/Download_data_script/"

RNAseq = 'Gene_Expression_Quantification/'
downloads = 'rawdata/'
named = 'named_data/'
analysis = 'analysis/'
stage = 'clean_stage/'
cancer = 'cancer/'
near = 'near/'
contrast = 'contrast/'
reported = 'reported/'
not_reported = 'not_reported'

os.chdir(project)

#def get_filename():, this file made by filter_organize,stage information had been plused
os.chdir(project + RNAseq + stage)
name_list = os.listdir(os.getcwd())

#check all file
for i in xrange(0,len(name_list)):
    file_name = name_list[i]
    try:
        #shell couldn't identify ' ' so we need use '\ ' to convert
        mv_file_name = file_name.split(" ",1)
        #get information of stage (reported or not_reported)
        stage_report = file_name.split("-",7)[7]
    except:
        #mac os will auto-generation some file, this file have bad influence on our script
        print "auto-generation file"
    else:
        #mv all not_reported file to the folder of 'not_reported/'
        if str(stage_report) == 'not reported.csv':
            os.system('mv' + ' ' + mv_file_name[0] + '\ ' + mv_file_name[1] + ' ' + not_reported)
        #mv file that have stage information to the folder of 'reported/'
        else:
            os.system('mv' + ' ' + mv_file_name[0] + '\ ' + mv_file_name[1] + ' ' + reported)

#due the file that have stage information
os.chdir(project + RNAseq + stage + reported)
reported_name_list = os.listdir(os.getcwd())
for i in xrange(0,len(reported_name_list)):
    reported_file_name = reported_name_list[i]
    try:
        #get number of cancer or near if num max than 2*, indicate this is contrast, elif num equal to 1*, indicate this is near cancer organise, elif this is cancer
        reported_cancer_number = reported_file_name.split("-",7)[3]
        #shell couldn't identify ' ' so we need use '\ ' to convert
        reported_mv_file_name = reported_file_name.split(" ",1)
    except:
        print "auto-generation file"
    else:
        number = reported_cancer_number[0]
        if int(number) < 1:
            os.system('mv ' + reported_mv_file_name[0] + '\ ' + reported_mv_file_name[1] +' ' + cancer)
        elif int(number) == 1:
            os.system('mv ' + reported_mv_file_name[0] + '\ ' + reported_mv_file_name[1] + ' ' + near)
        elif int(number) >1:
            os.system('mv ' + reported_mv_file_name[0] + '\ ' + reported_mv_file_name[1] + ' ' + contrast)

# Downsort_TCGA_data
Rename and Clean your RNA-Seq Expression Data 

__author__ = 'zhaoruowei'
#! /usr/env python
# -*-coding:utf-8-*-

import re
import os
import pandas as pd

# project = 'Your working directory', which is one layer upper than 'Gene_Expression_Quantification' etc ...
project = "/Users/zhaoruowei/tmp/TCGA-LIHC/"

# script = '*.json directory', which is one storage download_script etc ...
script = "/Users/zhaoruowei/tmp/TCGA-LIHC/Download_data_script/"

RNAseq = 'Gene_Expression_Quantification/'
downloads = 'rawdata/'
named = 'named_data/'
analysis = 'analysis/'
stage = 'clean_stage/'

os.chdir(project)

def find_submitter_id(download_directory,clean_directory):
    file = open(download_directory)
    lines = file.read()
    submitter_id_key = r'"entity_submitter_id": "(.*)",'
    file_name_key = r'"file_name": "(.*.htseq.counts.gz)",'
    stage_name_key = r'"tumor_stage": "(.*)",'
    tcga_name = re.findall(re.compile(submitter_id_key),lines)
    file_name = re.findall(re.compile(file_name_key),lines)
    stage_name = re.findall(re.compile(stage_name_key),lines)
    print file_name
    print len(file_name)
    print tcga_name
    print len(tcga_name)
    print stage_name
    print len(stage_name)

#def get_filename_list(clean_directory):
    new_filename_list = []
    filename_list = os.listdir(clean_directory)
    print filename_list
    print len(filename_list)
    for i in xrange(0,len(filename_list)):
        new_filename_list.append(filename_list[i]+".gz")
    print new_filename_list
    print len(new_filename_list)

#def replace_filename(clean_directory,filename_list,new_filename_list,file_name,tcga_name):
    for i in xrange(0,len(new_filename_list)):
        for x in xrange(0,len(file_name)):
            if new_filename_list[i] == file_name[x]:
                os.chdir(clean_directory)
                os.rename(filename_list[i],tcga_name[x])
                print 'replace done file' + i

#def plus_stage():
    os.chdir(clean_directory)
    for i in xrange(0,len(tcga_name)):
        old_fram = pd.read_table(tcga_name[i],header = None,names = ['gene',tcga_name[i]])
        stage_table = pd.Series(['stage',stage_name[i]], index=['gene',tcga_name[i]])
        new_fram = old_fram.append(stage_table,ignore_index = True)
        new_fram.to_csv(project + RNAseq + stage + tcga_name[i] + '-' + stage_name[i]+".csv", index=False)

json = raw_input('Json file name:\n')

find_submitter_id(script + jason,project + RNAseq + named)







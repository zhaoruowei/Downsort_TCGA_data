# Downsort_TCGA_data
Merge RNA-Seq Expression Cleandata

__author__ = 'zhaoruowei'
#! /usr/env python
# -*-coding:utf-8-*-

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

directory = raw_input("Input your directory:")

def merge_csv(stage_directory):
    os.chdir(stage_directory)
    filename_list = os.listdir(stage_directory)
    fram_list = [pd.read_csv(filename) for filename in filename_list]
    fram = fram_list[1]
    for i in xrange(2,len(fram_list)):
        fram = pd.merge(fram,fram_list[i])
    print "merge file have done!"
    merge_file_name = raw_input("Input your merge file name:")
    fram.to_csv(stage_directory + "/" + merge_file_name + ".csv",index = False)

merge_csv(directory)

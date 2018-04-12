# Downsort_TCGA_data
Download RNA-Seq or miRNA Expression Data 

__author__ = 'zhaoruowei'
#! /usr/env python
#-*-coding:utf-8-*-

#########################################
#### Download and Organize TCGA data ####
#########################################

'''
### GDC DATA PORTAL: [url=https://gdc.cancer.gov/]https://gdc.cancer.gov/[/url]
### Create the following folders:
    Gene_Expression_Quantification
        /rawdata
        /analysis
        /clean
    miRNA_Expression_Quantification
        /rawdata
        /analysis
        /clean    
    Download_data_script

### Put gdc-client into all Downloads folders
### Rename manifest and metadata using the following format:
    projectname_datacategory_manifest_xxx.txt
    projectname_datacategory_metadata_xxx.json

### move RNAseq_metadata and miRNA_metadata into their corresponding 'Analysis' folders

'''

import os
import shutil

# project = 'Your working directory', which is one layer upper than 'Gene_Expression_Quantification' etc ...
project = "/Users/zhaoruowei/tmp/TCGA-LIHC/"
os.chdir(project)

# software = 'gdc-client directory', which is one storage gdc-client etc ...
software = "/Users/zhaoruowei/tmp/TCGA-LIHC/Download_data_script/"

RNAseq = 'Gene_Expression_Quantification/'
miRNA = 'miRNA_Expression_Quantification/'
downloads = 'rawdata/'
clean = 'clean/'
analysis = 'analysis/'

def downloadRawData(directory, manifest):
    os.chdir(software)
    shutil.copy("gdc-client", directory)
    shutil.copy(manifest,directory)
    os.chdir(directory)
    print ('Start Downloading ...')
    os.system('./gdc-client download -m ' + manifest)
    print ('Download completed !')
    os.remove("gdc-client")
    os.remove(manifest)

dataCategory = raw_input('What kind of data are you going to download? (1.RNAseq; 2.miRNAs)\n')
manifest = raw_input('Manifest file name:\n')
print manifest

if dataCategory == '1':
    downloadRawData(project + RNAseq + downloads, manifest)

    ## copy downloaded data from 'Downloads' to the 'Clean' folder
    os.chdir(project + RNAseq)
    folders = os.listdir(downloads)
    for fd in folders:
        if os.path.isdir(downloads + fd):
            os.system('cp ' + downloads + fd + '/*.gz ' + clean)
    
    ## unzip the compressed .gz files
    os.system('gunzip ' + clean + '*.gz')

elif dataCategory == '2':
    downloadRawData(project + miRNA + downloads, manifest)
    os.chdir(project + miRNA)
    folders = os.listdir(downloads)
    for fd in folders:
        if os.path.isdir(downloads + fd):
            os.system('cp ' + downloads + fd + '/mirnas.quantification.txt ' + clean + fd + '.txt')
else:
    # pass
    print ('Enn, Let me decide later ...\n')

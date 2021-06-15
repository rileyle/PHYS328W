#!/usr/bin/python3

import sys
import os

yamlFile = open(sys.argv[1], 'r')
yaml = yamlFile.read()
yamlFile.close()

dirName = sys.argv[2]

# Get a list of all files in the current directory
fileNames = [line.rstrip() for line in os.listdir(os.getcwd()+'/'+dirName)]

# Submit jobs to make _histos.root files from all of the .mac files.
for fileName in fileNames:
    if '.html' in fileName:
        htmlFile = open(os.getcwd()+'/'+dirName+'/'+fileName, 'r')
        outFile = open(os.getcwd()+'/tmpFile.html', 'w')
        
        outFile.write(yaml)
        outFile.write(htmlFile.read())

        htmlFile.close()
        outFile.close()

        os.rename(os.getcwd()+'/tmpFile.html',
                  os.getcwd()+'/'+dirName+'/'+fileName)







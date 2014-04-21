#! /opt/local/bin/python

# IMPORT
import os
import sys
import shutil
import string
import glob
import math

ls = os.listdir('.')
ls.sort()

count = 0

rootdir = os.getcwd()
#outfile = open('','w')

for filename in glob.glob("*.tex"):
#for filename in glob.glob("schale08.tex"):
   print filename
   infile = open(filename, 'r')
   outfile = open('tmpfile', 'w')

   
   replacements = {'iny':'tiny'}

   for line in infile:
      if 'section' not in line and 'figure' not in line and 'centerin' not in line and 'label' not in line and 'caption' not in line:
          for src, target in replacements.iteritems():
              line = line.replace(src, target)
          outfile.write(line)

   infile.close()
   outfile.close()

   shutil.copyfile('tmpfile',filename)
   os.remove('tmpfile')

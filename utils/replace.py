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

#for filename in glob.glob("*.tex"):
for filename in glob.glob("test.tex"):
   print filename
   infile = open(filename, 'r')
   outfile = open('tmpfile', 'w')

   
   replacements = {'input{':'input{pics/near_clusters/', '   {':'   {data/near_clusters/', 'scale=1.5':'scale=0.55'}

   for line in infile:
      if 'section' and 'figure' and 'centerin' and 'label' and 'caption' not in line:
          for src, target in replacements.iteritems():
              line = line.replace(src, target)
          outfile.write(line)

   infile.close()
   outfile.close()

   shutil.copyfile('tmpfile',filename)
   os.remove('tmpfile')

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

for filename in glob.glob("fcc_size.dat"):
#for filename in glob.glob("schale08.tex"):
   print filename
   infile = open(filename, 'r')
   outfile = open('tmpfile', 'w')

   
#   replacements = {'includegraphics[scale=0.5]':'input', '/compl':'/schale', '/incompl':'/in-shell', '_':'-core', '.ps':'', 'caps':'cap'}
#   replacements = {'../data':'data'}
   replacements = {'E-04':'$\cdot 10^{-4}$', 'E-05':'$\cdot 10^{-5}$', 'E-06':'$\cdot 10^{-6}$'}

   for line in infile:
      if 'FloatBarrier' not in line:
          for src, target in replacements.iteritems():
              line = line.replace(src, target)
          outfile.write(line)

   infile.close()
   outfile.close()

   shutil.copyfile('tmpfile',filename)
   os.remove('tmpfile')

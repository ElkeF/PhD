#! /opt/local/bin/python

# IMPORT
import math


partial = [1.1407748351E-03,2.5762099258E-03,4.6398461909E-03]
#partial = [3.87662E-27,2.19171E-01,2.87102E-03,1.83693E-02,2.80956E-02]
total   = 6.1652493350e-03
hartree_to_eV = 2.7211383819580E+01


###################################
sum_partial = sum(partial)
new_partial = []
percent = []

for i in range(0,len(partial)):
   new_partial.append( partial[i] / sum_partial *total * hartree_to_eV )
   percent.append( new_partial[i] / total / hartree_to_eV)
   print new_partial[i], percent[i]
print total * hartree_to_eV

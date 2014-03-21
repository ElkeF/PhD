#! /opt/local/bin/python

# IMPORT
import math


partial = [9.9222359925E-04,8.3928442048E-03,7.2151629593E-03]
total   = 9.7508018383e-03
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 00:43:19 2019

@author: staubj
"""

import matplotlib.pyplot as plt
import sys


generations = []

for i in range(0,100):
    generations.append(i)
    
    
homo_A = []
uncertainty_homo_A = []

hetero = []
uncertainty_hetero = []

homo_B = []
uncertainty_homo_B = []

all_my_populations = []

file = open('Environmental_Stochasticity_Data.txt', 'r')

rows = file.readlines()

for index in range(len(rows)):
    values = rows[index].split(' , ')
    homo_A.append(float(values[1]))
    uncertainty_homo_A.append(float(values[2])/10)
    hetero.append(float(values[3]))
    uncertainty_hetero.append(float(values[4])/10)
    homo_B.append(float(values[5]))
    uncertainty_homo_B.append(float(values[6])/10)
    
moded_H = []
moded_Unc_H = []
gens = []

for i in range(0, len(homo_A), 10):
    moded_H.append(hetero[i])
    moded_Unc_H.append(uncertainty_hetero[i])
    gens.append(generations[i])

fig, ax = plt.subplots()
fig.set_tight_layout(True)
#ax.scatter(generations, homo_A, color = 'r', label = 'A Homozygous')
#ax.errorbar(generations, homo_A, yerr = uncertainty_homo_A, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
ax.scatter(generations, hetero, color = 'm', label = 'Heterozygous')
ax.errorbar(gens, moded_H, yerr = moded_Unc_H, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
#ax.scatter(generations, homo_B, color = 'b', label = 'B Homozygous')
#ax.errorbar(generations, homo_B, yerr = uncertainty_homo_B, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
ax.set_xlabel('Generation (years)')
ax.set_ylabel('Percent of Population')
ax.legend( title = 'Parameter:')
fig.savefig('Full_Environmental_Stochasticity_Figure_with_errorbars.png', filetype = 'png')
fig.savefig('Full_Environmental_Stochasticity_Figure_with_errorbars.svg', filetype = 'svg')
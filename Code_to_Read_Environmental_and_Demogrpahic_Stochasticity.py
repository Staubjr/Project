#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 00:43:19 2019

@author: staubj
"""

import matplotlib.pyplot as plt
import sys


def linear_regression(x_list, y_list):
    
    n = len(x_list)
    
    sigma_y = 0
    sigma_x = 0
    sigma_xy = 0
    sigma_x2 = 0
    sigma_y2 = 0
    
    for i in range(len(x_list)):
        
        sigma_y += y_list[i]
        
        sigma_x += x_list[i]
        
        sigma_x2 += ((x_list[i])**2)
        
        sigma_y2 += ((y_list[i])**2)
        
        sigma_xy += (y_list[i] * x_list[i])
        
    a = ( (sigma_y*sigma_x2) - (sigma_x*sigma_xy) ) / ( n*(sigma_x2) - (sigma_x)**2 )
        
    b = ( n*(sigma_xy) - (sigma_x*sigma_y) ) / ( n*(sigma_x2) - (sigma_x)**2 )
        
    num = n*sigma_xy - (sigma_x * sigma_y)
    den_1 = (n*sigma_x2 - (sigma_x)**2)**(0.5)      
    den_2 = (n*sigma_y2 - (sigma_y)**2)**(0.5)
    
    r = num/(den_1 * den_2)
    
    r_squared = r**2.
                
    vals = [b, a, r_squared]  
        
    return vals

generations = []

for i in range(0,100):
    generations.append(i)
    
    
E_homo_A = []
E_uncertainty_homo_A = []

E_hetero = []
E_uncertainty_hetero = []

E_homo_B = []
E_uncertainty_homo_B = []

all_my_populations = []

D_homo_A = []
D_uncertainty_homo_A = []

D_hetero = []
D_uncertainty_hetero = []

D_homo_B = []
D_uncertainty_homo_B = []

all_my_populations = []

file = open('Environmental_Stochasticity_Data.txt', 'r')

rows = file.readlines()

for index in range(len(rows)):
    values = rows[index].split(' , ')
    E_homo_A.append(float(values[1]))
    E_uncertainty_homo_A.append(float(values[2])/10)
    E_hetero.append(float(values[3]))
    E_uncertainty_hetero.append(float(values[4])/10)
    E_homo_B.append(float(values[5]))
    E_uncertainty_homo_B.append(float(values[6])/10)
    
file = open('Demographic_Stochasticity_Data.txt', 'r')

rows = file.readlines()

for index in range(len(rows)):
    values = rows[index].split(' , ')
    D_homo_A.append(float(values[1]))
    D_uncertainty_homo_A.append(float(values[2])/10)
    D_hetero.append(float(values[3]))
    D_uncertainty_hetero.append(float(values[4])/10)
    D_homo_B.append(float(values[5]))
    D_uncertainty_homo_B.append(float(values[6])/10)

#### For the linear regression lines ####
   
E_vals = linear_regression(generations, E_hetero)
D_vals = linear_regression(generations, D_hetero)

slope_E = E_vals[0]
slope_D = D_vals[0]
E_intercept = E_vals[1]
D_intercept = D_vals[1]
E_r = E_vals[2]
D_r = D_vals[2]
print(D_r, E_r)


E_line_x = []
E_line_y = []
D_line_x = []
D_line_y = []

delta = generations[99]/10
index = 0

while index <= generations[99]:
    E_line_x.append(index)
    D_line_x.append(index)
    E_line_y.append( (E_vals[0]*index) + E_vals[1] )
    D_line_y.append( (D_vals[0]*index) + D_vals[1] )
    index += delta

#### For errorbars ####

E_moded_H = []
E_moded_Unc_H = []
E_gens = []

D_H = []
D_Unc_H = []
D_gens_full = []

D_moded_H = []
D_moded_Unc_H = []
D_gens = []

for i in range(0, len(D_hetero), 2):
    D_H.append(D_hetero[i])
    D_Unc_H.append(D_uncertainty_hetero[i])
    D_gens_full.append(generations[i])

for i in range(0, len(E_homo_A), 10):
    E_moded_H.append(E_hetero[i])
    E_moded_Unc_H.append(E_uncertainty_hetero[i])
    E_gens.append(generations[i])
    D_moded_H.append(D_hetero[i])
    D_moded_Unc_H.append(D_uncertainty_hetero[i])    
    D_gens.append(generations[i])

fig, ax = plt.subplots()
fig.set_tight_layout(True)

#ax.scatter(generations, homo_A, color = 'r', label = 'A Homozygous')
#ax.errorbar(generations, homo_A, yerr = uncertainty_homo_A, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')

ax.scatter(generations, E_hetero, color = 'm', s = 60, label = 'Environmental Stochasticity')
ax.errorbar(E_gens, E_moded_H, yerr = E_moded_Unc_H, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
ax.plot(E_line_x, E_line_y, linestyle = '--', color = 'k')
ax.text(54, .445, 'H = {:.3e} * gen + {:.3f}'.format(slope_E, E_intercept))
ax.text(54, .435, '$R^2$ = {:.3f}'.format(E_vals[2]))

ax.scatter(D_gens_full, D_H, color = 'c', s = 60, label = 'Demographic Stochasticity')
ax.errorbar(D_gens, D_moded_H, yerr = D_moded_Unc_H, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')
ax.plot(D_line_x, D_line_y, linestyle = '--', color = 'k')
ax.text(45, .505, 'H = {:.3e} * gen + {:.3f}'.format(slope_D, D_intercept))
ax.text(45, 0.495, '$R^2$ = {:.3f}'.format(D_vals[2]))

#ax.scatter(generations, homo_B, color = 'b', label = 'B Homozygous')
#ax.errorbar(generations, homo_B, yerr = uncertainty_homo_B, capsize = 5, linewidth = 1, color = 'k', fmt = ' ')

ax.set_xlabel('Generation (years)')
ax.set_ylabel('Percent of Population')
ax.legend( title = 'Stochasticity Event:')
fig.savefig('Full_Stochasticity_Figure_with_errorbars.png', filetype = 'png')
fig.savefig('Full_Stochasticity_Figure_with_errorbars.svg', filetype = 'svg')
plt.show()
fig.show()
import os
import fnmatch
import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
import pdb

#First section is for user input
#-------------------------------------------------
#id_star1 - int: DAOPHOT ID# for first star.
#id_star2 - int: DAOPHOT ID# for second star.
#jack_img_num - int: Total number of jackknife images to be processed (including 2nd best ref-image)

#Generally, id_star1 is the brighter star but it's not strictly necessary.
id_star1 = [372]
id_star2 = [117]
jack_img_num = [14]

#-------------------------------------------------
#-------------------------------------------------
# Begin Program

data_dict = {} #Dictionary that will hold each jackknife starlist
star1_list = []
star2_list = []
jackknife_list = []

for i in range(jack_img_num):
    data_dict[i] = np.loadtxt('mag27maylgs__{0}_ks.als'.format(i+1), skiprows=2)
    for j in data_dict[i]:
        if j[0] == id_star1:
            star1_list.append(j[0:5])
    for j in data_dict[i]:
        if j[0] == id_star2:
            star2_list.append(j[0:5])
        
jackknife_list = np.hstack((star1_list, star2_list))

np.savetxt('jackknife_vals.dat', jackknife_list, fmt='%3s', header="id1, x1, y1, m1, me1, id2, x2, y2, m2, me2")


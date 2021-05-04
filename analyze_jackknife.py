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
#dt - int: time baseline (in years) between t0 and follow-up observation.

#Generally, id_star1 is the brighter star but it's not strictly necessary.
id_star1 = int(372)
id_star2 = int(117)
id_star3 = [] #Optional 3rd(blend) star
jack_img_num = int(14)
dt = int(11.199)

#-------------------------------------------------
#-------------------------------------------------
# Begin Program

data_dict = {} #Dictionary that will hold each jackknife starlist
star1_list = []
star2_list = []
star3_list = []
jackknife_list = []

for i in range(jack_img_num):
    data_dict[i] = np.loadtxt('mag27maylgs__{0}_ks.als'.format(i+1), skiprows=2)
    for j in data_dict[i]:
        if j[0] == id_star1:
            star1_list.append(j[0:5])
    for j in data_dict[i]:
        if j[0] == id_star2:
            star2_list.append(j[0:5])
# If 3-star jackknife, uncomment loop below (and 3-star jackknife_list below):            
#    for j in data_dict[i]:
#        if j[0] == id_star3:
#            star3_list.append(j[0:5])
            
#Stack stars in new jackknife_list
jackknife_list = np.hstack((star1_list, star2_list))
np.savetxt('jackknife_vals.dat', jackknife_list, fmt='%3s', header="id1, x1, y1, m1, me1, id2, x2, y2, m2, me2")
#-------
#3-star jackknife list below here:
#jackknife_list = np.hstack((star1_list, star2_list, star3_list))
#np.savetxt('jackknife_vals.dat', jackknife_list, fmt='%3s', header="id1, x1, y1, m1, me1, id2, x2, y2, m2, me2, id3, x3, y3, m3, me3")

#Calculate means and uncertainties for x,y,m via Equation 3 in Bhattacharya et al. 2021.

#jackknife_list = np.delete(jackknife_list, (3,7), axis=0) #remove outlier (optional).
#jack_img_num = 12
#print(jackknife_list)

dx = (jackknife_list[:, 6] - jackknife_list[:, 1])
dy = (jackknife_list[:, 7] - jackknife_list[:, 2])
dm = (jackknife_list[:, 8] - jackknife_list[:, 3])
mtot = -2.5*np.log10(((10**(-0.4*jackknife_list[:, 3]))+(10**(-0.4*jackknife_list[:, 8]))))
fratio = (10**(-0.4*jackknife_list[:, 8])/(10**(-0.4*jackknife_list[:, 3])))

dxbar = np.mean((jackknife_list[:, 6] - jackknife_list[:, 1]))
dybar = np.mean((jackknife_list[:, 7] - jackknife_list[:, 2]))
dmbar = np.mean((jackknife_list[:, 8] - jackknife_list[:, 3]))
mtotbar = np.mean(-2.5*np.log10(((10**(-0.4*jackknife_list[:, 3]))+(10**(-0.4*jackknife_list[:, 8])))))
fratiobar = np.mean((10**(-0.4*jackknife_list[:, 8])/(10**(-0.4*jackknife_list[:, 3]))))

dxerr = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dx - dxbar)**2))
dyerr = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dy - dybar)**2))
dmerr = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dm - dmbar)**2))
mtoterr = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((mtot - mtotbar)**2))
fratioerr = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((fratio - fratiobar)**2))

#Print results
print("dx = x1 - x2 =", dxbar, "+-", dxerr, "pix")
print("dy = y1 - y2 =", dybar, "+-", dyerr, "pix")
print("#-------------------------")
print("mu_rel,HE =", (dxbar*9.942)/dt, "+-", (dxerr*9.942)/dt, "mas/yr")
print("mu_rel,HN =", (dybar*9.942)/dt, "+-", (dyerr*9.942)/dt, "mas/yr")
print("mu_rel,H =", np.sqrt((dxbar)**2 + (dybar)**2)*9.942/dt, "+-", np.sqrt((dxerr)**2 + (dyerr)**2)*9.942/dt, "mas/yr")
print("#-------------------------")
print("dm = m1 - m2 =", dmbar, "+-", dmerr)
print("m_total =", mtotbar, "+-", mtoterr)
print("flux ratio = f1 / f2 =", fratiobar, "+-", fratioerr)



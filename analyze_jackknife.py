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
dt = int(11.12)

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
        
jackknife_list = np.hstack((star1_list, star2_list))

np.savetxt('jackknife_vals.dat', jackknife_list, fmt='%3s', header="id1, x1, y1, m1, me1, id2, x2, y2, m2, me2")

#Calculate means and uncertainties for x,y,m via Equation 3 in Bhattacharya et al. 2021.
jackknife_list = np.delete(jackknife_list, (3,7), axis=0) #remove outlier and/or alt. ref image data.
jack_img_num = 12
#print(jackknife_list)

x1bar = np.mean(jackknife_list[:, 1])
y1bar = np.mean(jackknife_list[:, 2])
m1bar = np.mean(jackknife_list[:, 3])

x2bar = np.mean(jackknife_list[:, 6])
y2bar = np.mean(jackknife_list[:, 7])
m2bar = np.mean(jackknife_list[:, 8])

x1err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:,1] - x1bar)**2))
y1err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:,2] - y1bar)**2))
m1err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:,3] - m1bar)**2))

x2err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:,6] - x2bar)**2))
y2err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:,7] - y2bar)**2))
m2err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:,8] - m2bar)**2))

sep_X = np.abs(x1bar - x2bar)
sep_X_err = np.sqrt((x1err)**2 + (x2err)**2)

sep_Y = np.abs(y1bar - y2bar)
sep_Y_err = np.sqrt((y1err)**2 + (y2err)**2)

#Print results
print("x1 =", x1bar, "+-", x1err)
print("y1 =", y1bar, "+-", y1err)
print("m1 =", m1bar, "+-", m1err)
print("#-------------------------")
print("x2 =", x2bar, "+-", x2err)
print("y2 =", y2bar, "+-", y2err)
print("m2 =", m2bar, "+-", m2err)
print("#-------------------------")
print("sep_X =", sep_X, "+-", sep_X_err, "pix")
print("sep_Y =", sep_Y, "+-", sep_Y_err, "pix")
print("#-------------------------")
print("mu_rel,HE =", (sep_X*9.942)/dt, "+-", (sep_X_err*9.942)/dt, "mas/yr")
print("mu_rel,HN =", (sep_Y*9.942)/dt, (sep_Y_err*9.942)/dt, "mas/yr")
print("mu_rel,H =", np.sqrt((sep_X)**2 + (sep_Y)**2)*9.942/dt, "+-", np.sqrt((sep_X_err)**2 + (sep_Y_err)**2)*9.942/dt, "mas/yr")
print("#-------------------------")
print("m2 - m1 =", m2bar - m1bar, "+-", np.sqrt((m1err)**2 + (m2err)**2))

#Propagate flux ratio errors (to-do: double check if propagation is correct! -ST)
#--------------------------------
exp_err = np.sqrt((0.4*m2err)**2 + (0.4*m1err)**2)
ln_err = exp_err * np.log(10)
f2f1_err = np.sqrt((0.4*m2err)**2 + (0.4*m1err)**2) * np.log(10) * (10**(-0.4*m2bar))/(((10**(-0.4*m1bar))))
f1f2_err = np.sqrt((0.4*m1err)**2 + (0.4*m2err)**2) * np.log(10) * (10**(-0.4*m1bar))/(((10**(-0.4*m2bar))))

f1tot_exp_err = np.sqrt((exp_err)**2 + (0.4*m1err)**2)
f2tot_exp_err = np.sqrt((exp_err)**2 + (0.4*m2err)**2)

f1tot_err = np.sqrt((exp_err)**2 + (0.4*m1err)**2) * np.log(10) * (10**(-0.4*m1bar))/((10**(-0.4*m1bar))+(10**(-0.4*m2bar)))
f2tot_err = np.sqrt((exp_err)**2 + (0.4*m2err)**2) * np.log(10) * (10**(-0.4*m2bar))/((10**(-0.4*m1bar))+(10**(-0.4*m2bar)))
#--------------------------------

print("f2 / f1 =", (10**(-0.4*m2bar))/(((10**(-0.4*m1bar)))), "+-", f2f1_err)
print("f1 / f2 =", (10**(-0.4*m1bar))/(((10**(-0.4*m2bar)))), "+-", f1f2_err)
print("f1 / (f1+f2) =", (10**(-0.4*m1bar))/((10**(-0.4*m1bar))+(10**(-0.4*m2bar))), "+-", f1tot_err)
print("f2 / (f1+f2) =", (10**(-0.4*m2bar))/((10**(-0.4*m1bar))+(10**(-0.4*m2bar))), "+-", f2tot_err)

fig = plt.subplots(figsize=(8,8))

plt.errorbar(x1bar,y1bar,xerr=x1err,yerr=y1err, color='r')
plt.errorbar(x2bar,y2bar,xerr=x2err,yerr=y2err, color='b')

plt.xlim(781,785)
plt.ylim(427,432)

plt.xlabel('X')
plt.ylabel('Y')

plt.show()



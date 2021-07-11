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
#jack_img_num - int: Total number of jackknife images to be processed (including aternative ref-image)
#dt - int: time baseline (in years) between t0 and follow-up observation.

#Generally, id_star1 is the brighter star but it's not strictly necessary.
id_star1 = int(1232)
id_star2 = int(1234)
id_star3 = int(1223)
jack_img_num = int(24)
dt = int(14.159)

#-------------------------------------------------
#-------------------------------------------------
# Begin Program

data_dict = {} #Dictionary that will hold each jackknife starlist
star1_list = []
star2_list = []
star3_list = []
jackknife_list = []

for i in range(jack_img_num):
    data_dict[i] = np.loadtxt('mag_OB06284_{0}_kp_tdOpen.als'.format(i+1), skiprows=2)
    for j in data_dict[i]:
        if j[0] == id_star1:
            star1_list.append(j[0:5])
    for j in data_dict[i]:
        if j[0] == id_star2:
            star2_list.append(j[0:5])
    for j in data_dict[i]:
        if j[0] == id_star3:
            star3_list.append(j[0:5])

#Stack stars in new jackknife_list
jackknife_list = np.hstack((star1_list, star2_list, star3_list))
np.savetxt('jackknife_vals.dat', jackknife_list, fmt='%3s', header="id1, x1, y1, m1, me1, id2, x2, y2, m2, me2, id3, x3, y3, m3, me3")
#-------------------------------------------------

#Calculate means and uncertainties for x,y,m,dx,dy,dm via Jackknife Equation #3 in Bhattacharya et al. 2021.

#jackknife_list = np.delete(jackknife_list, (3,7), axis=0) #remove outlier and/or alternate reference image data (if necessary).
#jack_img_num = 12
#print(jackknife_list)

x1bar = np.mean(jackknife_list[:,1])
y1bar = np.mean(jackknife_list[:,2])
m1bar = np.mean(jackknife_list[:,3])

x2bar = np.mean(jackknife_list[:,6])
y2bar = np.mean(jackknife_list[:,7])
m2bar = np.mean(jackknife_list[:,8])

x3bar = np.mean(jackknife_list[:,11])
y3bar = np.mean(jackknife_list[:,12])
m3bar = np.mean(jackknife_list[:,13])

x1err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 1] - x1bar)**2))
y1err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 2] - y1bar)**2))
m1err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 3] - m1bar)**2))

x2err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 6] - x2bar)**2))
y2err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 7] - y2bar)**2))
m2err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 8] - m2bar)**2))

x3err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 11] - x3bar)**2))
y3err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 12] - y3bar)**2))
m3err = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((jackknife_list[:, 13] - m3bar)**2))

#-------------
#Star 1-2 jackknife calc
#-------------
dx12 = (jackknife_list[:, 6] - jackknife_list[:, 1])
dy12 = (jackknife_list[:, 7] - jackknife_list[:, 2])
dm12 = (jackknife_list[:, 8] - jackknife_list[:, 3])
mtot12 = -2.5*np.log10(((10**(-0.4*jackknife_list[:, 3]))+(10**(-0.4*jackknife_list[:, 8]))))
fratio12 = (10**(-0.4*jackknife_list[:, 8])/(10**(-0.4*jackknife_list[:, 3])))

dxbar12 = np.mean((jackknife_list[:, 6] - jackknife_list[:, 1]))
dybar12 = np.mean((jackknife_list[:, 7] - jackknife_list[:, 2]))
dmbar12 = np.mean((jackknife_list[:, 8] - jackknife_list[:, 3]))
mtotbar12 = np.mean(-2.5*np.log10(((10**(-0.4*jackknife_list[:, 3]))+(10**(-0.4*jackknife_list[:, 8])))))
fratiobar12 = np.mean((10**(-0.4*jackknife_list[:, 8])/(10**(-0.4*jackknife_list[:, 3]))))

dxerr12 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dx12 - dxbar12)**2))
dyerr12 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dy12 - dybar12)**2))
dmerr12 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dm12 - dmbar12)**2))
mtoterr12 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((mtot12 - mtotbar12)**2))
fratioerr12 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((fratio12 - fratiobar12)**2))

#-------------
#Star 1-3 jackknife calc
#-------------
dx13 = (jackknife_list[:, 11] - jackknife_list[:, 1])
dy13 = (jackknife_list[:, 12] - jackknife_list[:, 2])
dm13 = (jackknife_list[:, 13] - jackknife_list[:, 3])
mtot13 = -2.5*np.log10(((10**(-0.4*jackknife_list[:, 3]))+(10**(-0.4*jackknife_list[:, 13]))))
fratio13 = (10**(-0.4*jackknife_list[:, 13])/(10**(-0.4*jackknife_list[:, 3])))

dxbar13 = np.mean((jackknife_list[:, 11] - jackknife_list[:, 1]))
dybar13 = np.mean((jackknife_list[:, 12] - jackknife_list[:, 2]))
dmbar13 = np.mean((jackknife_list[:, 13] - jackknife_list[:, 3]))
mtotbar13 = np.mean(-2.5*np.log10(((10**(-0.4*jackknife_list[:, 3]))+(10**(-0.4*jackknife_list[:, 13])))))
fratiobar13 = np.mean((10**(-0.4*jackknife_list[:, 13])/(10**(-0.4*jackknife_list[:, 3]))))

dxerr13 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dx13 - dxbar13)**2))
dyerr13 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dy13 - dybar13)**2))
dmerr13 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((dm13 - dmbar13)**2))
mtoterr13 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((mtot13 - mtotbar13)**2))
fratioerr13 = np.sqrt(((jack_img_num - 1)/(jack_img_num))*np.sum((fratio13 - fratiobar13)**2))

#Print results
print("POSITIONS & MAGNITUDES:")
print("")
print("x1 =", x1bar, "+-", x1err, "pix")
print("y1 =", y1bar, "+-", y1err, "pix")
print("m1=", m1bar, "+-", m1err)
print("-------------------------")
print("x2 =", x2bar, "+-", x2err, "pix")
print("y2 =", y2bar, "+-", y2err, "pix")
print("m2=", m2bar, "+-", m2err)
print("-------------------------")
print("x3 =", x3bar, "+-", x3err, "pix")
print("y3 =", y3bar, "+-", y3err, "pix")
print("m3=", m3bar, "+-", m3err)
print("-------------------------")
print("")
print("SEPARATIONS & FLUX RATIOS:")
print("")
print("dx = x1 - x2 =", dxbar12, "+-", dxerr12, "pix")
print("dy = y1 - y2 =", dybar12, "+-", dyerr12, "pix")
print("#-------------------------")
print("mu_rel,HE =", (dxbar12*9.942)/dt, "+-", (dxerr12*9.942)/dt, "mas/yr")
print("mu_rel,HN =", (dybar12*9.942)/dt, "+-", (dyerr12*9.942)/dt, "mas/yr")
print("mu_rel,H =", np.sqrt((dxbar12)**2 + (dybar12)**2)*9.942/dt, "+-", np.sqrt((dxerr12)**2 + (dyerr12)**2)*9.942/dt, "mas/yr")
print("#-------------------------")
print("dm = m1 - m2 =", dmbar12, "+-", dmerr12)
print("m_total =", mtotbar12, "+-", mtoterr12)
print("flux ratio = f1 / f2 =", fratiobar12, "+-", fratioerr12)
print("#-------------------------")
print("dx = x1 - x3 =", dxbar13, "+-", dxerr13, "pix")
print("dy = y1 - y3 =", dybar13, "+-", dyerr13, "pix")
print("#-------------------------")
print("mu_rel,HE =", (dxbar13*9.942)/dt, "+-", (dxerr13*9.942)/dt, "mas/yr")
print("mu_rel,HN =", (dybar13*9.942)/dt, "+-", (dyerr13*9.942)/dt, "mas/yr")
print("mu_rel,H =", np.sqrt((dxbar13)**2 + (dybar13)**2)*9.942/dt, "+-", np.sqrt((dxerr13)**2 + (dyerr13)**2)*9.942/dt, "mas/yr")
print("#-------------------------")
print("dm = m1 - m3 =", dmbar13, "+-", dmerr13)
print("m_total =", mtotbar13, "+-", mtoterr13)
print("flux ratio = f1 / f3 =", fratiobar13, "+-", fratioerr13)
#-------------------------------------------------

#Plot Results
fig = plt.subplots(figsize=(8,8))
plt.errorbar(x1bar,y1bar,xerr=x1err,yerr=y1err)
plt.errorbar(x2bar,y2bar,xerr=x2err,yerr=y2err)
plt.errorbar(x3bar,y3bar,xerr=x3err,yerr=y3err)

#plt.xlim(1140,1180)
#plt.ylim(1240,1245)
plt.xlabel('X [pix]', fontsize=18)
plt.ylabel('Y [pix]', fontsize=18)
plt.tick_params(which='both', length=8, width=1, labelsize=15, direction='in', right=True, top=True)

plt.show()




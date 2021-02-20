#for i in {1..8}; do  # STEP 1
#head -19 input_daophot.txt >> input_daophot.txt
#sed -i -e "$((19*i)),$((19*(i+1)))s/mag_OB06284_kp_tdOpen_1/mag_OB06284_kp_tdOpen_$((i+1))/g" input_daophot.txt
#done

#-----Comments-----#
# sed -i -e 's/blabla_old.coo/new_blabla.coo/g' input_daophot.txt in case need to change .coo file
# sed -i -e 's/blabla_old.lst/new_bla.lst/g' input_daophot.txt in case you need to change .lst file 
# repeat line 1, 2 for however many loops/ image combinations you have -1, eg. for 10 images n=9
# to remove the comment sign: sed -i -e 's/\#//g' input_daophot.txt
# every special character like: [, # will need an extra \ for sed.
#-------------------------#

#daophot-mcmc < input_daophot.txt  # STEP 2

#-----Comments-----#
# since allstar doesn't continue, copy paste the following 2 lines  as many times as your combination images-1.
#for i in {1..8}; do
#sed -i -e "1,3s/magtest$i/magtest$((i+1))/g" input_allstar.txt
#-------------------------#

#allstar < input_allstar.txt # STEP 3
#done 

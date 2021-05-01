for i in {1..13}; do  # STEP 1
head -16 input_daophot.txt >> input_daophot.txt
sed -i -e "$((16*i)),$((16*(i+1)))s/mag27maylgs__1/mag27maylgs__$((i+1))/g" input_daophot.txt
done

#-----Comments-----#
# sed -i -e 's/blabla_old.coo/new_blabla.coo/g' input_daophot.txt in case need to change .coo file
# sed -i -e 's/blabla_old.lst/new_bla.lst/g' input_daophot.txt in case you need to change .lst file 
# repeat line 1, 2 for however many loops/ image combinations you have -1, eg. for 10 images n=9
# to remove the comment sign: sed -i -e 's/\#//g' input_daophot.txt
# every special character like: [, # will need an extra \ for sed.
#-------------------------#

#daophot-mcmc < input_daophot.txt  # STEP 2

#for i in {1..13}; do  # STEP 3
#sed -i -e "1,3s/mag27maylgs__$i/mag27maylgs__$((i+1))/g" input_allstar.txt
#allstar < input_allstar.txt
#done
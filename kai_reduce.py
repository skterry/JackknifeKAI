# Copied from /u/jlu/data/microlens/20aug22os/reduce/reduce.py

##################################################
#
# General Notes:
# -- python uses spaces to figure out the beginnings
#    and ends of functions/loops/etc. So make sure
#    to preserve spacings properly (indent). This
#    is easy to do if you use emacs with python mode
#    and color coding.
# -- You will probably need to edit almost every
#    single line of the go() function.
# -- If you need help on the individual function calls,
#    then in the pyraf prompt, import the module and
#    then print the documentation for that function:
#    --> print nirc2.nirc2log.__doc__
#    --> print range.__doc__
#
##################################################

# Import python and iraf modules
from pyraf import iraf as ir
import numpy as np
import os, sys
import glob

# Import our own custom modules
from kai.reduce import calib
from kai.reduce import sky
from kai.reduce import data
from kai.reduce import util
from kai.reduce import dar
from kai.reduce import kai_util
from kai import instruments


##########
# Change the epoch, instrument, and distortion solution.
##########
epoch = '19may27'
nirc2 = instruments.NIRC2()

##########
# Make electronic logs
#    - run this first thing for a new observing run.
##########
def makelog_and_prep_images():
    """Make an electronic log from all the files in the ../raw/ directory.
    The file will be called nirc2.log and stored in the same directory.
    @author Jessica Lu
    @author Sylvana Yelda
    """
    nirc2_util.makelog('../raw', instrument=nirc2)

    # If you are reducing OSIRIS, you need to flip the images first. 
    #raw_files = glob.glob('../raw/i*.fits')
    #osiris.flip_images(raw_files)

    # Download weather data we will need.
    dar.get_atm_conditions('2019')

    return
    

###############
# Analyze darks
###############
# def analyze_darks():
#     """Analyze the dark_calib results
#     """
#     util.mkdir('calib')
#     os.chdir('calib')
# 
#     first_dark = 16
#     calib.analyzeDarkCalib(first_dark)  # Doesn't support OSIRIS yet
# 
#     os.chdir('../')

##########
# Reduce
##########
def go_calib():
    """Do the calibration reduction.
    @author Jessica Lu
    @author Sylvana Yelda
    """

    ####################
    #
    # Calibration files:
    #     everything created under calib/
    #
    ####################
    # Darks - created in subdir darks/
    #  - darks needed to make bad pixel mask
    #  - store the resulting dark in the file name that indicates the
    #    integration time (2.8s) and the coadds (10ca).
    #    -- If you use the OSIRIS image, you must include the full filename in the list. 
    #darkFiles = ['i200809_a003{0:03d}_flip'.format(ii) for ii in range(3, 7+1)]
    #calib.makedark(darkFiles, 'dark_2.950s_10ca_3rd.fits', instrument=osiris)

#    darkFiles = ['i200822_s003{0:03d}_flip'.format(ii) for ii in range(28, 32+1)]
#    calib.makedark(darkFiles, 'dark_5.901s_1ca_4rd.fits', instrument=osiris)

#    darkFiles = ['i200822_s020{0:03d}_flip'.format(ii) for ii in range(2, 10+1)]
#    calib.makedark(darkFiles, 'dark_11.802s_4ca_4rd.fits', instrument=osiris)

 #   darkFiles = ['i200822_s021{0:03d}_flip'.format(ii) for ii in range(2, 10+1)]
 #   calib.makedark(darkFiles, 'dark_5.901s_8ca_1rd.fits', instrument=osiris)

    # Flats - created in subdir flats/
    #offFiles = ['i200809_a013{0:03d}_flip'.format(ii) for ii in range(2, 11+1, 2)]
    #onFiles  = ['i200811_a002{0:03d}_flip'.format(ii) for ii in range(2, 13+1, 2)]
    #calib.makeflat(onFiles, offFiles, 'flat_kp_tdOpen.fits', instrument=osiris)

    # Masks (assumes files were created under calib/darks/ and calib/flats/)
    #calib.makemask('dark_2.950s_10ca_3rd.fits', 'flat_kp_tdOpen.fits',
    #               'supermask.fits', instrument=osiris)

    darkFiles = list(range(67, 72+1))
    calib.makedark(darkFiles, 'dark_30.0s_1ca.fits', instrument=nirc2)


    # Flats - created in subdir flats/
    offFiles = list(range(11, 16+1))
    onFiles = list(range(01, 06+1))
    calib.makeflat(onFiles, offFiles, 'flat_ks.fits', instrument=nirc2)
    
    # Masks
    calib.makemask('dark_30.0s_1ca.fits', 'flat_ks.fits',
                   'supermask.fits')



def go():
    """
    Do the full data reduction.
    """
    ##########
    #
    # OB06284
    #
    ##########

    ##########
    # Kp-band reduction
    ##########

    target = 'OB06284'
    #-----OSIRIS------
    #sci_files = ['i200810_a004{0:03d}_flip'.format(ii) for ii in range(2, 6+1)]
    #sci_files += ['i200822_a012{0:03d}_flip'.format(ii) for ii in range(2, 25+1)] #Add second dataset (on same night). [Optional]
    #sky_files = ['i200810_a007{0:03d}_flip'.format(ii) for ii in range(2, 6+1)] #16+1
    #refSrc = [1071, 854] # This is the target

    #sky.makesky(sky_files, target, 'kp_tdOpen', instrument=osiris)
    #data.clean(sci_files, target, 'kp_tdOpen', refSrc, refSrc, field=target, instrument=osiris)
    #data.calcStrehl(sci_files, 'kp_tdOpen', field=target, instrument=osiris)
    #data.combine(sci_files, 'kp_tdOpen', epoch, field=target,
    #                 trim=0, weight='strehl', submaps=3, instrument=osiris)
    #-----------------

    #-----NIRC2-------
    sci_files = list(range(133, 136+1))
    sky_files = list(range(224, 233+1))
    refSrc1 = [353., 469.] #This is the target

    sky.makesky(sky_files, 'nite1', 'ks', instrument=nirc2)
    data.clean(sci_files, 'nite1', 'ks', refSrc1, refSrc1, instrument=nirc2)
    data.calcStrehl(sci_files, 'ks', instrument=nirc2)
    data.combine(sci_files, 'ks', '27maylgs', trim=1, weight='strehl',
                   submaps=3, instrument=nirc2)
    #-----------------
    os.chdir('../')

    ##########
    #
    # KB200101
    #
    ##########

    ##########
    # Kp-band reduction
    ##########

#   util.mkdir('kp')
#   os.chdir('kp')

    #    -- If you have more than one position angle, make sure to
    #       clean them seperatly.
    #    -- Strehl and Ref src should be the pixel coordinates of a bright
    #       (but non saturated) source in the first exposure of sci_files.
    #    -- If you use the OSIRIS image, you must include the full filename in the list. 
#    target = 'OB060284'
#    sci_files = ['i200822_a014{0:03d}_flip'.format(ii) for ii in range(2, 28+1)]
#    sci_files += ['i200822_a015{0:03d}_flip'.format(ii) for ii in range(2, 5+1)]
#    sci_files += ['i200822_a016{0:03d}_flip'.format(ii) for ii in range(2, 5+1)]
#    sky_files = ['i200822_a017{0:03d}_flip'.format(ii) for ii in range(2, 6+1)]
#    refSrc = [975, 1006] # This is the target
    # Alternative star to try (bright star to right of target): [1158, 994]
    
#    sky.makesky(sky_files, target, 'kp_tdOpen', instrument=osiris)
#    data.clean(sci_files, target, 'kp_tdOpen', refSrc, refSrc, field=target, instrument=osiris)
#    data.calcStrehl(sci_files, 'kp_tdOpen', field=target, instrument=osiris)
#    data.combine(sci_files, 'kp_tdOpen', epoch, field=target,
#                     trim=1, weight='strehl', submaps=3, instrument=osiris)
#
def jackknife():
    """
    Do the Jackknife data reduction.
    """
    ##########
    #
    # OB06284
    #
    ##########

    ##########
    # Kp-band reduction
    ##########

    target = 'OB06284'
    #sci_files = ['i200810_a004{0:03d}_flip'.format(ii) for ii in range(2, 26+1)] OG
    sci_files = ['i200810_a004{0:03d}_flip'.format(ii) for ii in range(2, 26+1)]
 #   sci_files += ['i200822_a012{0:03d}_flip'.format(ii) for ii in range(2, 25+1)]
    sky_files = ['i200810_a007{0:03d}_flip'.format(ii) for ii in range(2, 6+1)] #16+1
    refSrc = [1071, 854] # This is the target
    # Alternative star to try (bright star to bottom of target): [1015, 581.9]

    sky.makesky(sky_files, target, 'kp_tdOpen', instrument=osiris)

    for i in enumerate(sci_files, start=1):
        jack_list = sci_files[:]
        jack_list.remove(i[1])
        data.clean(jack_list, target, 'kp_tdOpen', refSrc, refSrc, field=target, instrument=osiris)
        data.calcStrehl(jack_list, 'kp_tdOpen', field=target, instrument=osiris)
        data.combine(jack_list, 'kp_tdOpen', epoch, field=target,
                     trim=0, weight='strehl', submaps=3, instrument=osiris, outSuffix='_' + str(i[0]))
    os.chdir('../')




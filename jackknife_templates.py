#Jackknife reduction templates for NIRC2 and OSIRIS pipelines.
#Author: Sean Terry


def jackknife():
    """
    Do the Jackknife data reduction.
    """
    ##########
    #
    # NIRC2 Format
    #
    ##########

    ##########
    # Ks-band reduction
    ##########

    # Nite 1
    target = 'MB07192'
    sci_files1 = list(range(173, 177+1))
    sky_files1 = list(range(206, 215+1))
    refSrc1 = [385., 440.] #This is the target nearest to center

    sky.makesky(sky_files1, 'nite1', 'ks', instrument=nirc2)
    data.clean(sci_files1, 'nite1', 'ks', refSrc1, refSrc1, instrument=nirc2)


    # Nite 2
    sci_files2 = list(range(195, 203+1))
    sky_files2 = list(range(206, 215+1))
    refSrc2 = [387., 443.] #This is the target nearest to center

    sky.makesky(sky_files2, 'nite2', 'ks', instrument=nirc2)
    data.clean(sci_files2, 'nite2', 'ks', refSrc2, refSrc2, instrument=nirc2)
    #-----------------

    sci_files = sci_files1 + sci_files2

    for i in enumerate(sci_files, start=1):
        jack_list = sci_files[:]
        jack_list.remove(i[1])
        data.calcStrehl(jack_list, 'ks', instrument=nirc2)
        data.combine(jack_list, 'ks', '27maylgs', trim=1, weight='strehl',
                    instrument=nirc2, outSuffix='_' + str(i[0]))
        os.chdir('reduce')


    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------

def jackknife():
    """
    Do the Jackknife data reduction.
    """
    ##########
    #
    # OSIRIS Format
    #
    ##########

    ##########
    # Kp-band reduction
    ##########

    target = 'OB06284'
    sci_files = ['i200810_a004{0:03d}_flip'.format(ii) for ii in range(2, 26+1)]
    sky_files = ['i200810_a007{0:03d}_flip'.format(ii) for ii in range(2, 6+1)]
    refSrc = [1071., 854.] # This is the target

    sky.makesky(sky_files, target, 'kp_tdOpen', instrument=osiris)

    for i in enumerate(sci_files, start=1):
        jack_list = sci_files[:]
        jack_list.remove(i[1])
        data.clean(jack_list, target, 'kp_tdOpen', refSrc, refSrc, field=target, instrument=osiris)
        data.calcStrehl(jack_list, 'kp_tdOpen', field=target, instrument=osiris)
        data.combine(jack_list, 'kp_tdOpen', epoch, field=target,
                     trim=0, weight='strehl', instrument=osiris, outSuffix=str(i[0]))
        os.chdir('reduce')


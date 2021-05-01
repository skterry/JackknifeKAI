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

    target = 'OB110950'
    sci_files = list(range(133, 146+1))
    sky_files = list(range(224, 233+1))
    refSrc1 = [353., 469.] #This is the target

    sky.makesky(sky_files, 'nite1', 'ks', instrument=nirc2)

    for i in enumerate(sci_files, start=1):
        jack_list = sci_files[:]
        jack_list.remove(i[1])
        data.clean(jack_list, 'nite1', 'ks', refSrc1, refSrc1, instrument=nirc2)
        data.calcStrehl(jack_list, 'ks', instrument=nirc2)
        data.combine(jack_list, 'ks', '27maylgs', trim=1, weight='strehl',
                    submaps=3, instrument=nirc2, outSuffix=str(i[0]))
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

    util.mkdir('kp')
    os.chdir('kp')

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
                     trim=0, weight='strehl', submaps=3, instrument=osiris, outSuffix=str(i[0]))
        os.chdir('reduce')


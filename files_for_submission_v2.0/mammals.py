"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
     ## Mammals
               "pg_2861_6647", # Elephantidae. Rohland et al. 2010. PLoS Biol.
               "pg_2859_6643", # Muroidea. Schenk et al. 2013. Syst. Biol.
               "pg_1797_3635", # Tenrecidae. Poux et al. 2008. BMC Evol. Biol.
               "pg_2844_6605", # Talpa. Colangelo et al. 2010. MPE
               "pg_2843_6604", # Talpidae. He et al. 2014. MPE
               "pg_2825_6572", # Xenarthra. Delsuc et al. 2012. MPE
               "pg_2695_6250", # Ursidae. Krause et al. 2008. BMC Evol. Biol.
               "pg_2656_6185", # Primates. Springer et al. 2012. PLoS ONE
               "pg_1600_3231", # Euarchontoglires (Primates). Perelman et al. 2011. PloS Genetics *** Springer et al. have better sampling, but trees agree
               "pg_2688_6240", # Rodentia. Fabre et al. 2012. BMC Evol. Biol.
               "pg_2359_4962", # Antilopinae. Barmann et al. 2013. MPE
               "pg_2687_6239", # Phocidae. Fulton and Strobeck. 2009. Proc. Roy. Soc.
               "pg_2691_6244", # Procyonidae. Koepfli et al. 2007. MPE
               "pg_2685_6235", # Mustelidae. Koepfli et al. 2008. BMC Evol. Biol.
               "ot_168_1",     # Pteropus. Almeida et al. 2014. MPE
               "pg_1634_3303", # Chiroptera. Agnarsson et al. 2011. PLoS Currents Tree of Life
               "pg_1927_6215", # Cetacea. Steeman et al. 2009. Syst. Biol.
               "pg_2587_5998", # Cetacea. McGowen et al. 2009. MPE
               "pg_1981_4052", # Felidae. Johnson et al. 2006. Science
               "pg_2684_6644", # Hyaenidae. Koepfli et al. 2006. MPE
               "pg_1428_2855", # Mammals. Meredith et al. 2011. Science
               "pg_1646_6231", # Caniformia (Pinnipeds). Higdon et al. 2007. BMC Evol. Biol.
               "pg_2833_6588", # Metatheria. Cardillo et al. 2004. J. Zool.
               "pg_2834_6589", # Metatheria. Nilsson et al. 2004. Gene
               "pg_2816_6556", # Primates. Pozzi et al. 2014. MPE
               "pg_2741_6645", # Catarrhini. Tarver et al. 2011. Proc. Roy. Soc. *** Lots of extinct taxa ***
            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "___main__":
    import load_synth_extract
    from wopr_conf import *
    #from stephen_desktop_conf import *

    synthottolid="691846"

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)
    else:
        print "Assuming all studies have already been downloaded to:", studyloc

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


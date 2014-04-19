studytreelist=[
## Mammals
               "2861_6647", # Elephantidae. Rohland et al. 2010. PLoS Biol.
               "2859_6643", # Muroidea. Schenk et al. 2013. Syst. Biol.
               "1797_3635", # Tenrecidae. Poux et al. 2008. BMC Evol. Biol.
               "2844_6605", # Talpa. Colangelo et al. 2010. MPE
               "2843_6604", # Talpidae. He et al. 2014. MPE
               "2825_6572", # Xenarthra. Delsuc et al. 2012. MPE
               "2695_6250", # Ursidae. Krause et al. 2008. BMC Evol. Biol.
               "2656_6185", # Primates. Springer et al. 2012. PLoS ONE
               "1600_3231", # Euarchontoglires (Primates). Perelman et al. 2011. PloS Genetics *** Springer et al. have better sampling, but trees agree
               "2688_6240", # Rodentia. Fabre et al. 2012. BMC Evol. Biol.
               "2359_4962", # Antilopinae. Barmann et al. 2013. MPE
               "2687_6239", # Phocidae. Fulton and Strobeck. 2009. Proc. Roy. Soc.
               "2691_6244", # Procyonidae. Koepfli et al. 2007. MPE
               "2685_6235", # Mustelidae. Koepfli et al. 2008. BMC Evol. Biol.
               "1634_3303", # Chiroptera. Agnarsson et al. 2011. PLoS Currents Tree of Life
               "1927_6215", # Cetacea. Steeman et al. 2009. Syst. Biol.
               "2587_5998", # Cetacea. McGowen et al. 2009. MPE
               "1981_4052", # Felidae. Johnson et al. 2006. Science
               "2684_6644", # Hyaenidae. Koepfli et al. 2006. MPE
               "1428_2855", # Mammals. Meredith et al. 2011. Science
               "1646_6231", # Caniformia (Pinnipeds). Higdon et al. 2007. BMC Evol. Biol.
               "2833_6588", # Metatheria. Cardillo et al. 2004. J. Zool.
               "2834_6589", # Metatheria. Nilsson et al. 2004. Gene
               "2816_6556", # Primates. Pozzi et al. 2014. MPE
               "2741_6645", # Catarrhini. Tarver et al. 2011. Proc. Roy. Soc. *** Lots of extinct taxa ***
            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="691846"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


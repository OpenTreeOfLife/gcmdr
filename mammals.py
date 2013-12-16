studytreelist=[
     ## Mammals
               "2695_6250", # Ursidae. Krause et al. 2008. BMC Evol. Biol.
               "1600_3231", # Euarchontoglires (Primates). Perelman et al. 2011. PloS Genetics *** replace with Springer et al.
               "2656_6185", # Primates. Springer et al. 2012. PLoS ONE
               "2688_6240", # Rodentia. Fabre et al. 2012. BMC Evol. Biol.
               "2359_4962", # Antilopinae. Barmann et al. 2013. MPE
               "2687_6239", # Phocidae. Fulton and Strobeck. 2009. Proc. Roy. Soc.
               "2691_6244", # Procyonidae. Koepfli et al. 2007. MPE
               "2685_6235", # Mustelidae. Koepfli et al. 2008. BMC Evol. Biol.
               "1634_3303", # Chiroptera. Agnarsson et  al. 2011. PLoS Currents Tree of Life
               "1927_6215", # Cetacea. Steeman et al. 2009. Syst. Biol.
               "1981_4052", # Felidae. Johnson et al. 2006. Science
               "2684_6229", # Hyaenidae. Koepfli et al. 2006. MPE
               "1797_3635", # Tenrecidae. Poux et al. 2008. BMC Evol. Biol.
               "1428_2855", # Mammals. Meredith et al. 2011. Science
               "1646_6231", # Caniformia (Pinnipeds). Higdon et al. 2007. BMC Evol. Biol.
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


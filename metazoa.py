

synthottolid="691846"

studytreelist=["2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE
               "2599_6021", # Alaudidae (larks). Alstrom et al. 2013. MPE
               "2591_6008", # Parulidae (warblers). Lovette et al. 2008. MPE
               "2575_5974", # Passeriformes. Barker et al. 2013. Syst. Biol.
               "2015_4152", # Passeriformes. Odeen et al. 2011. Evolution
               "1634_3303", # Chiroptera. Agnarsson et  al. 2011. PLoS Currents Tree of Life
               "420_522",   # Aves. Hackett et al. 2008. Science
               "1600_3231", # Primates. Perelman et al. 2011. PloS Genetics
               "1428_2855", # Mammals. Meredith et al. 2011. Science
               "2415_5096", # Turtles. Guillon et al. 2012. Contributions to Zoology
               "423_2857",  # Amphibia. Pyron and Weins. 2011. MPE
               "2589_6001", # Gobioidei (fish). Agorreta et al. 2013. MPE
               "2655_6181", # Cichlidae. Friedman et al. 2013. Proc. Roy. Soc.
               "1997_6183", # Percidae. Near et al. 2011. Syst. Biol.
               "2551_6180", # Holacanthopterygii. Wainwright et al. 2012. Syst. Biol.
               "2654_6179", # Leiognathidae (fish). Chakrabarty et al. 2011. Mol. Ecol.
               "2585_5994", # Tetraodontiformes (fish). Santini et al. 2013. MPE
               "2576_5975", # Euteleostei (fish). Near et al. 2013. PNAS
               "1870_3769", # Cyprinidae (fish). Ruber et al. 2007. BMC Evol. Biol.
               "2573_5959", # Sauria. Crawford et al. 2012. Biology Letters
               "2460_5285", # Squamata. Pyron et al. 2013. BMC Evol. Biol.
               "421_523",   # Mollusca. Smith et al. 2011. Nature
               "1482_5228", # Eumetazoa. Evans et al. 2008. BMC Evol. Biol.
               "1217_2455", # Metazoa. Delsuc et al. 2008. Genesis
               "1366_6166", # Annelida. Struck et al. 2011. Nature
               "1563_6170", # Hymenoptera. Sharkey et al. 2011. Cladistics
               "1849_3731", # Formicidae (insect). Brady et al. 2006. PNAS
               "1776_3581", # Ditrysia (insect). Cho et al. 2011. Syst. Biol.
               "1761_6151", # Scleractinia (corals). Huang nad Roy. 2013. Ecology and Evolution
               "2407_5075", # Bilateria. Anderson et al. 2004. JME
               "1337_6167", # Holometabola (insect). Wiegmann et al. 2009. BMC Evol. Biol.
               "2629_6162", # Hexapoda. Letsch and Simon. 2013. Syst. Entomology
               "2604_6043", # Apoidea. Hedtke et al. 2013. BMC Evol. Biol.
               "2418_6152"] # Metazoa. Evans and Cartwright. 2010. MBE

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="691846"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn)

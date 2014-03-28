"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
     ## Birds
               "2806_6529", # Psittaciformes. Joseph et al. 2011. MPE
               "2805_6512", # Psittaciformes. Wright et al. 2008. MBE
               "1979_6300", # Psittacidae. Tavares et al. 2006. Syst. Biol.

               "2444_6526", # Columbiformes. Pereira et al. 2007. Syst. Biol.
               "2798_6497", # Spheniscidae. Subramanian et al. 2013. Biol. Lett.
               "2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE
               "2658_6192", # Trochilidae. McGuire et al. 2007. Syst. Biol.
               "2796_6491", # Pipridae. Ohlson et al. 2013. MPE
               "2707_6281", # Icteridae. Powell et al. 2013. MPE
               "1966_4019", # Maluridae. Lee et al. 2011. Syst. Biol.
               "2600_6022", # Paridae. Johansson et al. 2013. MPE
               "2599_6021", # Alaudidae (larks). Alstrom et al. 2013. MPE
               "2591_6008", # Parulidae (warblers). Lovette et al. 2008. MPE
               "2454_5247", # Thamnophilus. Brumfield and Edwards. 2007. Evolution
               "2692_6245", # Fringillidae. Zuccon et al. 2012. MPE
               "2702_6274", # core Corvoidea. Aggerbeck et al. 2014. MPE
               "2575_5974", # Passeriformes. Barker et al. 2013. Syst. Biol.
               "2015_4152", # Passeriformes. Odeen et al. 2011. Evolution
               "420_522",   # Aves. Hackett et al. 2008. Science
     ## Mammals
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
               "1981_4052", # Felidae. Johnson et al. 2006. Science
               "2684_6229", # Hyaenidae. Koepfli et al. 2006. MPE
               "1797_3635", # Tenrecidae. Poux et al. 2008. BMC Evol. Biol.
               "1428_2855", # Mammals. Meredith et al. 2011. Science
               "1646_6231", # Caniformia (Pinnipeds). Higdon et al. 2007. BMC Evol. Biol.

     ## Fish - need to figure out best ordering with mapcompat
#               "2651_6177", # Actinopterygii (Bony fishes). Betancur-R et al. 2013. PLoS Currents

               "2589_6001", # Gobioidei. Agorreta et al. 2013. MPE
               "2655_6181", # Cichlidae. Friedman et al. 2013. Proc. Roy. Soc.
               "1997_6183", # Percidae. Near et al. 2011. Syst. Biol. *** not working for some reason...
               "2654_6179", # Leiognathidae. Chakrabarty et al. 2011. Mol. Ecol.
               "2585_5994", # Tetraodontiformes. Santini et al. 2013. MPE
               "2653_6178", # Percomorpha. Miya et al. 2013. PLoS ONE *** prefer this over Near et al. 2012
               "2657_6191", # Percomorpha. Near et al. 2012. MPE
               "2551_6180", # Holacanthopterygii. Wainwright et al. 2012. Syst. Biol.
               "2576_5975", # Euteleostei. Near et al. 2013. PNAS
               "1870_3769", # Cyprinidae. Ruber et al. 2007. BMC Evol. Biol.
               "2659_6195", # Otophysi. Chen et al. 2013. Evolution

     ## Other tetrapods
               "2415_5096", # Turtles. Guillon et al. 2012. Contributions to Zoology
               "423_2857",  # Amphibia. Pyron and Weins. 2011. MPE
               "2573_5959", # Sauria. Crawford et al. 2012. Biology Letters
               "2711_6295", # Henophidia. Reynolds et al. 2014. MPE *** check this doesn't break the Pyron study
               "2460_5285", # Squamata. Pyron et al. 2013. BMC Evol. Biol. -- Anolis nonmonophyly

     ## Decapoda
               "1252_2661", # maps to: Anomura
               "1336_2660", # maps to: Brachyura
               "1948_6513", # maps to: Anomura
               "1796_6514", # maps to: Typhlatya
               "2243_6515", # maps to: Paramunida
               "2670_6214", # maps to: Atyidae
               "2671_6216", # maps to: Caridina
               "2673_6219", # maps to: Astacidea
               "2674_6220", # maps to: Cambaridae
               "2675_6221", # maps to: Cambaridae
               "2676_6222", # maps to: Scyllaridae
               "2677_6223", # maps to: Anomura
               "2682_6227", # maps to: Decapoda
               "2683_6228", # maps to: Dendrobranchiata
               "2807_6519", # maps to: Alpheidae
               "2808_6522", # maps to: Alpheoidea
               "2667_6211", # maps to: Galatheoidea

     ## Insects and other crawley stuff
               "2581_5987", # Membracidae. Cryan et al. 2004. Syst. Ent.
               "2087_4323", # Austrogoniodes. Banks and Paterson. 2004. Invert. Syst.
               "2811_6533", # Vespinae. Lopez-Osorio et al. 2014. MPE
               "1988_4074", # Mantodea. Svenson et al. 2009. CLadistics
               "2593_6247", # Dermaptera. Kocarek et al. 2013. PLoS ONE
               "1563_6170", # Hymenoptera. Sharkey et al. 2011. Cladistics
               "1849_3731", # Formicidae. Brady et al. 2006. PNAS
               "2664_6201", # Ditrysia. Regier et al. 2013. PLoS ONE *** prefer this over Cho et al. 2011
               "1776_3581", # Ditrysia. Cho et al. 2011. Syst. Biol.
               "1337_6167", # Holometabola (insect). Wiegmann et al. 2009. BMC Evol. Biol.
               "2629_6162", # Hexapoda. Letsch and Simon. 2013. Syst. Ent.
               "2604_6043", # Apoidea. Hedtke et al. 2013. BMC Evol. Biol.
               #"2686_6238", # Arthropoda. Lee et al. 2013. Curr. Biol.
               "437_6242",  # Diptera. Wiegmann et al. 2011. PNAS
               "1338_2666", # Pterygota. Simon et al. 2009. MBE

     ## Other
               "1343_6255", # Hexactinella. Dohrmann et al. 2009. MPE
               "1788_6534", # Siphonophora. Dunn et al. 2005. Syst. Biol.
               "1786_6257", # Hydrozoa. Cartwright et al. 2008. J. Marine Biol. Assoc. UK
               "2678_6224", # Echinodermata. Janies et al. 2011. Syst. Biol.
               "421_523",   # Mollusca. Smith et al. 2011. Nature
               "1366_6166", # Annelida. Struck et al. 2011. Nature
               "1761_6151", # Scleractinia (corals). Huang nad Roy. 2013. Ecology and Evolution
               "2710_6291"  # Metazoa. Ryan et al. 2013. Science *** need to choose best Metazoa tree(s)
            #   "1482_5228", # Eumetazoa. Evans et al. 2008. BMC Evol. Biol. <- breaks stuff?
            #   "1217_2455", # Metazoa. Delsuc et al. 2008. Genesis
            #   "2418_6152", # Metazoa. Evans and Cartwright. 2010. MBE *** not working for some reason...
            #   "2407_6390", # Bilateria. Anderson et al. 2004. JME

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


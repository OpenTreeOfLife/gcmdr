studytreelist=[
## Birds
               "2876_6670", # Tinamidae. Bertelli, Sara, Ana Luz Porzecanski
               "2875_6668", # Oriolidae. Jonsson et al. 2010. Ecography
               "2874_6667", # Carpodacus. Tietze et al. 2013. Zool. J. Linn. Soc.
               "2873_6666", # Certhia. Tietze et al. 2006. Ibis
               "2332_4912", # Sylviidae. Voelker and Light. 2011. BMC Evol. Biol. *** Pseudoalcippe should be in the family Silviidae rather than Timaliidae
               "1854_3743", # Troglodytinae. Mann et al. 2006. MPE
               "1586_3208", # Timaliidae. Moyle et al. 2012. Syst. Biol.
               "2858_6642", # Turdidae. Nylander et al. 2008. Syst. Biol.
               "2829_6579", # Thraupidae. Burns et al. 2014. MPE
               "1953_3977", # Furnariidae. Derryberry et al. 2011. Evolution
               "2872_6665", # Caprimuligidae. Han et al. MPE
               "1872_3780", # Gruiformes. Fain et al 2007. MPE
               "2869_6661", # Bucerotiformes. Gonzalez et al. 2013. MPE
               "2870_6662", # Falconidae. Fuchs et al. 2011. MPE
               "2871_6663", # Falconidae. Fuchs et al. 2012. Ibis
               "2864_6651", # Platalea. Chesser et al. 2010. Zootaxa
               "2845_6606", # Sitta. Pasquet et al. 2014. J. Ornith.
               "2806_6529", # Psittaciformes. Joseph et al. 2011. MPE
               "2805_6512", # Psittaciformes. Wright et al. 2008. MBE
               "1979_6300", # Psittacidae. Tavares et al. 2006. Syst. Biol.
               "2857_6628", # Gyps. Arshad et al. 2009. J. Ornith.
               "1887_6629", # Accipitridae. Lerner et al. 2008. Auk
               "2850_6620", # Columbidae. Cibois et al. 2014. MPE
               "2444_6526", # Columbiformes. Pereira et al. 2007. Syst. Biol.
               "2798_6497", # Spheniscidae. Subramanian et al. 2013. Biol. Lett.
               "2866_6656", # Anseriformes. Gonzalez et al. 2009. J. Zool.
               "2860_6646", # Anatidae. Fulton et al. 2012. Proc. Roy. Soc.
               "2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE
               "2865_6654", # Cynanthus. Garcia-Deras et al. 2008. Zootaxa.
               "2853_6624", # Trochilidae. McGuire et al. 2014. Curr. Biol. *** Replaces McGuire et al. 2007. Syst. Biol.
               "2796_6491", # Pipridae. Ohlson et al. 2013. MPE
               "2707_6281", # Icteridae. Powell et al. 2013. MPE *** Hypopyrrhus not mapped to Icteridae
               "1966_4019", # Maluridae. Lee et al. 2011. Syst. Biol.
               "2600_6022", # Paridae. Johansson et al. 2013. MPE
               "2599_6021", # Alaudidae (larks). Alstrom et al. 2013. MPE
               "2591_6008", # Parulidae (warblers). Lovette et al. 2008. MPE
               "2454_5247", # Thamnophilus. Brumfield and Edwards. 2007. Evolution
               "2692_6245", # Fringillidae. Zuccon et al. 2012. MPE
               "2702_6274", # core Corvoidea. Aggerbeck et al. 2014. MPE *** mapping back to Passeroidea
               "2575_5974", # Passeriformes. Barker et al. 2013. Syst. Biol.
               "2015_4152", # Passeriformes. Odeen et al. 2011. Evolution
               "420_522",   # Aves. Hackett et al. 2008. Science
            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="81461"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


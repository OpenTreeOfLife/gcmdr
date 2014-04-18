"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


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

     ## Fish - need to figure out best ordering with mapcompat
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
               "2143_4505", # Kentropyx. Collevatti et al. 2008. Mol. Ecol.
               "2098_6487", # Stenocercus. Torres-Carvajal et al. 2005. MPE
               "2851_6621", # Kinosternidae. Spinks at al. 2014. MPE
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
               "2405_6669", # Phyllodocidae. Eklof et al. 2007. MPE
               "2614_6121", # Nicrophorus. Sikes and Venables. 2013.
               "2628_6143", # Sarcophaga. Whitmore et al. 2013. Zool. J. Linn. Soc.
               "2838_6594", # Pleocyemata. Bracken-Grissom et al. 2014. Syst. Biol.
               "2357_6538", # Evaniscus. Mullins et al. 2012. ZooKeys <- 2 new species are not in OTT
               "2323_6537", # Bombyliidae. Lambkin and Bartlett. 2011. ZooKeys <- check sampling
               "1940_3943", # Drosophilidae. Van der Linde et al. 2010. Genet. Res.
               "2581_5987", # Membracidae. Cryan et al. 2004. Syst. Ent.
               "2087_4323", # Austrogoniodes. Banks and Paterson. 2004. Invert. Syst.
               "2811_6533", # Vespinae. Lopez-Osorio et al. 2014. MPE
               "1988_4074", # Mantodea. Svenson et al. 2009. CLadistics
               "2593_6247", # Dermaptera. Kocarek et al. 2013. PLoS ONE
               "1563_6170", # Hymenoptera. Sharkey et al. 2011. Cladistics
               "1849_3731", # Formicidae. Brady et al. 2006. PNAS
               "2664_6201", # Ditrysia. Regier et al. 2013. PLoS ONE *** prefer this over Cho et al. 2011
               "1776_3581", # Ditrysia. Cho et al. 2011. Syst. Biol.
               "1337_6167", # Holometabola (insect). Wiegmann et al. 2009. BMC Evol. Biol. *** mapping to Endopterygota
               "2629_6162", # Hexapoda. Letsch and Simon. 2013. Syst. Ent.
               "2604_6043", # Apoidea. Hedtke et al. 2013. BMC Evol. Biol.
               "437_6242",  # Diptera. Wiegmann et al. 2011. PNAS
               "2594_6014", # Diptera. Lambkin et al. 2013. Syst. Ent.
               "1338_2666", # Pterygota. Simon et al. 2009. MBE
               "2068_6488", # Siboglinidae. Rouse et al. 2004. Science
               "2092_4335", # Alopiinae. de Weerd and Gittenberger. 2005. Zool. J. Linn. Soc.
               "2156_5953", # Dorvilleidae. Wiklund et al. 2009. Zootaxa

     ## Other
               "2709_6290", # Demospongiae. Redmond et al. 2013. Int. Comp. Biol.
               "2842_6603", # Thecostraca. Perez-Losada et al. 2009. BMC Biol.
               "2708_6289", # Cnidaria. Kayal et al. 2013. BMC Evol. Biol.
               "1343_6255", # Hexactinella. Dohrmann et al. 2009. MPE
               "1788_6534", # Siphonophora. Dunn et al. 2005. Syst. Biol.
               "1786_6257", # Hydrozoa. Cartwright et al. 2008. J. Marine Biol. Assoc. UK
               "2678_6224", # Echinodermata. Janies et al. 2011. Syst. Biol.
               "421_523",   # Mollusca. Smith et al. 2011. Nature
               "1366_6166", # Annelida. Struck et al. 2011. Nature *** mapping to Lophotrochozoa
               "1761_6151", # Scleractinia (corals). Huang nad Roy. 2013. Ecology and Evolution
               "2710_6291", # Metazoa. Ryan et al. 2013. Science *** need to choose best Metazoa tree(s) 

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


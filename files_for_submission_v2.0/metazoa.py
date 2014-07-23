"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
     ## Birds
               "pg_2926_6757", # Palaeognaths. Mitchell et al. 2014. Science
               "pg_1764_6299", # Pelicanidae. Kennedy et al. 2013. MPE
               "pg_2924_6755", # Emberizinae. Klicka et al. 2014. MPE
               "pg_2876_6670", # Tinamidae. Bertelli, Sara, Ana Luz Porzecanski
               "pg_2875_6668", # Oriolidae. Jonsson et al. 2010. Ecography
               "pg_2874_6667", # Carpodacus. Tietze et al. 2013. Zool. J. Linn. Soc.
               "pg_2873_6666", # Certhia. Tietze et al. 2006. Ibis
               "pg_2332_4912", # Sylviidae. Voelker and Light. 2011. BMC Evol. Biol. *** Pseudoalcippe should be in the family Silviidae rather than Timaliidae
               "pg_1854_3743", # Troglodytinae. Mann et al. 2006. MPE
               "pg_1586_3208", # Timaliidae. Moyle et al. 2012. Syst. Biol.
               "pg_2858_6642", # Turdidae. Nylander et al. 2008. Syst. Biol.
               "pg_2829_6579", # Thraupidae. Burns et al. 2014. MPE
               "pg_1953_3977", # Furnariidae. Derryberry et al. 2011. Evolution
               "pg_2872_6665", # Caprimuligidae. Han et al. MPE
               "pg_1872_3780", # Gruiformes. Fain et al 2007. MPE
               "pg_2869_6661", # Bucerotiformes. Gonzalez et al. 2013. MPE
               "pg_2870_6662", # Falconidae. Fuchs et al. 2011. MPE
               "pg_2871_6663", # Falconidae. Fuchs et al. 2012. Ibis
               "pg_2864_6651", # Platalea. Chesser et al. 2010. Zootaxa
               "pg_2845_6606", # Sitta. Pasquet et al. 2014. J. Ornith.
               "pg_2806_6529", # Psittaciformes. Joseph et al. 2011. MPE
               "pg_2805_6512", # Psittaciformes. Wright et al. 2008. MBE
               "pg_1979_6300", # Psittacidae. Tavares et al. 2006. Syst. Biol.
               "pg_2857_6628", # Gyps. Arshad et al. 2009. J. Ornith.
               "pg_1887_6629", # Accipitridae. Lerner et al. 2008. Auk
               "pg_2850_6620", # Columbidae. Cibois et al. 2014. MPE
               "pg_2444_6526", # Columbiformes. Pereira et al. 2007. Syst. Biol.
               "pg_2798_6497", # Spheniscidae. Subramanian et al. 2013. Biol. Lett.
               "pg_2866_6656", # Anseriformes. Gonzalez et al. 2009. J. Zool.
               "pg_2860_6646", # Anatidae. Fulton et al. 2012. Proc. Roy. Soc.
               "pg_2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE
               "pg_2865_6654", # Cynanthus. Garcia-Deras et al. 2008. Zootaxa.
               "pg_2853_6624", # Trochilidae. McGuire et al. 2014. Curr. Biol. *** Replaces McGuire et al. 2007. Syst. Biol.
               "pg_2796_6491", # Pipridae. Ohlson et al. 2013. MPE
               "pg_2707_6281", # Icteridae. Powell et al. 2013. MPE *** Hypopyrrhus not mapped to Icteridae
               "pg_1966_4019", # Maluridae. Lee et al. 2011. Syst. Biol.
               "pg_2600_6022", # Paridae. Johansson et al. 2013. MPE
               "pg_2599_6021", # Alaudidae (larks). Alstrom et al. 2013. MPE
               "pg_2591_6008", # Parulidae (warblers). Lovette et al. 2008. MPE
               "pg_2454_5247", # Thamnophilus. Brumfield and Edwards. 2007. Evolution
               "pg_2692_6245", # Fringillidae. Zuccon et al. 2012. MPE
               "pg_2702_6274", # core Corvoidea. Aggerbeck et al. 2014. MPE *** mapping back to Passeroidea
               "pg_2575_5974", # Passeriformes. Barker et al. 2013. Syst. Biol.
               "pg_2015_4152", # Passeriformes. Odeen et al. 2011. Evolution
               "pg_2913_6742", # Himilayan songbirds. Price et al. 2014. Nature
               "pg_420_522",   # Aves. Hackett et al. 2008. Science

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

     ## Fish - need to figure out best ordering with mapcompat
               "ot_96_1",      # Cottoidea. Smith and Busby. 2014. MPE
               "pg_2589_6001", # Gobioidei. Agorreta et al. 2013. MPE
               "pg_2655_6181", # Cichlidae. Friedman et al. 2013. Proc. Roy. Soc.
               "pg_1997_6183", # Percidae. Near et al. 2011. Syst. Biol. *** not working for some reason...
               "pg_2654_6179", # Leiognathidae. Chakrabarty et al. 2011. Mol. Ecol.
               "pg_2585_5994", # Tetraodontiformes. Santini et al. 2013. MPE
               "pg_2653_6178", # Percomorpha. Miya et al. 2013. PLoS ONE *** prefer this over Near et al. 2012
               "pg_2657_6191", # Percomorpha. Near et al. 2012. MPE
               "pg_2551_6180", # Holacanthopterygii. Wainwright et al. 2012. Syst. Biol.
               "pg_2576_5975", # Euteleostei. Near et al. 2013. PNAS
               "pg_1870_3769", # Cyprinidae. Ruber et al. 2007. BMC Evol. Biol.
               "pg_2659_6195", # Otophysi. Chen et al. 2013. Evolution

     ## Other tetrapods
               "pg_2881_6680", # Anolis. Mahler et al. 2013. Science
               "pg_2143_4505", # Kentropyx. Collevatti et al. 2008. Mol. Ecol.
               "pg_2098_6487", # Stenocercus. Torres-Carvajal et al. 2005. MPE
               "pg_2851_6621", # Kinosternidae. Spinks at al. 2014. MPE
               "pg_2415_5096", # Turtles. Guillon et al. 2012. Contributions to Zoology
               "pg_423_2857",  # Amphibia. Pyron and Weins. 2011. MPE
               "pg_2573_5959", # Sauria. Crawford et al. 2012. Biology Letters
               "pg_2711_6295", # Henophidia. Reynolds et al. 2014. MPE *** check this doesn't break the Pyron study
               "pg_2460_5285", # Squamata. Pyron et al. 2013. BMC Evol. Biol. -- Anolis nonmonophyly

     ## Decapoda
               "pg_1252_2661", # maps to: Anomura
               "pg_1336_2660", # maps to: Brachyura
               "pg_1948_6513", # maps to: Anomura
               "pg_1796_6514", # maps to: Typhlatya
               "pg_2243_6515", # maps to: Paramunida
               "pg_2670_6214", # maps to: Atyidae
               "pg_2671_6216", # maps to: Caridina
               "pg_2673_6219", # maps to: Astacidea
               "pg_2674_6220", # maps to: Cambaridae
               "pg_2675_6221", # maps to: Cambaridae
               "pg_2676_6222", # maps to: Scyllaridae
               "pg_2677_6223", # maps to: Anomura
               "pg_2682_6227", # maps to: Decapoda
               "pg_2683_6228", # maps to: Dendrobranchiata
               "pg_2807_6519", # maps to: Alpheidae
               "pg_2808_6522", # maps to: Alpheoidea
               "pg_2667_6211", # maps to: Galatheoidea

     ## Insects and other crawley stuff
               "pg_251_134",   # Formicidae. Moreau et al. 2006. Science
               "pg_2405_6669", # Phyllodocidae. Eklof et al. 2007. MPE
               "pg_2614_6121", # Nicrophorus. Sikes and Venables. 2013.
               "pg_2628_6143", # Sarcophaga. Whitmore et al. 2013. Zool. J. Linn. Soc.
               "pg_2838_6594", # Pleocyemata. Bracken-Grissom et al. 2014. Syst. Biol.
               "pg_2357_6538", # Evaniscus. Mullins et al. 2012. ZooKeys <- 2 new species are not in OTT
               "pg_2323_6537", # Bombyliidae. Lambkin and Bartlett. 2011. ZooKeys <- check sampling
               "pg_1940_3943", # Drosophilidae. Van der Linde et al. 2010. Genet. Res.
               "pg_2581_5987", # Membracidae. Cryan et al. 2004. Syst. Ent.
               "pg_2087_4323", # Austrogoniodes. Banks and Paterson. 2004. Invert. Syst.
               "pg_2811_6533", # Vespinae. Lopez-Osorio et al. 2014. MPE
               "pg_1988_4074", # Mantodea. Svenson et al. 2009. CLadistics
               "pg_2593_6247", # Dermaptera. Kocarek et al. 2013. PLoS ONE
               "pg_1563_6170", # Hymenoptera. Sharkey et al. 2011. Cladistics
               "pg_1849_3731", # Formicidae. Brady et al. 2006. PNAS
               "pg_2664_6201", # Ditrysia. Regier et al. 2013. PLoS ONE *** prefer this over Cho et al. 2011
               "pg_1776_3581", # Ditrysia. Cho et al. 2011. Syst. Biol.
               "pg_1337_6167", # Holometabola (insect). Wiegmann et al. 2009. BMC Evol. Biol. *** mapping to Endopterygota
               "pg_2629_6162", # Hexapoda. Letsch and Simon. 2013. Syst. Ent.
               "pg_2604_6043", # Apoidea. Hedtke et al. 2013. BMC Evol. Biol.
               "pg_437_6242",  # Diptera. Wiegmann et al. 2011. PNAS
               "pg_2594_6014", # Diptera. Lambkin et al. 2013. Syst. Ent.
               "pg_1338_2666", # Pterygota. Simon et al. 2009. MBE
               "pg_2068_6488", # Siboglinidae. Rouse et al. 2004. Science
               "pg_2092_4335", # Alopiinae. de Weerd and Gittenberger. 2005. Zool. J. Linn. Soc.
               "pg_2156_5953", # Dorvilleidae. Wiklund et al. 2009. Zootaxa
               "ot_41_1",      # Lepidoptera. Kawahara and Breinholt. 2014. Proc. Roy. Soc.

     ## Other
               "pg_2544_6482", # Hexactinellida. Dohrmann et al. 2008. Syst. Biol.
               "pg_2696_6249", # Demospongiae. Hill et al. 2013. PLoS ONE
               "pg_2709_6290", # Demospongiae. Redmond et al. 2013. Int. Comp. Biol.
               "pg_2842_6603", # Thecostraca. Perez-Losada et al. 2009. BMC Biol.
               "pg_2708_6289", # Cnidaria. Kayal et al. 2013. BMC Evol. Biol.
               "pg_1343_6255", # Hexactinella. Dohrmann et al. 2009. MPE
               "pg_1788_6534", # Siphonophora. Dunn et al. 2005. Syst. Biol.
               "pg_1786_6257", # Hydrozoa. Cartwright et al. 2008. J. Marine Biol. Assoc. UK
               "pg_2678_6224", # Echinodermata. Janies et al. 2011. Syst. Biol.
               "pg_421_523",   # Mollusca. Smith et al. 2011. Nature
               "pg_1366_6166", # Annelida. Struck et al. 2011. Nature *** mapping to Lophotrochozoa
               "pg_1761_6151", # Scleractinia (corals). Huang nad Roy. 2013. Ecology and Evolution
               "pg_2710_6291", # Metazoa. Ryan et al. 2013. Science *** need to choose best Metazoa tree(s) 

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


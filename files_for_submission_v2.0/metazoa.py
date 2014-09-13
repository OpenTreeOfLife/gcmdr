"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
     ## Birds

    ## Galliformes
               "ot_119_1",     # Cracidae. Pereira et al. 2002. Syst. Biol.
               "ot_118_1",     # Megapodidae. Harris et al. 2014. J. Biogeo.
               "pg_2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE

    ## Anseriformes
               "pg_2866_6656", # Anseriformes. Gonzalez et al. 2009. J. Zool.
               "pg_2860_6646", # Anatidae. Fulton et al. 2012. Proc. Roy. Soc.

               "ot_116_1",     # Strigiformes. Hugall and Stuart-Fox. 2012. Nature # can fill this out more

               #"ot_121_2",     # Couinae. Payne. 2005. Book
               #"ot_121_1",     # Cuculiformes. Payne. 2005. Book
               "ot_121_7",     # Cuculiformes. Payne. 2005. Book. combined from above

               "pg_2876_6670", # Tinamidae. Bertelli et al. 2004. Orn. Neotrop.
               "pg_2926_6757", # Palaeognaths. Mitchell et al. 2014. Science

               "pg_1764_6299", # Pelicanidae. Kennedy et al. 2013. MPE
               "ot_137_1",     # Sulidae. Patterson et al. 2011. MPE
               "ot_140_1",     # Phalacrocoracidae. Kenedy and Spencer. 2014. MPE
               "pg_2798_6497", # Spheniscidae. Subramanian et al. 2013. Biol. Lett.
               "ot_104_1",     # Gavia. Boertmann. 1990. Steenstrupia
               "ot_142_1",     # Diomedeidae. Chambers et al. 2009. Notornis
               "ot_138_1",     # Ciconiidae. Slikas. 1997. MPE
               "pg_2864_6651", # Platalea. Chesser et al. 2010. Zootaxa
               "ot_139_1",     # Threskiornithidae. Ramirez et al. 2013. Gen. Mol. Res.
               "pg_1872_3780", # Gruiformes. Fain et al 2007. MPE
               "ot_125_1",     # Psophia. Ribas et al. 2011. Proc. Roy. Soc.

               "pg_2869_6661", # Bucerotiformes. Gonzalez et al. 2013. MPE

               "ot_112_1",     # Apodidae. Packert et al. 2012. MPE
               "pg_2853_6624", # Trochilidae. McGuire et al. 2014. Curr. Biol.
               "ot_123_1",     # Aegotheles. Dumbacher. 2003. MPE
               "pg_2872_6665", # Caprimuligidae. Han et al. MPE # can do better than this one

               "ot_122_1",     # Phoenicopteriformes. Torres et al. 2014. BMC Evol. Biol.
               "ot_124_1",     # Otididae. Pitra et al. 2002. MPE
               "ot_129_1",     # Musophagidae. Njabo and Sorenson. 2009. Ostrich
               "ot_147_1",     # Trogonidae. Ornelas et al. 2009. J. Evol. Biol.
               "ot_148_1",     # Meropidae. Marks et al. 2007. MPE
               "ot_149_4",     # Todidae. Overton et al. 2004. MPE

    ## Piciformes
               "ot_150_3",     # Megalaimidae. den Tex and Leonard. 2013. MPE
               "ot_156_1",     # barbets. Moyle. 2004. MPE
               "ot_153_1",     # Pteroglossus. Patel et al. 2011. MPE
               "ot_151_1",     # Capito. Armenta et al. 2005. Condor
               "ot_154_1",     # Andigena+Selenidera. Lutz et al. 2013. MPE
               "ot_155_1",     # Aulacorhynchus. Bonaccorso et al. 2011. Zool. Scripta
               "ot_152_1",     # Ramphastos. Patane et al. 2009. MPE
               "ot_157_1",     # Celeus. Benz and Robbins. 2011. MPE
               "ot_158_1",     # Colaptes. Moore et al. 2011. MPE
               "ot_159_1",     # Picidae. Benz et al. 2006. MPE 

    ## Charadriiformes
               "ot_144_1",     # Alcidae. Pereira and Baker. 2008. MPE
               "ot_136_1",     # Jacanidae. Whittingham et al. 2000. Auk

    ## Accipitriformes
               "pg_2857_6628", # Gyps. Arshad et al. 2009. J. Ornith.
               "pg_1887_6629", # Accipitridae. Lerner et al. 2008. Auk

    ## Columbiformes
               "pg_2850_6620", # Columbidae. Cibois et al. 2014. MPE
               "pg_2444_6526", # Columbiformes. Pereira et al. 2007. Syst. Biol.

    ## Falconidae
               "pg_2870_6662", # Falconidae. Fuchs et al. 2011. MPE
               "pg_2871_6663", # Falconidae. Fuchs et al. 2012. Ibis

    ## Psittaciformes
               "ot_166_1",     # Androglossini. Quintero et al. 2012. Zool. Scripta
               "ot_161_1",     # Amazona. Russello and Amato. 2004. MPE
               "ot_160_1",     # Cacatuidae. White et al. 2011. MPE
               "pg_1979_6300", # Psittacidae. Tavares et al. 2006. Syst. Biol.
               "pg_2805_6512", # Psittaciformes. Wright et al. 2008. MBE
               "ot_162_1",     # Prioniturus. Schweizer et al. 2012. J. Zool. Syst. Evol. Res.
               "ot_164_1",     # Brotogeris. Ribas et al. 2009. J. Biogeo.
               "ot_165_1",     # Forpus. Smith et al. 2012. Mol. Ecol.
               "ot_167_1",     # Pyrrhura. Ribas et al. 2006. Auk



    ## Temp Passeriformes. Ordering is a big factor here as the higher taxonomy is out of date (i.e. incompatible with new studies)
               "ot_170_1",     # Regulus. Packert et al. 2009. J. Ornith.
               "ot_102_1",     # Pheucticus. Pulgarin-R et al. 2013. MPE
               "ot_174_1",     # Rhipidura. Nyari et al. 2009. Zool. Scripta
               "ot_110_1",     # Oenanthe. Schweizer and Shirihai. 2013. MPE
               "pg_2845_6606", # Sitta. Pasquet et al. 2014. J. Ornith.
               "ot_172_1",     # Certhia. Packert et al. 2011. J. Biogeo.
               "pg_2454_5247", # Thamnophilus. Brumfield and Edwards. 2007. Evolution
               "ot_172_2",     # Pinicola+Pyrrhula. Packert et al. 2011. J. Biogeo.

               "ot_173_1",     # chickadees. Harris et al. 2014. Evolution
               "pg_2600_6022", # Paridae. Johansson et al. 2013. MPE

               "ot_176_1",     # Tachycineta. Cerasale et al. 2012. MPE
               "ot_177_1",     # Hirundo. Dor et al. 2010. MPE
               "ot_178_1",     # Hirundinidae. Sheldon et al. 2005. MPE
               "pg_2591_6024", # Parulidae. Lovette et al. 2008. MPE
               "pg_2599_6021", # Alaudidae. Alstrom et al. 2013. MPE
               "pg_1966_4019", # Maluridae. Lee et al. 2011. Syst. Biol.
               "pg_2875_6668", # Oriolidae. Jonsson et al. 2010. Ecography
               "pg_2707_6281", # Icteridae. Powell et al. 2013. MPE *** Hypopyrrhus not mapped to Icteridae. currently unmapped


# *** Important to get these in: ***
#               "pg_2829_6579", # Thraupidae. Burns et al. 2014. MPE
#               "pg_2924_6755", # Emberizinae. Klicka et al. 2014. MPE


# The following studies are good, but don't agree with Barker et al. 2004
#               "ot_171_1",     # Bombycillidae. Spellman et al. 2008. MPE
#               "pg_2858_6642", # Turdidae. Nylander et al. 2008. Syst. Biol.
#               "pg_1854_3743", # Troglodytinae. Mann et al. 2006. MPE
#               "pg_1953_3977", # Furnariidae. Derryberry et al. 2011. Evolution
#               "pg_2890_6701", # Formicariidae. Rice. 2005. Auk
#               "ot_103_4",     # Acrocephalinae. Arbabi et al. 2014. MPE
#               "pg_1586_3208", # Timaliidae. Moyle et al. 2012. Syst. Biol.
#               "pg_2332_4912", # Sylviidae. Voelker and Light. 2011. BMC Evol. Biol. *** Pseudoalcippe should be in Silviidae rather than Timaliidae
#               "pg_2796_6491", # Pipridae. Ohlson et al. 2013. MPE
#               "pg_2692_6245", # Fringillidae. Zuccon et al. 2012. MPE
#               "ot_101_1",     # Saltator. Chaves et al. 2013. J. Biogeo. *** Includes Saltatricula (Thraupini), while Saltator is Cardinalini

# Others
#               "pg_2874_6667", # Carpodacus. Tietze et al. 2013. Zool. J. Linn. Soc. * not monophyletic
#               "pg_2865_6654", # Cynanthus. Garcia-Deras et al. 2008. Zootaxa. *** monophyly rejected by pg_2853_6624


# big kahuna (for now)
               "pg_2404_5068", # Passeriformes. Barker et al. 2004. PNAS

# Other deep-level Passeriformes
#               "pg_2702_6274", # core Corvoidea. Aggerbeck et al. 2014. MPE *** mapping back to Passeroidea
#               "pg_2575_5974", # Passeriformes. Barker et al. 2013. Syst. Biol.
#               "pg_2015_4152", # Passeriformes. Odeen et al. 2011. Evolution
#               "pg_2913_6742", # Himilayan songbirds. Price et al. 2014. Nature


# Aves
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

     ## Fish - need to figure out best ordering with mapcompat
               #"ot_96_1",      # Cottoidea. Smith and Busby. 2014. MPE
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
               "ot_181_2",     # Selachii (sharks). Velez-Zuazo and Agnarsson. 2011. MPE

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
 "pg_2838_6594", # Pleocyemata. Bracken-Grissom et al. 2014. Syst. Biol. *** maps back to Decapoda ***


     ## Hemiptera
 #              "pg_2581_5987", # Membracidae. Cryan et al. 2004. Syst. Ent. # broken now for some reason?!?


     ## Neoptera
               "pg_2087_4323", # Austrogoniodes. Banks and Paterson. 2004. Invert. Syst.
               "pg_1988_4074", # Mantodea. Svenson et al. 2009. CLadistics
               "pg_2593_6247", # Dermaptera. Kocarek et al. 2013. PLoS ONE


     ## Coleoptera
               "pg_2614_6121", # Nicrophorus. Sikes and Venables. 2013.


     ## Diptera
               "pg_2628_6143", # Sarcophaga. Whitmore et al. 2013. Zool. J. Linn. Soc. ** map more **
               "pg_2323_6537", # Bombyliidae. Lambkin and Bartlett. 2011. ZooKeys <- check sampling
               "pg_1940_3943", # Drosophilidae. Van der Linde et al. 2010. Genet. Res.
               "pg_437_6242",  # Diptera. Wiegmann et al. 2011. PNAS
               "pg_2594_6014", # Diptera. Lambkin et al. 2013. Syst. Ent.


     ## Hymenoptera
               "pg_2357_6538", # Evaniscus. Mullins et al. 2012. ZooKeys <- 2 new species are not in OTT
               "pg_251_134",   # Formicidae. Moreau et al. 2006. Science
               "pg_1849_3731", # Formicidae. Brady et al. 2006. PNAS
               "pg_2811_6533", # Vespinae. Lopez-Osorio et al. 2014. MPE
               "pg_2604_6043", # Apoidea. Hedtke et al. 2013. BMC Evol. Biol.
               "pg_1563_6170", # Hymenoptera. Sharkey et al. 2011. Cladistics


     ## Lepidoptera
               "pg_2664_6201", # Ditrysia. Regier et al. 2013. PLoS ONE *** prefer this over Cho et al. 2011
               "pg_1776_3581", # Ditrysia. Cho et al. 2011. Syst. Biol.
               "ot_185_1",     # Lepidoptera. Kawahara and Breinholt. 2014. Proc. Roy. Soc.


     ## Other Insects
               "pg_1337_6167", # Endopterygota (insect). Wiegmann et al. 2009. BMC Evol. Biol.
               "pg_2629_6162", # Hexapoda. Letsch and Simon. 2013. Syst. Ent.
               "pg_2156_5953", # Dorvilleidae. Wiklund et al. 2009. Zootaxa
               "pg_1338_2666", # Pterygota. Simon et al. 2009. MBE


     ## Nematodes
               "pg_2422_5117", # Ascaridoidea. Nadler and Hudspeth. 1998. MPE
               "ot_182_1",     # Nematoda. Blaxter et al. 1998. Nature
               "ot_183_2",     # Nematoda. Sultana et al. 2013. BMC Evol. Biol.
               "pg_2061_4245", # Nematoda. Mullin et al. 2003. Nematology

     ## Annelida
               "pg_2068_6488", # Siboglinidae. Rouse et al. 2004. Science
               "pg_2405_6669", # Phyllodocidae. Eklof et al. 2007. MPE
               "pg_1366_6166", # Annelida. Struck et al. 2011. Nature


     ## Gastropoda
               "pg_2092_4335", # Alopiinae. de Weerd and Gittenberger. 2005. Zool. J. Linn. Soc.



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
               "pg_1761_6151", # Scleractinia (corals). Huang nad Roy. 2013. Ecology and Evolution
               "pg_2710_6291" # Metazoa. Ryan et al. 2013. Science *** need to choose best Metazoa tree(s) 

            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "___main__":
    import load_synth_extract
    #from wopr_conf import *
    from stephen_desktop_conf import *

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


"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
     ## Birds
               "pg_2890_6701", # Formicariidae. Rice. 2005. Auk
               "ot_104_1",     # Gavia. Boertmann. 1990. Steenstrupia
               "ot_103_4",     # Acrocephalinae. Arbabi et al. 2014. MPE
               "ot_102_1",     # Pheucticus. Pulgarin-R et al. 2013. MPE
               "ot_101_1",     # Saltator. Chaves et al. 2013. J. Biogeo. *** Includes Saltatricula (Thraupini), while Saltator is Cardinalini
               
               "pg_2926_6757", # Palaeognaths. Mitchell et al. 2014. Science
               "pg_1764_6299", # Pelicanidae. Kennedy et al. 2013. MPE
               "pg_2924_6755", # Emberizinae. Klicka et al. 2014. MPE
               "pg_2876_6670", # Tinamidae. Bertelli, Sara, Ana Luz Porzecanski
               "pg_2875_6668", # Oriolidae. Jonsson et al. 2010. Ecography
               "pg_2874_6667", # Carpodacus. Tietze et al. 2013. Zool. J. Linn. Soc.
               "pg_2873_6666", # Certhia. Tietze et al. 2006. Ibis
               "pg_2332_4912", # Sylviidae. Voelker and Light. 2011. BMC Evol. Biol. *** Pseudoalcippe should be in Silviidae rather than Timaliidae
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
            ]

studytreelistTF = [True] * len(studytreelist)


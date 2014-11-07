"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
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
               
     ## Crustacea
               "pg_2842_6603", # Thecostraca. Perez-Losada et al. 2009. BMC Biol.
               
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

     ## Other Arthropods
               "pg_1337_6167", # Endopterygota (insect). Wiegmann et al. 2009. BMC Evol. Biol.
               "pg_2629_6162", # Hexapoda. Letsch and Simon. 2013. Syst. Ent.
               "pg_1338_2666" # Pterygota. Simon et al. 2009. MBE
               
            ]

studytreelistTF = [True] * len(studytreelist)


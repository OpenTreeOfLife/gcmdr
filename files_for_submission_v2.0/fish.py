"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
     ## Actinopterygii - need to figure out best ordering with mapcompat
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
               "pg_2659_6195" # Otophysi. Chen et al. 2013. Evolution
            ]

studytreelistTF = [True] * len(studytreelist)



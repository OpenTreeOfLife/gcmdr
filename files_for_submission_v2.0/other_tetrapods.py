"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
     ## Other tetrapods
               "pg_2881_6680", # Anolis. Mahler et al. 2013. Science
               "pg_2143_4505", # Kentropyx. Collevatti et al. 2008. Mol. Ecol.
               "pg_2098_6487", # Stenocercus. Torres-Carvajal et al. 2005. MPE
               "pg_2851_6621", # Kinosternidae. Spinks at al. 2014. MPE
               "pg_2415_5096", # Turtles. Guillon et al. 2012. Contributions to Zoology
               "pg_423_2857",  # Amphibia. Pyron and Weins. 2011. MPE
               "pg_2573_5959", # Sauria. Crawford et al. 2012. Biology Letters
               "pg_2711_6295", # Henophidia. Reynolds et al. 2014. MPE *** check this doesn't break the Pyron study
               "pg_2460_5285" # Squamata. Pyron et al. 2013. BMC Evol. Biol. -- Anolis nonmonophyly

            ]

studytreelistTF = [True] * len(studytreelist)



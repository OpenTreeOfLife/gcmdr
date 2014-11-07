"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""

# these are either 1) too broad in scope or 2) too isolated to be included with other groups.

studytreelist=[
               "ot_181_2",     # Selachii (sharks). Velez-Zuazo and Agnarsson. 2011. MPE
               "pg_2092_4335", # Alopiinae. de Weerd and Gittenberger. 2005. Zool. J. Linn. Soc.
               "pg_2678_6224", # Echinodermata. Janies et al. 2011. Syst. Biol.
               "pg_421_523",   # Mollusca. Smith et al. 2011. Nature
               "pg_2710_6291"  # Metazoa. Ryan et al. 2013. Science *** need to choose best Metazoa tree(s) 
            ]

studytreelistTF = [True] * len(studytreelist)

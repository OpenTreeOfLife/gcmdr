"""
Note: studies are (for the most part) ordered from shallow to deep clades. 
      This might need to be reversed when using the mapcompatible function.
"""


studytreelist=[
## Bacteria + Archaea
               "pg_2542_5590", # Bacteria + Archaea. Lang et al. 2013. PLoS ONE

## Bacteria
               "pg_263_149",   # Thermotogaceae. Swithers et al. 2012. GBE
               "pg_2753_6360", # Enterobacteriaceae. Husnk et al. 2011. BMC Biol.
               "pg_2757_6369", # Proteobacteria. Sachs et al. 2013. Proc. Roy. Soc.
               
## Amoebozoa
               "pg_2556_5586", # Myxogastria. Fiore-donno et al. 2010. J. Euk. Microbiol.
               "pg_2484_6607", # Amoebozoa. Lahr et al. 2011. PLoS ONE
               
## Eukaryota
               "pg_2553_5579", # Euglenophyceae. Nudelman et al. 2003. J. Phycology
               "pg_312_264",   # Excavata. Takishita et al. 2011. Protist
               "pg_313_6681",  # Stramenopiles. Grant et al. 2009. Protist
               "pg_2822_6569",  # Eukaryota. Parfrey et al. 2011. PNAS
               
## Chromalveolata
               "pg_2742_6342", # Dinophyceae. Gomez et al. 2009. Protist
               "pg_2849_6615" # Amphora. Sato. 2013. Phycologia
            ]

studytreelistTF = [True] * len(studytreelist)



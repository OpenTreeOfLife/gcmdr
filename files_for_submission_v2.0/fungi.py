"""
This includes the studies and the ottolid
"""
import load_synth_extract


studytreelist=["pg_2818_6563", # Fungi. Hibbett 2007
               "pg_240_123",   # Pezizomycotina
               "pg_827_1585",  # Blastocladiomycota
               "pg_1144_5800", # Entomophthoromycota
               "pg_439_5514",  # Glomeromycota
               #"238_110",  # Ascomycota	<- mapped back to Eukaryota
               "pg_1197_5822", # Fungi
               "pg_2701_6271", # Dikarya	<- mapped back to Basidiomycota
               "pg_1162_5805"  #Fungi
               ]
 
"""
studytreelist=["1162_5805",
               "1682_5491",
               "1665_5483",
               "1754_5492",
               "1692_3412",
               "1075_2094",
               "1079_5502",
               "1736_3492",
               "1737_3493",
               "736_1330",
               "1191_5507",
               "775_1445",
               "735_1328",
               "734_1325",
               "955_1877",
               "877_5506",
               "434_548",
               "744_5510",
               "439_5514",
               "1142_5799",
               #"238_109"
               ]
"""

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
    from stephen_laptop_conf import *
    import general_tm_utils
    
    synthottolid="352914"

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)    

    load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)

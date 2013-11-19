"""
This includes the studies and the ottolid
"""
import load_synth_extract


studytreelist=["240_123",#Pezizomycotina
               "827_1585",#Blastocladiomycota
               "1144_5800",#Entomophthoromycota
               "439_5514",#Glomeromycota
               "238_110",#Ascomycota
               "2701_6271",#Dikarya
               "1197_5822",#Fungi
               "1162_5805"#Fungi
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

if __name__ == "__main__":
	from stephen_desktop_conf import *

	
	synthottolid="352914"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn)

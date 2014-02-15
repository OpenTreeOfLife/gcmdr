"""
this is the stuff specific to the studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

from wopr_conf import *

## for testing synthesis:
#from goo import studytreelist as goolist
#from mammals import studytreelist as mammalslist
#from birds import studytreelist as birdslist
#from tetrapoda import studytreelist as tetrapodalist

## for serious synthesis:
#from plants import studytreelist as plantslist
#from metazoa import studytreelist as metalist
#from fungi import studytreelist as fungilist
#from microbes import studytreelist as microbelist
#from decapods import studytreelist as decapodlist

studytreelist = []
#studytreelist.extend(goolist)
#studytreelist.extend(mammalslist)
#studytreelist.extend(birdslist)
#studytreelist.extend(tetrapodalist)

#studytreelist.extend(plantslist)
#studytreelist.extend(metalist)
#studytreelist.extend(fungilist)
#studytreelist.extend(microbelist)
#studytreelist.extend(decapodlist)

import load_synth_extract

# 805080 = life; 691846 = Metazoa; 81461 = Aves; 244265 = Mammalia; 229562 = Tetrapoda; Amniota = 229560; Archosauria = 335588; 304358 = Eukaryota; Decapoda = 169205

#synthottolid = "805080"
#extractottolid = "691846"
synthottolid = "169205"

# should mapcompat be used?
studytreelistTF = [True] * len(studytreelist)
#studytreelistTF = [False] * len(studytreelist)

# reverse the list. may or may not be wanted. to consider: load in one order (for compatability), prefer in opposite.
#studytreelist.reverse()

print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

# analysis name
#aname="Life_(Plants+Metazoa)_test_2.4draft17_mapcompat"
aname="Decapoda_OTT2.4draft17_taxonomy-only"
# location of synth database
dsynth=bdir+aname+".db"
# location of synth treefile
treefn=bdir+aname+"-synth.tre"

#load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,extractottolid)
load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


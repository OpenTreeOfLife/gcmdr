"""
this is the stuff specific to the studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

from wopr_conf import *

from birds import studytreelist as birdslist

studytreelist = []
studytreelist.extend(birdslist)

import load_synth_extract

# 805080 = life; 691846 = Metazoa; 81461 = Aves; 244265 = Mammalia;
# 229562 = Tetrapoda; Amniota = 229560; Archosauria = 335588; 304358 = Eukaryota; Decapoda = 169205;
# 93302 = cellular organisms;

synthottolid = "691846"
#extractottolid = "691846"
#synthottolid = "691846"

# should mapcompat be used?
studytreelistTF = [True] * len(studytreelist)
#studytreelistTF = [False] * len(studytreelist)

# reverse the list. may or may not be wanted. to consider: load in one order (for compatability), prefer in opposite.
#studytreelist.reverse()

print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

# analysis name
aname="Birds_v2.6_mapcompat_13April_5"
# location of synth database
dsynth=bdir+aname+".db"
# location of synth treefile
treefn=bdir+aname+"-synth.tre"

#load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,extractottolid)
load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


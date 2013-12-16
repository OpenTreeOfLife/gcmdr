"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

from wopr_conf import *

#from plants import studytreelist as plantslist
#from goo import studytreelist as goolist
from metazoa import studytreelist as metalist
#from mammals import studytreelist as mammalslist
#from birds import studytreelist as birdslist
#from tetrapoda import studytreelist as tetrapodalist
#from fungi import studytreelist as fungilist


studytreelist = []
#studytreelist.extend(plantslist)
#studytreelist.extend(goolist)
studytreelist.extend(metalist)
#studytreelist.extend(mammalslist)
#studytreelist.extend(birdslist)
#studytreelist.extend(tetrapodalist)
#studytreelist.extend(fungilist)

import load_synth_extract

# 805080 = life; 691846 = Metazoa; 81461 = Aves; 244265 = Mammalia; 229562 = Tetrapoda
#synthottolid="805080"
#extractottolid="691846"

synthottolid = "691846"
#extractottolid = "691846"

studytreelistTF = [True] * len(studytreelist)

print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

# analysis name
aname="Metazoa_test_2.3_mapcompat"
# location of synth database
dsynth=bdir+aname+".db"
# location of synth treefile
treefn=bdir+aname+"-synth.tre"

#load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,extractottolid)
load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


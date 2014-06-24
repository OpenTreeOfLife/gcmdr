"""
this is the stuff specific to the studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

from wopr_conf import *

## for testing synthesis:
#from goo import studytreelist as goolist
#from mammals import studytreelist as mammalslist
#from birds import studytreelist as birdslist
#from tetrapoda import studytreelist as tetrapodalist
#from decapods import studytreelist as decapodlist

## for serious synthesis:
from plants import studytreelist as plantslist
from metazoa import studytreelist as metalist
from fungi import studytreelist as fungilist
from microbes import studytreelist as microbelist

studytreelist = []
#studytreelist.extend(goolist)
#studytreelist.extend(mammalslist)
#studytreelist.extend(birdslist)
#studytreelist.extend(tetrapodalist)
#studytreelist.extend(decapodlist)

studytreelist.extend(plantslist)
studytreelist.extend(metalist)
studytreelist.extend(fungilist)
studytreelist.extend(microbelist)

import load_synth_extract

# 805080 = life; 691846 = Metazoa; 81461 = Aves; 244265 = Mammalia;
# 229562 = Tetrapoda; Amniota = 229560; Archosauria = 335588; 304358 = Eukaryota; Decapoda = 169205;
# 93302 = cellular organisms;

synthottolid = "93302"
#extractottolid = "691846"
#synthottolid = "691846"

# should mapcompat be used?
studytreelistTF = [True] * len(studytreelist)
#studytreelistTF = [False] * len(studytreelist)

# reverse the list. may or may not be wanted. to consider: load in one order (for compatability), prefer in opposite.
#studytreelist.reverse()

print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

# analysis name. this is used to prefix result files/directories. the base directory 'bdir' come in from wopr_conf.py.
#aname="Metazoa_test_2.5draft1_mapcompat"
#aname="Life_taxonomy-only_2.5draft1"
#aname="Decapoda_OTT2.5draft1_taxonomy-only"
aname="Life_v2.8draft5_mapcompat_20June2014"
# location of synth database
dsynth=bdir+aname+".db"
# location of synth treefile
treefn=bdir+aname+"-synth.tre"

download = True
if download:
    import general_tm_utils
    general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)  

#load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,extractottolid)
load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


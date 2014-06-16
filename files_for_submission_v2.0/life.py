"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

from stephen_desktop_conf import *


from microbes import studytreelist as microbelist
from plants import studytreelist as plantslist
from metazoa import studytreelist as metalist
from fungi import studytreelist as fungilist


studytreelist = []
studytreelist.extend(plantslist)
studytreelist.extend(metalist)
studytreelist.extend(fungilist)
studytreelist.extend(microbelist)

mapcompat = [True] * len(studytreelist)
#mapcompat = [] * len(studytreelist)

import load_synth_extract

synthottolid="93302"
print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

download = True
if download == True:
    for i in studytreelist:
        a = i.split("_")
        studyid = "_".join(a[:-1])
        print "downloading studyid "+studyid+" to "+studyloc
        general_tm_utils.get_study_opentreeapi(studyid,studyloc)
        

load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
			 treemloc,generallogfileloc,dsynth,synthottolid,treefn,mapcompat)

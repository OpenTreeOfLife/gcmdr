"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

from stephen_desktop_conf import *


#from microbes import studytreelist as microbelist
from plants_mls import studytreelist as plantslist
#from sas_metazoa import studytreelist as metalist
#from fungi import studytreelist as fungilist



studytreelist = []
studytreelist.extend(plantslist)
#studytreelist.extend(metalist)
#studytreelist.extend(fungilist)
#studytreelist.extend(microbelist)

mls_treelist = ["MLS_MPR_files/fungi_mls.out.noknees",
                "MLS_MPR_files/fabales.mls.out.noknees",
                "MLS_MPR_files/monocots.mls.out.noknees",
                "MLS_MPR_files/deepplants.mls.out.noknees",
                "MLS_MPR_files/rosids.mls.out.noknees"
]


mapcompat = [True] * len(studytreelist)
#mapcompat = [] * len(studytreelist)

import load_synth_extract

synthottolid="93302"
print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

download = True
if download:
    import general_tm_utils
    general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)    

load_synth_extract.run_with_additional_files(dott,dload,mls_treelist,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,mapcompat)

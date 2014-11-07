"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

import sys

sys.path.insert(0, '../')

from wopr_conf import *

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
                "MLS_MPR_files/rosids.mls.out.noknees",
#                "MLS_MPR_files/Aves_22August2014_mls_pruned.tre",
#                "MLS_MPR_files/Mammals_21August2014_mls_pruned.tre",
                "MLS_MPR_files/Microbes_24August2014_mls_pruned.tre"
]


mapcompat = [True] * len(studytreelist)
#mapcompat = [] * len(studytreelist)

import load_synth_extract

synthottolid="93302"
print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

aname="Life-test2_no-animals_MLS_27August2014"
dsynth=bdir+aname+".db"
treefn=bdir+aname+"-synth.tre"

download = False
if download:
    import general_tm_utils
    general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)    

load_synth_extract.run_with_additional_files(dott,dload,mls_treelist,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,mapcompat)

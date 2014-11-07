"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

import sys

sys.path.insert(0, '../')

from wopr_conf import *

from plants_mls import studytreelist as plantslist
from other_metazoa import studytreelist as metalist
from other_microbes import studytreelist as microbelist

studytreelist = []
studytreelist.extend(plantslist)
studytreelist.extend(metalist)
studytreelist.extend(microbelist)

mls_treelist = [
                "MLS_MPR_files_v2.0/Fungi_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/fabales.mls.out.noknees",
                "MLS_MPR_files_v2.0/monocots.mls.out.noknees",
                "MLS_MPR_files_v2.0/deepplants.mls.out.noknees",
                "MLS_MPR_files_v2.0/rosids.mls.out.noknees",
                "MLS_MPR_files_v2.0/Aves_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Mammals_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Actinopterygii_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Other_Tetrapods_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Arthropods_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Nematoda_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Annelida_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Cnidaria_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Porifera_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Archaea_MLS_7October2014_mls_pruned.tre",
                "MLS_MPR_files_v2.0/Cyanobacteria_MLS_7October2014_mls_pruned.tre"
]

mapcompat = [True] * len(studytreelist)

import load_synth_extract

synthottolid="93302"
print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

aname="Life_MLS_7October2014"
dsynth=bdir+aname+".db"
treefn=bdir+aname+"-synth.tre"

download = False
if download:
    import general_tm_utils
    general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)    

load_synth_extract.run_with_additional_files(dott,dload,mls_treelist,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,mapcompat)


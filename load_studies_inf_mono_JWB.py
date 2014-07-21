import sys
import load_synth_extract

sys.path.insert(0, 'files_for_submission_v2.0')

#from goo import studytreelist as metalist
from birds import studytreelist as birdlist
#from metazoa import studytreelist as metalist
#from fungi import studytreelist as metalist

if __name__ == "__main__":
    from wopr_conf import *
    
    synthottolid="691846" # metazoa
#    synthottolid="93302" # cellular organisms
#    studytreelist = ["420_522"]
#    studytreelist = ["2460_5285"] # Pyron Squamata study
#    studytreelist = ["2573_5959"] # Sauria
#    studytreelist = ["2573_5959"]
#    from metazoa import studytreelist as metalist
    studytreelist = []
    studytreelist.extend(birdlist)

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    baseloc = "files_for_submission_v2.0/"
    resloc = baseloc + "Aves_log/"
    dsynth = bdir + "TERP.db"
    treefn = bdir + "TERP.tre"
    
    download = False
    if download:
        import general_tm_utils
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc) 
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = resloc + i + ".log"
        ttfntreefn = resloc + i + ".tre"
        infmonofn = resloc + i + ".inf_mono"
        load_synth_extract.run_load_single_ttfn_inf_mono(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn,infmonofn)




import load_synth_extract

from plants import studytreelist as plantslist
from metazoa import studytreelist as metalist
from fungi import studytreelist as fungilist
from microbes import studytreelist as microbelist

studytreelist = []
studytreelist.extend(metalist)
studytreelist.extend(fungilist)
studytreelist.extend(microbelist)
studytreelist.extend(plantslist)

if __name__ == "__main__":
    from wopr_conf_TEMP import *
    
    synthottolid="93302" # cellular organisms
#    studytreelist = ["420_522"]
#    studytreelist = ["2460_5285"] # Pyron Squamata study
#    studytreelist = ["2573_5959"] # Sauria
#    studytreelist = ["2573_5959"]
#    from metazoa import studytreelist as metalist
#    studytreelist = []
#    studytreelist.extend(metalist)

#    studytreelist = [
#    "1634_3303", # Chiroptera. Agnarsson et al. 2011. PLoS Currents Tree of Life
#    ]

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "synth_studies_submission/"+i+".log"
        ttfntreefn = "synth_studies_submission/"+i+".tre"
        infmonofn = "synth_studies_submission/"+i+".inf_mono"
        load_synth_extract.run_load_single_ttfn_inf_mono(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn,infmonofn)




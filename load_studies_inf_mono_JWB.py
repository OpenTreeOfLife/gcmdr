import load_synth_extract

from metazoa_all import studytreelist

if __name__ == "__main__":
    from wopr_conf_TEMP import *
    
    synthottolid="691846" # metazoa
#    studytreelist = ["420_522"]
    studytreelist = ["2686_6238"]
#    studytreelist = ["2573_5959"]
#    from metazoa import studytreelist as metalist
#    studytreelist = []
#    studytreelist.extend(metalist)

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "metazoalog/"+i+".log"
        ttfntreefn = "metazoalog/"+i+".tre"
        infmonofn = "metazoalog/"+i+".inf_mono"
        load_synth_extract.run_load_single_ttfn_inf_mono(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn,infmonofn)




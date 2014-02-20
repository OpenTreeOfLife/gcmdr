import load_synth_extract

from metazoa_all import studytreelist
#studytreelist = ["2374_6380"]

if __name__ == "__main__":
    from wopr_conf_TEMP import *
    
    synthottolid="691846" # metazoa
    
    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "loadlog_JWB/" + i + ".log"
        ttfntreefn = "loadlog_JWB/" + i + ".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)




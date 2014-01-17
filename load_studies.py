import load_synth_extract

from fungi import studytreelist

if __name__ == "__main__":
    from stephen_desktop_conf_TEMP import *
    
    synthottolid="10218"

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "loadlog/"+i+".log"
        ttfntreefn = "loadlog/"+i+".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)




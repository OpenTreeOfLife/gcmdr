import load_synth_extract

from microbes import studytreelist

if __name__ == "__main__":
    from stephen_desktop_conf_TEMP2 import *
    
    synthottolid="10218"
    studytreelist = ["313_6019"]
    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "microbes_all_log/"+i+".log"
        ttfntreefn = "microbes_all_log/"+i+".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)




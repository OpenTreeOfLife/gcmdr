import load_synth_extract

from fungal_all import studytreelist

if __name__ == "__main__":
    from stephen_desktop_conf_TEMP import *
    
    synthottolid="656316"
    #studytreelist = ["713_1287"]
    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "fungallog_inf_mono/"+i+".log"
        ttfntreefn = "fungallog_inf_mono/"+i+".tre"
        infmonofn = "fungallog_inf_mono/"+i+".inf_mono"
        load_synth_extract.run_load_single_ttfn_inf_mono(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn,infmonofn)




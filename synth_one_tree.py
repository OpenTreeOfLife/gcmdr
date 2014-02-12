import load_synth_extract

from plants_all import studytreelist

if __name__ == "__main__":
    from stephen_desktop_conf_TEMP import *
    
    synthottolid="10218"
    studytreelist = ["2539_6294"]
    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    generallogfileloc = studytreelist[0]+".log"
    ttfntreefn = studytreelist[0]+".tre"
    load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,ttfntreefn,[True])




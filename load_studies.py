import load_synth_extract

from microbes import studytreelist

if __name__ == "__main__":
    from stephen_laptop_conf import *
    
    synthottolid="93302"
    studytreelist = ["313_6681"]
    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "/home/smitty/TEMP/"+i+".log"
        ttfntreefn = "/home/smitty/TEMP/"+i+".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)




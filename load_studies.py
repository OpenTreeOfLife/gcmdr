import load_synth_extract
import general_tm_utils

if __name__ == "__main__":
    from stephen_laptop_conf import *
    
    synthottolid="93302"
    studytreelist = [
"pg_1583_3194"
]
    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "/home/smitty/TEMP/"+i+".log"
        ttfntreefn = "/home/smitty/TEMP/"+i+".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)




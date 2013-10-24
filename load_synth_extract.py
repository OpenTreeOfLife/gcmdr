from general_tm_utils import *
from general_utils import *

def run_load_single(dott,dload,studyloc,studytreelist,javapre,treemloc,
        generallogfileloc,dsynth,synthottolid,treefn):
    delete_database(dload)
    copy_database(dott,dload)

    print "loading trees"
    for i in studytreelist:
        load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)

def run(dott,dload,studyloc,studytreelist,javapre,treemloc,
        generallogfileloc,dsynth,synthottolid,treefn):
    delete_database(dload)
    copy_database(dott,dload)

    print "loading trees"
    for i in studytreelist:
        load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)

    append = True

    delete_database(dsynth)
    copy_database(dload,dsynth)

    print "synthesizing"
    run_synth(javapre,treemloc,dsynth,synthottolid,studytreelist,generallogfileloc,append)

    print "extracting"
    extract_synth(javapre,treemloc,dsynth,synthottolid,treefn,append)


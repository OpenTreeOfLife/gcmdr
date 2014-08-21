from general_tm_utils import *
from general_utils import *

def run_load_single(dott,dload,studyloc,studytreelist,javapre,treemloc,
        generallogfileloc,dsynth,synthottolid,treefn,mapcompat):
    delete_database(dload)
    copy_database(dott,dload)

    print "loading trees"
    count = 0
    for i in studytreelist:
        load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        if mapcompat[count] == True: 
            mapcompat_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        count += 1


def run_load_single_ttfn(dott,dload,studyloc,studytreelist,javapre,treemloc,
                    generallogfileloc,dsynth,synthottolid,treefn,temptreefn):
    delete_database(dload)
    copy_database(dott,dload)

    print "loading trees"
    for i in studytreelist:
        load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,temptreefn,False)
        mapcompat_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,temptreefn,True)
        
def run_load_single_ttfn_inf_mono(dott,dload,studyloc,studytreelist,javapre,treemloc,
                    generallogfileloc,dsynth,synthottolid,treefn,temptreefn,infmonofn):
    delete_database(dload)
    copy_database(dott,dload)

    print "loading trees"
    for i in studytreelist:
        load_one_study_inf_mono(studyloc,i,javapre,treemloc,dload,generallogfileloc,temptreefn,infmonofn,False)

def run(dott,dload,studyloc,studytreelist,javapre,treemloc,
        generallogfileloc,dsynth,synthottolid,treefn,mapcompat):
    delete_database(dload)
    copy_database(dott,dload)

    print "loading trees"
    count = 0
    #get the hash as well and update the list
    studytreelist2 = [] #studytreelist with the hash
    for i in studytreelist:
        h = load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        studytreelist2.append(i+"_"+h)
        if mapcompat[count] == True: 
            mapcompat_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        count += 1

    append = True

    delete_database(dsynth)
    copy_database(dload,dsynth)

    print "synthesizing"
    run_synth(javapre,treemloc,dsynth,synthottolid,studytreelist2,generallogfileloc,append)

    print "extracting"
    extract_synth(javapre,treemloc,dsynth,synthottolid,treefn,append)

"""
this is intended to be used when you have files that are in additional to those that will be from the studytreelist
"""
def run_with_additional_files(dott,dload,mls_treelist,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,mapcompat):
    delete_database(dload)
    copy_database(dott,dload)
    studytreelist2 = [] #studytreelist with the hash

    print "loading individual files"
    for i in mls_treelist:
        h = load_one_study_newick(i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        studytreelist2.append(i)
        #assuming that we are mapping compatible
        mapcompat_one_study_newick(i,javapre,treemloc,dload,generallogfileloc,"TEST",False)

    print "loading trees"
    count = 0
    #get the hash as well and update the list
    for i in studytreelist:
        h = load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        studytreelist2.append(i+"_"+h)
        if mapcompat[count] == True: 
            mapcompat_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        count += 1

    append = True

    delete_database(dsynth)
    copy_database(dload,dsynth)

    print "synthesizing"
    run_synth(javapre,treemloc,dsynth,synthottolid,studytreelist2,generallogfileloc,append)

    print "extracting"
    extract_synth(javapre,treemloc,dsynth,synthottolid,treefn,append)

"""
This file contains general utils for working with treemachine and a database. 
This includes functions like
 - running pgloadind
 - running pgdelind
 - running sourceexplorer
"""

from subprocess import Popen
from tree_reader import read_tree_string

"""
this loads using the pgloadind function, the standard for 
all our loading in opentree

the study_treeid format is studyid_treeid
logfile should be a logfilename
"""
def load_nexson(studyloc,study_treeid,javapre,treemloc,dload,logfilename,append,test=False):
    studyid = study_treeid.split("_")[0]
    treeid = study_treeid.split("_")[1]
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("pgloadind")
    cmd.append(dload)
    cmd.append(studyloc+"/"+studyid)
    cmd.append(treeid)
    if test==True:
        cmd.append("f")
        print "testing nexson "+study_treeid+ " and saving log to "+logfilename
    else:
        print "loading nexson "+study_treeid+ " and saving log to "+logfilename
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    logfile = open(logfilename,filemode)
    pr = Popen(cmd,stdout=logfile).wait()
    logfile.close()

def load_taxonomy(treemloc,javapre,dott,taxonomy_filename,synonym_filename):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("inittax")
    cmd.append(taxonomy_filename)
    cmd.append(synonym_filename)
    cmd.append(dott)
    pr = Popen(cmd).wait()

def source_explorer(study_treeid,javapre,treemloc,dload,outfile,append):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("sourceexplorer")
    cmd.append(study_treeid)
    cmd.append(dload)
    print "printing the source "+study_treeid+" as loaded into "+dload+" into "+outfile
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    logfile = open(outfile,filemode)
    pr = Popen(cmd,stdout=logfile).wait()
    logfile.close()

"""
this will load the study and then export the source
and then will process the tree and print out the information about 
where it is mapped
"""
def load_one_study(studyloc,study_treeid,javapre,treemloc,dload,outfile,treeoutfile,append):
    load_nexson(studyloc,study_treeid,javapre,treemloc,dload,outfile,append)
    source_explorer(study_treeid,javapre,treemloc,dload,treeoutfile,append)
    #attempt to read the tree
    tf = open(treeoutfile,"r")
    tree = read_tree_string(tf.readline())
    print "root name:"+tree.label
    tf.close()

"""
this will return a boolean about ingroup and then a dictionary
of the taxa that mapped
"""
def test_one_study(studyloc,study_treeid,javapre,treemloc,dload,outfile,append):
    load_nexson(studyloc,study_treeid,javapre,treemloc,dload,outfile,append,True)
    ingroup = False
    matched_taxa = {}
    #read the logfile
    outf = open(outfile,"r")
    for i in outf:
        if "property added ot:inGroupClade" in i:
            ingroup = True
        spls = i.strip().split(" ")
        if spls[0] == "pgloadind":
            if "matched anc info" in i:
                matched_taxa[spls[11]]=spls[13]
    outf.close()
    return ingroup,matched_taxa

"""
this will run a normal synthesis for OpenTree of Life
"""
def run_synth(javapre,treemloc,dsynth,ottolid,studytreelist,outfile,append):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("synthesizedrafttreelist_ottid")
    cmd.append(str(ottolid))
    stt = ",".join(studytreelist)
    stt += ",taxonomy"
    cmd.append(stt)
    cmd.append(dsynth)
    print "running synth with "+" ".join(cmd)
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    logfile = open(outfile,filemode)
    pr = Popen(cmd,stdout=logfile).wait()
    logfile.close()

def extract_synth(javapre,treemloc,dsynth,ottolid,treeoutfile,append):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("extractdrafttree_ottid")
    cmd.append(str(ottolid))
    cmd.append(treeoutfile)
    cmd.append(dsynth)
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    pr = Popen(cmd).wait()

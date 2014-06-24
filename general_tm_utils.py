"""
This file contains general utils for working with treemachine and a database. 
This includes functions like
 - running pgloadind
 - running pgdelind
 - running sourceexplorer
"""
import urllib2,json
from subprocess import Popen,PIPE
from tree_reader import read_tree_string

def get_study_opentreeapi(studyid, studyloc):
    call = "http://ot10.opentreeoflife.org/api/v1/study/"+studyid
    req = urllib2.Request(call)
    res = urllib2.urlopen(req)
    fl = open(studyloc+"/"+studyid,"w")
    fl.write(res.read())
    fl.close()

def get_all_studies_opentreeapi(studytreelist,studyloc):
    for i in studytreelist:
        a = i.split("_")
        studyid = "_".join(a[:-1])
        print "downloading studyid "+studyid+" to "+studyloc
        get_study_opentreeapi(studyid,studyloc)

def get_git_SHA(studyloc):
    #is there a cleaner way to get the git SHA
    shacmd = "cat "+studyloc+"/.git/refs/heads/master"
    prt = Popen(shacmd,stdout=PIPE,shell=True,stdin=PIPE,close_fds=True)
    sha  = prt.stdout.read().strip()
    return sha

def get_git_SHA_from_json(studylocfile):
    fl = open(studylocfile,"r").read()
    data = json.loads(fl)
    sha = str(data['sha'])
    return sha

"""
this loads using the pgloadind function, the standard for 
all our loading in opentree

the study_treeid format is studyid_treeid
logfile should be a logfilename

UPDATE: this will get the current SHA of the git repo. if 
        want something else then you need to do something
        else
"""
def load_nexson(studyloc,study_treeid,javapre,treemloc,dload,logfilename,append,test=False):
    spls = study_treeid.split("_")
    studyid = "_".join(spls[:-1])
    treeid = spls[-1]
    sha = get_git_SHA_from_json(studyloc+"/"+studyid)
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("pgloadind")
    cmd.append(dload)
    cmd.append(studyloc+"/"+studyid)
    cmd.append(treeid)
    cmd.append(sha)
    if test==True:
        cmd.append("f")
        print "testing nexson "+study_treeid+ " ("+sha+") and saving log to "+logfilename
    else:
        print "loading nexson "+study_treeid+ " ("+sha+") and saving log to "+logfilename
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    logfile = open(logfilename,filemode)
    print " ".join(cmd)
    pr = Popen(cmd,stdout=logfile).wait()
    logfile.close()

def load_taxonomy(treemloc,javapre,dott,taxonomy_filename,synonym_filename,version):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("inittax")
    cmd.append(taxonomy_filename)
    cmd.append(synonym_filename)
    cmd.append(version)
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
    print " ".join(cmd)
    pr = Popen(cmd,stdout=logfile,stderr=PIPE).wait()
    logfile.close()

def source_explorer_inf_mono(study_treeid,javapre,treemloc,dload,outfile,append):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("sourceexplorer_inf_mono")
    cmd.append(study_treeid)
    cmd.append(dload)
    print "printing the source information and monophyly "+study_treeid+" as loaded into "+dload+" into "+outfile
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
    studyid = "_".join(study_treeid.split("_")[:-1])
    print studyid
    sha = get_git_SHA_from_json(studyloc+"/"+studyid)
    source_explorer(study_treeid+"_"+sha,javapre,treemloc,dload,treeoutfile,append)
    #attempt to read the tree
    tf = open(treeoutfile,"r")
    ts = None
    for i in tf:
        ts = i
    tree = read_tree_string(ts)
    print "root name:"+tree.label
    tf.close()
    return sha

"""
this will load the study and then export the source
and then will process the tree and print out the information about 
where it is mapped
"""
def load_one_study_inf_mono(studyloc,study_treeid,javapre,treemloc,dload,outfile,treeoutfile,infmonofile,append):
    load_nexson(studyloc,study_treeid,javapre,treemloc,dload,outfile,append)
    studyid = "_".join(study_treeid.split("_")[:-1])
    sha = get_git_SHA_from_json(studyloc+"/"+studyid)
    source_explorer(study_treeid+"_"+sha,javapre,treemloc,dload,treeoutfile,append)
    tf = open(treeoutfile,"r")
    tree = read_tree_string(tf.readline())
    print "root name:"+tree.label
    tf.close()
    mapcompat_one_study(studyloc,study_treeid,javapre,treemloc,dload,outfile,outfile,True)
    source_explorer_inf_mono(study_treeid,javapre,treemloc,dload,infmonofile,append)
    
"""
this will map the compatible nodes to a study loaded
"""
def mapcompat_one_study(studyloc,study_treeid,javapre,treemloc,dload,outfile,treeoutfile,append):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("mapcompat")
    cmd.append(dload)
    studyid = "_".join(study_treeid.split("_")[:-1])
    sha = get_git_SHA_from_json(studyloc+"/"+studyid)
    cmd.append(study_treeid+"_"+sha)
    print "mapping compatible nodes for " +study_treeid+" as loaded into "+dload
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    logfile = open(outfile,filemode)
    pr = Popen(cmd,stdout=logfile).wait()
    logfile.close()

"""
this will map the compatible nodes to a study loaded
"""
def mapcompat_one_study_test(studyloc,study_treeid,javapre,treemloc,dload,outfile,append):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("mapcompat")
    cmd.append(dload)
    studyid = "_".join(study_treeid.split("_")[:-1])
    sha = get_git_SHA_from_json(studyloc+"/"+studyid)
    cmd.append(study_treeid+"_"+sha)
    cmd.append("test")
    print "mapping compatible nodes for " +study_treeid+" as loaded into "+dload
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    logfile = open(outfile,filemode)
    pr = Popen(cmd,stdout=logfile).wait()
    logfile.close()
    
"""
this will return a boolean about ingroup and then a dictionary
of the taxa that mapped
"""
def test_one_study(studyloc,study_treeid,javapre,treemloc,dload,outfile,append,mapcompat):
    if mapcompat == True:
        load_nexson(studyloc,study_treeid,javapre,treemloc,dload,outfile,append,False)
    else:
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
    if mapcompat == True: 
        mapcompat_one_study_test(studyloc,i,javapre,treemloc,dload,outfile,True)
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
    print "extracting synth tree with "+" ".join(cmd)
    filemode = "w" #default is write
    if append == True:
        filemode = "a"
    pr = Popen(cmd).wait()

def extract_graphml(javapre,treemloc,dload,ottolid,outfile,depth):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("graphml_ottolid")
    cmd.append(ottolid)
    cmd.append(outfile)
    cmd.append("T")
    #cmd.append(str(ottolid))
    cmd.append(dload)
    cmd.append(str(depth))
    print "extracting graphml tree with "+" ".join(cmd)
    filemode = "w" #default is write
    pr = Popen(cmd).wait()


def extract_taxonomy_from_ids(javapre,treemloc,dload,ottlist,outfile):
    cmd = javapre.split(" ")
    cmd.append(treemloc)
    cmd.append("extracttaxonomysubtreeforottids")
    cmd.append(ottlist)
    cmd.append(outfile)
    cmd.append(dload)
    filemode = "a"
    pr = Popen(cmd).wait()

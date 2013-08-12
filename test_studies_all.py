import os,sys
from general_tm_utils import *
from general_utils import *

#this is my conf, make your own -- no need to commit
from stephen_laptop_conf import *

delete_database(dload)
copy_database(dott,dload)

studylist = []
for i in os.listdir(studyloc):
    #need to get the trees from the studies
    try:
        int(i)
    except:
        continue
    tfile = open(studyloc+"/"+i,"r")
    for j in tfile:
        if "#tree" in j:
            tnum = j.split("#tree")[1].split('"')[0]
            studylist.append(i+"_"+tnum)
    tfile.close()

print "loading trees"
for i in studylist:
    ingroup,matchedtaxa = test_one_study(studyloc,i,javapre,treemloc,dload,"loaded_"+i+".log",False)
    if ingroup == True:
        tfile = open("taxa_"+i+".tre","w")
        for j in matchedtaxa:
            tfile.write(j+"\t"+matchedtaxa[j]+"\n")
        tfile.close()
        break

import sys
from node import *

"""
this will take the output from 
process_taxa_from_test_studies.py 
and create trees with the labels of the number of studies that cover
those names
"""

treefilepre = "mappedtree_"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "python "+sys.argv[0]+" inlist taxonomy outtreedir"
        sys.exit(0)
    id_num = {}
    inf = open(sys.argv[1],"r")
    for i in inf:
        spls = i.strip().split("\t")
        id_num[spls[0]] = spls[2]
    inf.close()
    

    count = 0
    pid = {} #key is the child id and the value is the parent
    cid = {} #key is the parent and value is the list of children
    nid = {}
    nrank = {}
    sid = {}
    unid = {}
    tax = open(sys.argv[2],"r")
    for i in tax:
        spls = i.strip().split("\t|")
        tid = spls[0].strip()
        parentid = spls[1].strip()
        name = spls[2].strip()
        rank = spls[3].strip()
        flag = spls[6].strip()
        if flag == "D":
            continue
        nrank[tid] = rank
        nid[tid] = name
        sid[tid] = spls[4].strip()
        unid[tid] = spls[5].strip()
        pid[tid] = parentid
        if parentid not in cid: 
            cid[parentid] = []
        cid[parentid].append(tid)
        count += 1
        if count % 100000 == 0:
            print count
    tax.close()
    

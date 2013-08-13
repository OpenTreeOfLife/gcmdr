import sys
from node import *

"""
this will take the output from 
process_taxa_from_test_studies.py 
and create trees with the labels of the number of studies that cover
those names
"""

treefilepre = "mappedtree_"
target = "Viridiplantae"
maxnodes = 1000

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
    nodes = {}
    tax = open(sys.argv[2],"r")
    targetid = ""
    for i in tax:
        spls = i.strip().split("\t|")
        tid = spls[0].strip()
        parentid = spls[1].strip()
        name = spls[2].strip()
        rank = spls[3].strip()
        flag = spls[6].strip()
        if flag == "D":
            continue
        nid[tid] = name
        pid[tid] = parentid
        if name == target:
            #print "name set ",tid
            targetid = tid
        if parentid not in cid: 
            cid[parentid] = []
        cid[parentid].append(tid)
        count += 1
        #if count % 100000 == 0:
            #print count
    tax.close()
    
    if targetid == "":
        targetid = "805080"
    stack = [targetid]
    root = Node()
    root.label=target
    nodes[targetid] = root
    if targetid in id_num:
        nodes[targetid].data["size"] = id_num[targetid]
    count = 0
    while len(stack) > 0:
        count += 1
        if count >maxnodes:
            break
        tempid = stack.pop()
        if tempid not in cid:
            continue
        nodes[tempid] = Node()
        nodes[tempid].label = nid[tempid]
        nodes[tempid].istip=True
        if tempid in id_num:
            nodes[tempid].data["size"] = id_num[tempid]
        if tempid != targetid:
            if len(pid[tempid]) > 0:
                nodes[tempid].parent = nodes[pid[tempid]]
                nodes[pid[tempid]].add_child(nodes[tempid])
        #outfile.write(tempid+"\t|\t"+pid[tempid]+"\t|\t"+nid[tempid]+"\t|\t"+nrank[tempid]+"\t|\t"+sid[tempid]+"\t|\t"+unid[tempid]+"\t|\t"+flag[tempid]+"\t|\t\n")
        if tempid in cid:
            for i in cid[tempid]:
                stack.append(i)
    datatouse = ["size"]

    print nodes[targetid].get_json_repr(datatouse)
    

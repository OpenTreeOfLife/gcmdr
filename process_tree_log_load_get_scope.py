"""
this is intended to process the files from the load_studies.py script
where we can get loaded names of the tips and internal nodes

this will also extract the compatible information from the log file
"""
import os

import tree_reader
import node

directory = "fungallog"
tend = ".tre"
lend = ".log"

outfilen = "fungi.scope.results"

taxonomy_file = "/media/data/temp/taxonomy/OTT/ott/fungi.tsv"

def get_number_of_tips(tid,cid):
    tipn = 0
    stack = [tid]
    while len(stack) > 0:
        tempid = stack.pop()
        if tempid in cid:
            for i in cid[tempid]:
                stack.append(i)
        else:
            tipn += 1
    return tipn

if __name__ == "__main__":
    print "reading taxonomy file"
    fl = open(taxonomy_file)
    taxad = {} #key is id, value is name
    parad = {} #key is id, value is parent id
    cid = {}
    alreadyd = {} #key is id, value is number of tips
    for i in fl:
        spls = i.strip().split("\t|")
        tid = spls[0].strip()
        pid = spls[1].strip()
        taxad[tid] = spls[2].strip()
        parad[tid] = pid
        if pid not in cid: 
            cid[pid] = []
        cid[pid].append(tid)
    fl.close()
    print "finished reading the taxonomy"
    
    studies = []
    
    outfile = open(outfilen,"w")

    for i in os.listdir(directory):
        studies.append(i[0:len(i)-len(lend)])
    sl = set(studies)
    for i in sl:
        try:
            fl = open(directory+"/"+i+tend,"r")
            ts = fl.readline()
            fl.close()
            if len(ts) > 1:
                #read the tree first
                tr = tree_reader.read_tree_string(ts)
                tid = tr.label.split("_")[-1]
                if tid not in alreadyd:
                    alreadyd[tid] = get_number_of_tips(tid,cid)
                if alreadyd[tid] == 1:
                    continue
                outfile.write(i+","+str(len(list(tr.leaves())))+","+str(alreadyd[tid])+"\n")
        except:
            print "some problem with "+i
    
    outfile.close()

"""
this is intended to process the files from the load_studies.py script
where we can get loaded names of the tips and internal nodes

this will also extract the compatible information from the log file
"""
import os
import sys

tflags = ["major_rank_conflict","major_rank_conflict_direct","major_rank_conflict_inherited","environmental","unclassified_inherited","viral","nootu","barren","not_otu","incertae_sedis","incertae_sedis_direct","incertae_sedis_inherited","extinct_inherited","extinct_direct","hidden"]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "python process_taxonomy_for_load_log.py target infile outfile"
        sys.exit(0)
    target = (sys.argv[1]).strip()
    print "target taxa: ",target
    infile = open(sys.argv[2],"r")
    outfile = open(sys.argv[3],"w")

    count = 0
    pid = {} #key is the child id and the value is the parent
    cid = {} #key is the parent and value is the list of children
    nid = {}
    nrank = {}
    sid = {}
    unid = {}
    flagsp = {}
    targetid = ""
    for i in infile:
        spls = i.strip().split("\t|")
        tid = spls[0].strip()
        parentid = spls[1].strip()
        name = spls[2].strip()
        rank = spls[3].strip()
        nrank[tid] = rank
        nid[tid] = name
        sid[tid] = spls[4].strip()
        unid[tid] = spls[5].strip()
        flags = spls[6].strip()
        badflag = False
        if len(flags) > 0:
            for j in tflags:
                if j in flags:
                    badflag = True
                    break
            if badflag == True:
                continue
        flagsp[tid] = flags
        if tid == target:
            print "name set ",tid
            targetid = tid
        pid[tid] = parentid
        if parentid not in cid: 
            cid[parentid] = []
        cid[parentid].append(tid)
        count += 1
        if count % 100000 == 0:
            print count
    infile.close()
    
    stack = [targetid]
    while len(stack) > 0:
        tempid = stack.pop()
        outfile.write(tempid+"\t|\t"+pid[tempid]+"\t|\t"+nid[tempid]+"\t|\t"+nrank[tempid]+"\t|\t"+sid[tempid]+"\t|\t"+unid[tempid]+"\t|\t"+flagsp[tempid]+"\t|\t\n")
        if tempid in cid:
            for i in cid[tempid]:
                stack.append(i)
    outfile.close()


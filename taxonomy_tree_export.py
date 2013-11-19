import sys
from node import Node

def name_fix(nm):
    return nm.replace(" ","_").replace(")","_").replace("(","_").replace("-","_").replace(":","_")

skip = True
skiplist = ["uncultured","clone"]


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "python "+sys.argv[0]+" targetid depth taxonomyfile outfileprefix"
        sys.exit(0)
    target = (sys.argv[1]).strip()
    print "target taxa id: ",target
    depth = int(sys.argv[2])
    print "depth: ",depth
    infile = open(sys.argv[3],"r")
    count = 0
    pid = {} #key is the child id and the value is the parent
    cid = {} #key is the parent and value is the list of children
    nid = {}
    nrank = {}
    sid = {}
    unid = {}
    targetid = ""
    for i in infile:
        spls = i.strip().split("\t|")
        tid = spls[0].strip()
        parentid = spls[1].strip()
        name = spls[2].strip()
        if skip == True:
			cont = False
			for j in skiplist:
				if j in name:
					cont = True
					break
			if cont == True:
				continue
        #rank = spls[3].strip()
        #nrank[tid] = rank
        nid[tid] = name
        #sid[tid] = spls[4].strip()
        #unid[tid] = spls[5].strip()
        if tid == target:
            print "target set ",name, tid
            targetid = tid
        pid[tid] = parentid
        if parentid not in cid: 
            cid[parentid] = []
        cid[parentid].append(tid)
        count += 1
        if count % 100000 == 0:
            print count
    infile.close()
    
    outfile = open(sys.argv[4]+".list","w")
    stack = [targetid]
    nddict = {} #key is id, value is node
    root = Node()
    root.label = name_fix(nid[targetid])+"______"+targetid
    nddict[targetid] = root
    depths = {} #key is id, value is depth
    depths[targetid] = 1
    while len(stack) > 0:
        tempid = stack.pop()
        tdepth = depths[tempid]
        outfile.write(tempid+"\t|\t"+pid[tempid]+"\t|\t"+nid[tempid]+"\t|\t \t|\t \t|\t \t|\t\n")
        if depths[tempid] >= depth:
            continue
        if tempid in cid:
            pnd = nddict[tempid]
            for i in cid[tempid]:
                tnd = Node()
                tnd.label = name_fix(nid[i])+"______"+i
                pnd.add_child(tnd)
                nddict[i] = tnd
                stack.append(i)
                depths[i] = tdepth + 1
    outfile.close()
    outfile = open(sys.argv[4]+".tre","w")
    stri = root.get_newick_repr()
    outfile.write(stri+"\n")
    outfile.close()
    

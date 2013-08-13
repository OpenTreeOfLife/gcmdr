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
        #for newick
        nodes[tempid].label += '[&!label="'+str(id_num[tempid])+'"]'
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
            #for newick
            nodes[tempid].label += '[&!label="'+str(id_num[tempid])+'"]'
        if tempid != targetid:
            if len(pid[tempid]) > 0:
                nodes[tempid].parent = nodes[pid[tempid]]
                nodes[pid[tempid]].add_child(nodes[tempid])
        #outfile.write(tempid+"\t|\t"+pid[tempid]+"\t|\t"+nid[tempid]+"\t|\t"+nrank[tempid]+"\t|\t"+sid[tempid]+"\t|\t"+unid[tempid]+"\t|\t"+flag[tempid]+"\t|\t\n")
        if tempid in cid:
            for i in cid[tempid]:
                stack.append(i)
    datatouse = ["size"]
    print '#NEXUS\nbegin trees;\n'
    print '\ttree tree_1 = [&R] '+nodes[targetid].get_newick_repr(False)+";\n"
    print 'end;\n\n\n\nbegin figtree;\n\n\tset appearance.backgroundColour=#-1;\n\tset appearance.branchColorAttribute="User Selection";\n\tset appearance.branchLineWidth=0.05;\n\tset appearance.foregroundColour=#-16777216;\n\tset appearance.selectionColour=#-2144520576;\n\tset branchLabels.displayAttribute="Branch times";\n\tset branchLabels.fontName="sansserif";\n\tset branchLabels.fontSize=8;\n\tset branchLabels.fontStyle=0;\n\tset branchLabels.isShown=false;\n\tset branchLabels.significantDigits=4;\n\tset layout.expansion=0;\n\tset layout.layoutType="POLAR";\n\tset layout.zoom=0;\n\tset nodeBars.barWidth=4.0;\n\tset nodeLabels.displayAttribute="label";\n\tset nodeLabels.fontName="sansserif";\n\tset nodeLabels.fontSize=8;\n\tset nodeLabels.fontStyle=0;\n\tset nodeLabels.isShown=false;\n\tset nodeLabels.significantDigits=4;\n\tset polarLayout.alignTipLabels=false;\n\tset polarLayout.angularRange=0;\n\tset polarLayout.rootAngle=0;\n\tset polarLayout.rootLength=100;\n\tset polarLayout.showRoot=true;\n\tset radialLayout.spread=0.0;\n\tset rectilinearLayout.alignTipLabels=false;\n\tset rectilinearLayout.curvature=0;\n\tset rectilinearLayout.rootLength=100;\n\tset scale.offsetAge=0.0;\n\tset scale.rootAge=1.0;\n\tset scale.scaleFactor=1.0;\n\tset scale.scaleRoot=false;\n\tset scaleAxis.automaticScale=true;\n\tset scaleAxis.fontSize=8.0;\n\tset scaleAxis.isShown=false;\n\tset scaleAxis.lineWidth=1.0;\n\tset scaleAxis.majorTicks=1.0;\n\tset scaleAxis.origin=0.0;\n\tset scaleAxis.reverseAxis=false;\n\tset scaleAxis.showGrid=true;\n\tset scaleAxis.significantDigits=4;\n\tset scaleBar.automaticScale=true;\n\tset scaleBar.fontSize=10.0;\n\tset scaleBar.isShown=true;\n\tset scaleBar.lineWidth=1.0;\n\tset scaleBar.scaleRange=0.0;\n\tset scaleBar.significantDigits=4;\n\tset tipLabels.displayAttribute="Names";\n\tset tipLabels.fontName="sansserif";\n\tset tipLabels.fontSize=8;\n\tset tipLabels.fontStyle=0;\n\tset tipLabels.isShown=false;\n\tset tipLabels.significantDigits=4;\n\tset trees.order=true;\n\tset trees.orderType="decreasing";\n\tset trees.rooting=false;\n\tset trees.rootingType="User Selection";\n\tset trees.transform=false;\n\tset trees.transformType="cladogram";\nend;\n'
    

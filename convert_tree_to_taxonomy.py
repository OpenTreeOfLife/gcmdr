import sys
import tree_reader
from node import Node

"""
This script will convert a newick into a taxonomy
for the processing of smasher. It will create a file
that should be placed in a folder with more source
information that can be processed by smasher to update
sections of the taxonomy

This needs to do a variety of things to clean up these 
taxonomies before adding them to smasher

1) are there ranks
2) are there any new names
"""

check_taxonomy_by_ending = True

def check_rank_ending_plants(name):
    rank = "no rank"
    if len(name) > 5 and name[-5:] == "aceae":
        return "family"
    elif len(name) > 4 and name[-4:] == "ales":
        return "order"
    elif len(name) > 3 and name[-3:] == "eae":
        return "tribe"
    else:
        return "genus"
    return rank

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python "+sys.argv[0]+" infile.tre outfile.taxa"
        sys.exit(0)
    infile = open(sys.argv[1],"r")
    stri = infile.readline()
    tree = tree_reader.read_tree_string(stri)
    infile.close()
    names = {} #key is name, value is parent
    nums = {} #key is name, value is number
    cnum = 1
    for i in tree.iternodes():
        if len(i.label) > 0:
            nums[i.label] = cnum
            cnum += 1
        if i.parent != None:
            names[i.label] = i.parent.label
    outfile = open(sys.argv[2],"w")
    for i in nums:
        #print i
        p = ""
        if i in names:
            p = str(nums[names[i]])
        rank = "no rank"
        if check_taxonomy_by_ending:
            rank = check_rank_ending_plants(i)
        outfile.write(str(nums[i])+"\t|\t"+p+"\t|\t"+i+"\t|\t"+rank+"\t|\t\n")
    outfile.close()

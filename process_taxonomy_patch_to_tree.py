import sys
import tree_reader
from node import * 

"""
format of the patch file: 
command - what kind of operation to perform (includes add, synonym, move, prune and elide)
name1 - the name of a taxon (call it taxon1)
rank - rank to be associated with taxon1
name2 - the name of another taxon (call it taxon2)
context - the name of a taxon that is an ancestor of taxon1 and taxon2 (for homonym disambiguation)
sourceInfo - abbreviated information about the source of this taxon, see below

commands for the patch file
add
synonym
move
prune
elide

need to see if there is an annotate or add a visible and invisible command
"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python "+sys.argv[0]+" infile.tre outfile.patch"
        sys.exit(0)
    infile = open(sys.argv[1],"r")
    tree = tree_reader.read_newick(infile.readline())
    infile.close()


import sys
import tree_reader

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python "+sys.argv[0]+" infile.tre outfile.tre"
        sys.exit()
    infile = open(sys.argv[1],"r")
    outfile = open(sys.argv[2],"w")
    tree = tree_reader.read_tree_string(infile.readline())
    
    going = True
    while going == True:
        found = False
        for i in tree.leaves():
            parent = i
            while parent != tree:
                if len(parent.children) == 1:
                    pp = parent.parent
                    ch = parent.children[0]
                    pp.remove_child(parent)
                    parent.remove_child(ch)
                    pp.add_child(ch)
                    ch.parent = pp
                    break
                else:
                    parent = parent.parent
        if found == False:
            going = False
            break

    infile.close()
    outfile.write(tree.get_newick_repr()+";")
    outfile.close()

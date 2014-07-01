import sys
import tree_reader
import delete_knees
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python "+sys.argv[0]+" infile.tre outfile.tre"
        sys.exit()
    from stephen_laptop_conf import *
    infile = sys.argv[1]
    outfile = sys.argv[2]
    temp1 = "tempfile1"
    temp2 = "tempfile2"
    cmd1 = "cp "+infile+" "+temp1
    #copy to a temp
    os.system(cmd1)
    cmd2 = javapre +" "+treemloc+" checktaxhier "+ temp1 +" "+dott+" > "+temp2
    #tax hier
    os.system(cmd2)
    #delete knees
    inf = open(temp2,"r")
    inf.readline()
    tree = tree_reader.read_tree_string(inf.readline().strip()+";") 
    inf.close()
    tree = delete_knees.del_knees(tree)
    ouf = open(temp1,"w")
    ouf.write(tree.get_newick_repr()+";")
    ouf.close()
    #tax hier
    os.system(cmd2)
    #delete knees again
    inf = open(temp2,"r")
    inf.readline()
    tree = tree_reader.read_tree_string(inf.readline().strip()+";") 
    inf.close()
    tree = delete_knees.del_knees(tree)
    ouf = open(outfile,"w")
    ouf.write(tree.get_newick_repr()+";")
    ouf.close()
    

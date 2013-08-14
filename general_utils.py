"""
This file contains general functions for interacting with the database (not treemachine) 
using the neo4j connector. You can install this with these instructions
https://github.com/neo4j-contrib/python-embedded
or http://docs.neo4j.org/drivers/python-embedded/snapshot/

On linux you can do
sudo apt-get install python-jpype
sudo apt-get install python-pip
sudo pip install neo4j-embedded

then you need to make sure that you have JAVA_HOME set to your jdk folder
"""
#leaving the neo4j imports to the functions so that we can import without that module for now

from subprocess import Popen

"""
this takes a relid (as an int)
and a graphdatabase location
"""
def get_rel_info(dbname,relid):        
    from neo4j import GraphDatabase
    from neo4j import OUTGOING, INCOMING, ANY
    db = GraphDatabase(dbname)
    relid = int(relid) #make sure it is an int
    rel = db.relationship[relid]
    print rel
    for key,value in rel.items():
        print "\t"+key,value
    db.shutdown()

def get_node_info(dbname,nodeid):
    from neo4j import GraphDatabase
    from neo4j import OUTGOING, INCOMING, ANY
    db = GraphDatabase(dbname)
    nodeid = int(nodeid) #make sure it is an int
    nd = db.node[nodeid]
    print nd
    for key,value in nd.items():
        print "\t"+key,value
        if "uniqname" in str(key):
            break
    db.shutdown()

"""
search some text and get the ottol ids that match
"""
def get_nodeinfo_for_name(dbname,name):
    from neo4j import GraphDatabase
    from neo4j import OUTGOING, INCOMING, ANY
    db = GraphDatabase(dbname)
    with db.transaction:
        node_idx = db.node.indexes.get('graphNamedNodes')
        hits = node_idx['name'][name]
        for i in hits:
            print i
            for key,value in i.items():
                print "\t"+key,value
                #printing after, prints mrcas which are usually too long
                #comment to let it go, but don't commit
                if "uniqname" in str(key):
                    break
        hits.close()
    db.shutdown()

"""
construct a python object tree by traversing certain relationships
in the graph. This can be used to construct a tree of, for example,
synthesis
ottolid: start id
reltypes: s(stree),y(synth),t(taxonomy)
depth: limit on the depth
this is incomplete!
"""
def get_tree_from_rels(dbname,ottolid,reltype,depth):
    from neo4j import GraphDatabase
    from neo4j import OUTGOING, INCOMING, ANY
    db = GraphDatabase(dbname)
    with db.transaction:
        #get the node based on the ottolid
        node_idx = db.node.indexes.get('graphNamedNodes')
        hits = node_idx['name'][name]
        stnd = i
        for i in hits:
            print i
            stnd = i
            break
        hits.close()
        

"""
this will copy a database
"""
def copy_database(olddb,newdb):
    print "copying "+olddb+" to "+newdb
    cmd = ["cp","-r",olddb,newdb]
    pr = Popen(cmd).wait()

"""
this will remove a database
"""
def delete_database(dbname):
    print "deleting "+dbname
    cmd = ["rm","-r",dbname]
    pr = Popen(cmd).wait()

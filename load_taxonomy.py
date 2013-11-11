"""
this intention is to provide an easy way to load the taxonomy from ott
into treemachine
"""
from general_tm_utils import *
from general_utils import *

def load(treemloc, javapre, dott,taxonomy_filename, synonyms_filename):
    delete_database(dott)
    print "loading taxonomy"
    load_taxonomy(treemloc,javapre,dott,taxonomy_filename,synonyms_filename)
    
if __name__ == "__main__":
	from stephen_desktop_conf import *
	load(treemloc,javapre,dott,taxfile,synfile)

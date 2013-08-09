"""
This is used just to search for names and get back info from 
the database. Case sensitive
"""
import sys
from general_utils import *


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: python "+sys.argv[0]+"name database"
        sys.exit(0)
    get_nodeinfo_for_name(sys.argv[2],sys.argv[1])

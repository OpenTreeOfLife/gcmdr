# a dummy file to run specific tests of problematic taxa

studytreelist=[
               "420_522",   # Aves. Hackett et al. 2008. Science
               "1428_2855", # Mammals. Meredith et al. 2011. Science
               "2573_5959", # Sauria. Crawford et al. 2012. Biology Letters
            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="691846"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelist)


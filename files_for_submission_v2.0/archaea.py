synthottolid="996421"

studytreelist=[

"ot_106_1",       # Archaea. Matte-Tailliez et al. 2002. MBE
"pg_2731_6428",   # Archaea. Barns et al. 1996. PNAS
"pg_2715_6308",   # Archaea. Groussin. 2011. MBE

# "pg_2397_5038",   # Archaea + Bacteria + Eukaryotes. Williams et al. 2012. Proc. Roy. Soc. # Eukaryoyes withon Archaea. seems like a rooting problem. Don't buy it.

#"pg_2542_5590",   # Bacteria + Archaea. Lang et al. 2013. PLoS ONE
               
]
studytreelistTF = [True] * len(studytreelist)
if __name__ == "___main__":
	import load_synth_extract
	from wopr_conf import *

	synthottolid="996421"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)

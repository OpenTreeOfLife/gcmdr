studytreelist=[

"2810_6528", # unpublished study
"1252_2661", # maps to: Anomura
"1336_2660", # maps to: Brachyura
"1948_6513", # maps to: Anomura
"1796_6514", # maps to: Typhlatya
"2243_6515", # maps to: Paramunida
"2670_6214", # maps to: Atyidae
"2671_6216", # maps to: Caridina
"2673_6219", # maps to: Astacidea
"2674_6220", # maps to: Cambaridae
"2675_6221", # maps to: Cambaridae
"2676_6222", # maps to: Scyllaridae
"2677_6223", # maps to: Anomura
"2682_6227", # maps to: Decapoda
"2683_6228", # maps to: Dendrobranchiata
"2807_6519", # maps to: Alpheidae
"2808_6522", # maps to: Alpheoidea
"2667_6211" #on GitHub List # maps to: Galatheoidea
            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="169205"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)


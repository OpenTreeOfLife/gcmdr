synthottolid="805080"

"""
full list
study 425 tree 5976
study 239 tree 111 and 112  
study 263 tree  149
study 2413 tree 5093 and 5094 
study 2397 tree 5038 and 5039  
study 2398 tree 5040
from Dail
2739	6325	Bettina E Schirrmeister, Alexandre Antonelli, Homayoun C Bagheri. 2011. The origin of multicellularity in cyanobacteria. BMC Evolutionary Biology 11(1):45
2552	6326,6327, 6328, 6329	Theriot E., Cannone J., Gutell R., & Alverson A. 2009. The limits of nuclear-encoded SSU rDNA for resolving the diatom phylogeny. European Journal of Phycology, 44(3): 277-290.
2448	5223	Nicola Segata, Daniela Bornigen, Xochitl C. Morgan, and Curtis Huttenhower. PhyloPhlAn is a new method for improved phylogenetic and taxonomic placement of microbes
2425	5121	Fewer D., Friedl T., & Budel B. 2002. Chroococcidiopsis and heterocyst differentiating cyanobacteria are each other's closest living relatives. Molecular Phylogenetics and Evolution, 23(1): 82-90..
2542	5471, 5588, 5590	Jenna Morgan Lang, Aaron E. Darling, Jonathan A. Eisen. 2013. Phylogeny of Bacterial and Archaeal Genomes Using Conserved Genes: Supertrees and Supermatrices. PLoS ONE 8(4):e62510.

"""

studytreelist=["425_5976"] # Eukaryota. Katz et al. 2012. Syst Biol.

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="805080"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn)

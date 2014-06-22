import sys,os
from sequence import Sequence

"""
this is for reading some common alignment files
a list of sequences will be returned

NOTE: if you want to read an alignment in fasta format
		just use the fasta reader in seq_reader.py
"""


"""
This will read a phylip alignment file and return the 
list of seqs

The phylip file is in the format
numoftaxa numofsites
seqlabel sequence
seqlabel sequence

we assume that the phylip files are extended and not
strict (in terms of what type and how much white space
and how many characters for taxon names)
"""
def read_phylip_file(infilename):
	infile = open(infilename,"r")
	seqlist = []
	# first line is the number of taxa and num of sites
	# we don't really even need to read this line, 
	# so let's just skip it
	i = infile.readline()
	for i in infile:
		if len(i) > 2:
			spls = i.strip().split()
			name = spls[0].strip()
			seq = spls[1].strip()
			tseq = Sequence(name=name,seq=seq)
			seqlist.append(tseq)
	infile.close()
	return seqlist

"""
This will read a phylip alignment file with continuous characters and return the 
list of seqs

The phylip file is in the format
numoftaxa numofsites
seqlabel contvalue contvalue
seqlabel contvalue contvalue

we assume that the phylip files are extended and not
strict (in terms of what type and how much white space
and how many characters for taxon names)
"""
def read_phylip_cont_file(infilename):
	infile = open(infilename,"r")
	seqlist = []
	# first line is the number of taxa and num of sites
	# we don't really even need to read this line, 
	# so let's just skip it
	i = infile.readline()
	for i in infile:
		if len(i) > 2:
			spls = i.strip().split("\t")
			name = spls[0].strip()
			seq = spls[1].strip().split(" ")
			tseq = Sequence(name=name)
			tseq.set_cont_values(seq)
			seqlist.append(tseq)
	infile.close()
	return seqlist




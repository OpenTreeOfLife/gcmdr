import sys,os
from sequence import Sequence

"""
We can assume that the fastq will have
a sequence every 4 lines
"""
def read_fastq_file(infilename):
	infile = open(infilename,"r")
	seqlist = []
	i = infile.readline()
	while len(i) > 0: #no EOF in readline
		if i[0] == "@":
			name = i[1:].strip()
			seq = infile.readline().strip()
			i = infile.readline().strip()
			qual = infile.readline().strip()
			tseq = Sequence(name=name,seq=seq)
			tseq.set_qualstr(qual)
			seqlist.append(tseq)
		i = infile.readline()
	infile.close()
	return seqlist

"""
This is similar to the above but you can
use it as an iterator instead of reading it
into a list
usage: for i in read_fastq_file_iter(filename):
			print i.get_fastq()
"""
def read_fastq_file_iter(infilename):
	infile = open(infilename,"r")
	seqlist = []
	i = infile.readline()
	while len(i) > 0: #no EOF in readline
		if i[0] == "@":
			name = i[1:].strip()
			seq = infile.readline().strip()
			i = infile.readline().strip()
			qual = infile.readline().strip()
			tseq = Sequence(name=name,seq=seq)
			tseq.set_qualstr(qual)
			yield tseq
		i = infile.readline()
	infile.close()

"""
fasta files can be less well structured
so we have to account for white space, etc
"""
def read_fasta_file(infilename):
    infile = open(infilename,"r")
    seqlist = []
    curseqname = ""
    curseq = ""
    first = True
    for i in infile:
        i = i.strip()
        if len(i) == 0:
            continue
        if i[0] == ">":
            if first == True:
                first = False
            else:# if not the first, store the last seq
                tseq = Sequence()
                tseq.name = curseqname 
                tseq.seq = curseq
                seqlist.append(tseq)
            curseqname = i[1:]
            curseq = ""
        else: #seq can be on multiple lines
            curseq += i
    #need to get the last sequence stored
    tseq = Sequence()
    tseq.name = curseqname 
    tseq.seq = curseq
    seqlist.append(tseq)
    infile.close()
    return seqlist


if __name__ == "__main__":
	seqs = read_fasta_file("test.fasta")
	for i in seqs:
		print i.get_fasta()
	seqs = read_fastq_file("test.fastq")
	for i in seqs:
		print i.get_fastq()
	for i in read_fastq_file_iter("test.fastq"):
		print i.get_fastq()

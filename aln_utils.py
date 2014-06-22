import sys,os
from sequence import Sequence
import copy
import random

def sample_with_repl(pop, nitems):
    n = len(pop)
    result = [None] * nitems
    for i in xrange(nitems):
        j = int(random.random() * n)
        result[i] = pop[j]
    return result

def sample_without_repl(pop, nitems):
    return random.sample(pop,nitems)

def bootstrap_aln(seqs):
	bsseqs = copy.deepcopy(seqs)
	res = sample_with_repl(range(0,len(seqs[0].seq)),len(seqs[0].seq))
	#print res
	for i in range(len(bsseqs)):
		s = ""
		for j in res:
			s += seqs[i].seq[j]
		bsseqs[i].seq = s
	return bsseqs

"""
the nsites here should be the number of sites we want in the jackknife
alignment
"""
def jackknife_aln(seqs,nsites):
	bsseqs = copy.deepcopy(seqs)
	res = sample_without_repl(range(0,len(seqs[0].seq)),nsites)
	for i in range(len(bsseqs)):
		s = ""
		for j in res:
			s += seqs[i].seq[j]
		bsseqs[i].seq = s
	return bsseqs


#seqsarray should be an array of seqs
def write_concat_genes_to_phylip(seqsarray,outfilename):
    specieslist = []
    genespecies = []
    genespeciesd = []
    count = 0
    nsites = 0
    genelens = []
    for i in seqsarray:
        nsites += len(i[0].seq)
        genelens.append(len(i[0].seq))
        gsp = []
        gspd = {}
        for j in i:
            specieslist.append(j.name)
            if j.name in gsp:
                print "error",j.name,"duplicated in alignment",count
            gsp.append(j.name)
            gspd[j.name]= j
        count += 1
        genespecies.append(gsp)
        genespeciesd.append(gspd)
    specieslist = set(specieslist)
    
    outfile = open(outfilename,"w")
    seqstring = {}
    for j in specieslist:
        seqstring[j] = j+"\t"

    outfile.write(str(len(specieslist))+"\t"+str(nsites)+"\n")
    for i in range(len(seqsarray)):
        for j in specieslist:
            if j in genespecies[i]:
                seqstring[j] += genespeciesd[i][j].seq
            else:
                seqstring[j] += ("-"*genelens[i])
    
    for i in seqstring:
        outfile.write(seqstring[i]+"\n")

    outfile.close()

    outfile = open(outfilename+".models","w")
    start = 0
    end = 1
    for i in range(len(seqsarray)):
        start += 1
        end = start + genelens[i] - 1
        outfile.write("DNA, gene"+str(i)+" = "+str(start)+"-"+str(end)+"\n")
        start = end
    outfile.close()

import sys,os
import seq_reader,sequence
import aln_utils,aln_reader

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "python "+sys.argv[0]+" infile.fasta... outfile"
        sys.exit(0)
    seqsarray = []
    for i in sys.argv[1:-1]:
        seqs = aln_reader.read_phylip_file(i)
        seqsarray.append(seqs)
    aln_utils.write_concat_genes_to_phylip(seqsarray,sys.argv[-1])

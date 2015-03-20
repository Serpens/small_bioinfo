#!/usr/bin/env python
import sys
import getopt
from Bio import SeqIO
from helpers import parse_fasta


def filter_seqs(seqs, threshold):
    return [i for i in seqs if len(i.seq)>=threshold]


if __name__=='__main__':
    opts = list(getopt.getopt(sys.argv[1:], 't:'))
    opts[0] = dict(opts[0])
    threshold = int(opts[0].get('-t', 10))
    for fasta_path in opts[1]:
        seqs = parse_fasta(fasta_path)
        seqs = filter_seqs(seqs, threshold)
        print ''.join([i.format('fasta') for i in seqs])


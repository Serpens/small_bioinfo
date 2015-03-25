#!/usr/bin/env python
import sys
from getopt import getopt
from Bio import SeqIO
from helpers import parse_fasta, get_opts, write_seqs

def cut_from_left(seq, to_find='ATG'):
    start = seq.seq.find(to_find)
    if start > -1 and start < len(seq):
        return seq[start:]
    else:
        return None


if __name__=='__main__':
    opts = get_opts(sys.argv[1:], 's:i:o:')[0]
    seqs = parse_fasta(opts['-i'])
    seqs = [cut_from_left(i, to_find=opts.get('-s', 'ATG')) for i in seqs]
    seqs = [i for i in seqs if i is not None]
    write_seqs(seqs, opts['-o'])


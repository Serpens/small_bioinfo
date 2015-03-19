#!/usr/bin/env python
from getopt import getopt
from Bio import SeqIO
from Bio.Alphabet import IUPAC

def parse_fasta(fasta_path, alphabet=IUPAC.unambiguous_dna):
    with open(fasta_path) as f:
        seqs = [i for i in SeqIO.parse(f, 'fasta', alphabet)]
    return seqs

def get_opts(argv, opt_string, long_opt_string=[]):
    if not long_opt_string:
        opts = list(getopt(argv, opt_string))
    else:
        opts = list(getopt(argv, opt_string, long_opt_string))
    opts[0] = dict(opts[0])
    return opts


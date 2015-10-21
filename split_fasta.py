#!/usr/bin/env python
import sys
from Bio import SeqIO
from helpers import parse_fasta, write_seqs


if __name__=='__main__':
    input_path = sys.argv[1]
    seqs = parse_fasta(input_path)
    for seq in seqs:
        output_path = input_path.rstrip('.fasta') + '_' + seq.id + '.fasta'
        write_seqs(seq, output_path)


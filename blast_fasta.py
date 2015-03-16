#!/usr/bin/env python
import os, sys
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from time import sleep

def parse_fasta(fasta_path):
    with open(fasta_path) as f:
        seqs = [i for i in SeqIO.parse(f, 'fasta')]
    return seqs

def run_blast(seq, blast_type='blastn'):
    return NCBIWWW.qblast(blast_type, 'nr', seq.format('fasta')).getvalue()


if __name__=='__main__':
    fasta_path = sys.argv[1]
    seqs = parse_fasta(fasta_path)
    for seq in seqs:
        blast_xml_str = run_blast(seq)
        with open(seq.id + '_blast.xml', 'w') as f:
            f.write(blast_xml_str)
        sleep(2)     # I don't want to get banned by NCBI


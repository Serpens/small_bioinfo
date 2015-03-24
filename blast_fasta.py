#!/usr/bin/env python
import os, sys
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from time import sleep
from helpers import parse_fasta, get_opts

def usage():
    print """Usage: blast_fasta.py [OPTIONS] seqs.fasta
    Options:
        -t blast_type     blastn, blastp, blastx, tblastn, tblastx, default: blastn
        -o out_dir        output directory, default: current directory
        -p out_prefix     prefix for output file names, default: blast_
    """

def run_blast(seq, blast_type='blastn'):
    return NCBIWWW.qblast(blast_type, 'nr', seq.format('fasta')).getvalue()


if __name__=='__main__':
    try:
        opts = get_opts(sys.argv[1:], 't:o:p:')
        fasta_path = opts[1][0]
        opts = dict(opts[0])
    except:
        usage()
        exit(1)
    blast_type = opts.get('-t', 'blastn')
    out_dir = opts.get('-o', os.getcwd())
    out_prefix = opts.get('-p', 'blast_')
    seqs = parse_fasta(fasta_path)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for seq in seqs:
        print 'Running BLAST for ' + seq.id +  '... ',
        blast_xml_str = run_blast(seq, blast_type)
        with open(os.path.join(out_dir, out_prefix + seq.id + '.xml'), 'w') as f:
            f.write(blast_xml_str)
        print 'completed'
        sleep(2)     # I don't want to get banned by NCBI


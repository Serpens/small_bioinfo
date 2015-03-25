#!/usr/bin/env python
import os, sys
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline
from time import sleep
from helpers import get_opts

def usage():
    print """Usage: blast_fasta.py -d database [OPTIONS] seqs1.fasta [seqs2.fasta [...]]
    Options:
        -d database       path to database
        -t blast_type     blastn, blastp, blastx, tblastn, tblastx, default: blastn
        -o out_dir        output directory, default: current directory
        -p out_prefix     prefix for output file names, default: blast_
    """

def run_local_blast(fasta_path, database_path, blast_type='blastn'):
    cline = NcbiblastxCommandline(cmd=blast_type, query=fasta_path, 
            db=database_path, outfmt=5)    # outfmt=5 gives results as XML
    return cline()[0]


if __name__=='__main__':
    try:
        opts = get_opts(sys.argv[1:], 'd:t:o:p:')
        fasta_paths = opts[1]
        opts = dict(opts[0])
        db_path = opts['-d']
    except:
        usage()
        exit(1)
    blast_type = opts.get('-t', 'blastn')
    out_dir = opts.get('-o', os.getcwd())
    out_prefix = opts.get('-p', 'blast_')
    for fasta_path in fasta_paths:
        print 'Running BLAST for ' + fasta_path + '... ',
        blast_xml_str = run_local_blast(fasta_path, db_path, blast_type)
        with open(os.path.join(out_dir, out_prefix + os.path.basename(fasta_path) + '.xml'), 'w') as f:
            f.write(blast_xml_str)
        print 'completed'


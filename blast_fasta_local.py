#!/usr/bin/env python
import os, sys
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline
from time import sleep
from helpers import get_opts

def usage():
    print """Usage: blast_fasta.py -d database [OPTIONS] seqs.fasta
    Options:
        -d database       path to database
        -t blast_type     blastn, blastp, blastx, tblastn, tblastx, default: blastn
        -o out_file       output file, default: blast.xml
    """

def run_local_blast(fasta_path, database_path, blast_type='blastn'):
    cline = NcbiblastxCommandline(cmd=blast_type, query=fasta_path, 
            db=database_path, outfmt=5)    # outfmt=5 gives results as XML
    return cline()[0]


if __name__=='__main__':
    try:
        opts = get_opts(sys.argv[1:], 'd:t:o:p:')
        fasta_path = opts[1][0]
        opts = dict(opts[0])
        db_path = opts['-d']
    except:
        usage()
        exit(1)
    blast_type = opts.get('-t', 'blastn')
    out_file = opts.get('-o', 'blast.xml')
    blast_xml_str = run_local_blast(fasta_path, db_path, blast_type)
    with open(out_file, 'w') as f:
        f.write(blast_xml_str)


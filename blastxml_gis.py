#!/usr/bin/env python
import sys
from Bio.Blast.NCBIXML import BlastParser, read

def get_gis(blast_file_handle):
    parser = read(blast_file_handle)
    return [i.hit_id for i in parser.alignments]


if __name__=='__main__':
    with open('blastx_results/blast_IIKE3SZ08JLAXS.xml') as f:
        print '\n'.join(get_gis(f))


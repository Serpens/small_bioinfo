#!/usr/bin/env python
import sys
from Bio.Blast.NCBIXML import BlastParser, read

def get_gis(blast_file_handle):
    parser = read(blast_file_handle)
    return [i.hit_id for i in parser.alignments]


if __name__=='__main__':
    for i in sys.argv[1:]:
        with open(i) as f:
            print i
            print '\n'.join(get_gis(f))


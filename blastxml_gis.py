#!/usr/bin/env python
import sys
import getopt
from Bio.Blast.NCBIXML import BlastParser, read

def get_hit_ids(blast_file_handle):
    parser = read(blast_file_handle)
    return [i.hit_id for i in parser.alignments]

def filter_gi(hit_id):
    return hit_id.split('|')[1]

if __name__=='__main__':
    opts = list(getopt.getopt(sys.argv[1:], '', ['only-gi']))
    opts[0] = [i[0] for i in opts[0]]
    for i in opts[1]:
        with open(i) as f:
            print i
            ids = get_hit_ids(f)
            if '--only-gi' in opts[0]:
                ids = [filter_gi(i) for i in ids]
            print '\n'.join(ids)


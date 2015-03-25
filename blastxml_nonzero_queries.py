#!/usr/bin/env python
import sys
from Bio.Blast.NCBIXML import parse


def get_query_ids(blast_file_handle):
    parser = parse(blast_file_handle)
    records = [i for i in parser]
    return [i.query for i in records if len(i.alignments)]


if __name__=='__main__':
    for i in sys.argv[1:]:
        with open(i) as f:
            print i
            print '\n'.join(get_query_ids(f))


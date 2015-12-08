#!/usr/bin/env python
import sys
from helpers import parse_fasta, get_opts


if __name__=='__main__':
    opts = get_opts(sys.argv[1:], 'i:o:')[0]
    seqs = parse_fasta(opts['-i'])
    result = [' '.join([s.name, str(len(s))]) for s in seqs]
    with open(opts['-o'], 'w') as f:
        f.write('\n'.join(result))

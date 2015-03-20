#!/usr/bin/env python
import os, sys
import getopt
from helpers import parse_fasta

def translate_all_frames(seq):
    ans = []
    for i in xrange(0, 3):
        ans.append(SeqIO.SeqRecord(
            id=seq.id + '_' + str(i), 
            seq=seq.seq[i:].translate(to_stop=True), 
            description=seq.description))
        ans.append(SeqIO.SeqRecord(
            id=seq.id + '_reverse_' + str(i), 
            seq=seq.seq[i:].reverse_complement().translate(to_stop=True), 
            description=seq.description))
    return ans

def write_seqs(seqs, fasta_path):
    with open(fasta_path, 'w') as f:
        SeqIO.write(seqs, f, 'fasta')


if __name__=='__main__':
    seqs = parse_fasta(sys.argv[1])
    translated = [translate_all_frames(s) for s in seqs]
    translated = reduce(lambda x,y: x+y, translated)
    write_seqs(translated, sys.argv[2])



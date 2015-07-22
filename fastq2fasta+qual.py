#!/usr/bin/env python
import sys
from Bio import SeqIO


def convert_fastq(fastq_path, fasta_path, qual_path):
    SeqIO.convert(fastq_path, 'fastq', fasta_path, 'fasta')
    SeqIO.convert(fastq_path, 'fastq', qual_path, 'qual')


if __name__ == '__main__':
    fastq_path = sys.argv[1]
    if len(sys.argv) == 4:
        fasta_path = sys.argv[2]
        qual_path = sys.argv[3]
    else:
        fasta_path = fastq_path.rstrip('.fastq') + '.fasta'
        qual_path = fastq_path.rstrip('.fastq') + '.qual'
    convert_fastq(fastq_path, fasta_path, qual_path)


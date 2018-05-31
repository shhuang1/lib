"""
Extract sequence FASTA file from BED files, replaced modified nucleotides.
Currently only 5mC from all_c files in HDF5 format.
"""
import argparse
import gzip
import os
import re
import sys

from Bio import SeqIO
from collections import defaultdict
from pandas import read_hdf

from shared import LoggerFactory

def main():

    parser = argparse.ArgumentParser(description='Modified genome FASTA file by 5mC')
    parser.add_argument('genome')
    parser.add_argument('allc_h5')
    parser.add_argument('genome_mod')
    parser.add_argument('--zero',help='whether the allc table is 0-index',action='store_true')
    args = parser.parse_args()
    genome,allc_h5,genome_mod = args.genome,args.allc_h5,args.genome_mod
    offset = 0 if args.zero else 1  # allc table positions are 1-based
    
    logger = LoggerFactory.get_logger(genome_mod+'.log')
    LoggerFactory.log_command(logger,sys.argv)
    logger.info('Getting unmodified genome FASTA file from %s',genome)

    coord_pat = re.compile('^(chr)?(.+)$')
    fa_list = list(SeqIO.parse(genome, "fasta"))
    fa_dict = dict((r.id,r.seq) for r in fa_list)
    fa_key_by_chrom = dict()
    for k in fa_dict.keys(): # '1' -> 'chr1' or '1' -> '1'
        coord_mat = coord_pat.match(k)
        chrom = coord_mat.group(2)
        fa_key_by_chrom[chrom] = k

    logger.info('Chromosomes: %s',fa_key_by_chrom.keys())
    logger.info('Modifying FASTA by all_c %s',allc_h5)
    fa_dict_out = dict()
    for chrom,fa_key in fa_key_by_chrom.items():
        logger.info('Reading allc table for chromosome %s from %s',chrom,allc_h5)
        hdf = read_hdf(allc_h5,'allc_'+str(chrom),where=['mcall==1'],columns=['pos','strand','context'])
        mc_pos,mc_strand,mc_type = hdf['pos'],hdf['strand'],hdf['context']
        logger.info('Number of methylated C: %d',len(mc_pos))

        seq = fa_dict[fa_key].tomutable()
        for p,s,t in zip(mc_pos,mc_strand,mc_type):
            p0 = p - offset
            if (p0>len(seq)):
                logger.info('Index out of bound for %s: mc_pos %d, len %d',fa_key,p0,len(seq))
                continue
            if s=='+':
                if (seq[p0]=='C' or seq[p0]=='c'):
                    seq[p0] = 'm'
                else:
                   logger.warn('Sequence %s: expected to see C/c (%s:%s) at %d, but saw %s',fa_key,t,s,p0,seq[p0])
            elif s=='-':
                if (seq[p0]=='G' or seq[p0]=='g'):
                    seq[p0] = '1'
                else:
                    logger.warn('Sequence %s: expected to see G/g (%s:%s) at %d, but saw %s',fa_key,t,s,p0,seq[p0])
            else:
                logger.warn('Sequence %s: unrecognized strand %s at %d',fa_key,s,p0)
        fa_dict_out[fa_key] = seq
                        
    for r in fa_list:
        r.seq = fa_dict_out[r.id]
    with open(genome_mod,'w') as ofa:
        SeqIO.write(fa_list,ofa,'fasta')

    logger.info('Done!')
        

if __name__=='__main__':
    main()

# Python 3.6.7
# seung1.yoo@gamil.com

import yaml
import os
import gzip
from Bio import SeqIO

class CreateConfig:
    def __init__(self, args):
        self.config_dic = dict()
        self.add_rawreadList(args.rawreadList)
        self.add_inbamList(args.inbamList)
        self.write(args.outfn, args.workdir)

    def add_rawreadList(self, fn):
        for line in open(fn):
            items = line.rstrip('\n').split()
            _path = items[0]
            sample = items[1]
            strand = items[2]
            if strand in ['1']:
                self.config_dic.setdefault("samples", {}).setdefault(sample, {}).setdefault("fastq_1", _path)
            elif strand in ['2']:
                self.config_dic.setdefault("samples", {}).setdefault(sample, {}).setdefault("fastq_2", _path)
            else:
                print("ERROR : un-expacted read strand")
                sys.exit()

    def add_inbamList(self, fn):
        for line in open(fn):
            items = line.rstrip('\n').split()
            _path = items[0]
            sample = items[1]
            self.config_dic.setdefault("samples", {}).setdefault(sample, {}).setdefault("inbam", _path)

    def write(self, outfn, workdir):
        outfh = open(outfn, 'w')
        outfh.write('\n')
        outfh.write('workdir: {0}\n'.format(workdir))
        outfh.write('\n')
        yaml.dump(self.config_dic, outfh)
        outfh.write('\n')
        outfh.close()


class ExtractRawread:
    def __init__(self, args):
        self.target_dic = self.add_readList(args.readList)
        self.extracter(args.in_fq_1, args.out_fq_1)
        self.extracter(args.in_fq_2, args.out_fq_2)

    def add_readList(self, fn):
        target_dic = dict()
        for line in open(fn):
            target_dic.setdefault(line.strip())
        return target_dic

    def extracter(self, in_fq, out_fq):
        outfh = gzip.open(out_fq, 'wt')
        for record in SeqIO.parse(gzip.open(in_fq, 'rt'), 'fastq'):
            if record.id in self.target_dic:
                SeqIO.write(record, outfh, 'fastq')
        outfh.close()


def main(args):
    if args.command in ['create_config']:
        config = CreateConfig(args)
    elif args.command in ['extract_rawread']:
        extracted_rawread = ExtractRawread(args)


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    subparser = subparsers.add_parser('create_config')
    subparser.add_argument('--outfn')
    subparser.add_argument('--rawreadList')
    subparser.add_argument('--inbamList')
    subparser.add_argument('--workdir')

    subparser = subparsers.add_parser('extract_rawread')
    subparser.add_argument('--in-fq-1', help='have to fq.gz')
    subparser.add_argument('--in-fq-2', help='have to fq.gz')
    subparser.add_argument('--readList')
    subparser.add_argument('--out-fq-1', help='have to fq.gz')
    subparser.add_argument('--out-fq-2', help='have to fq.gz')

    args = parser.parse_args()
    main(args)

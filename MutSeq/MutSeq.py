#!/usr/bin/env python
import os
import sys, getopt
import os.path
import argparse
import pandas as pa

dir = os.path.dirname(os.path.abspath(__file__))
version_py = os.path.join(dir, "_version.py")
exec(open(version_py).read())

def MutSeq(inputpath,input,outpath,outfile):
    os.chdir(inputpath)
    DNA = pd.read_csv(input,sep="\t",header=0,names=['seq'])
    bases = ['A', 'T', 'C', 'G']
    result = {}

    for indexid, seq in DNA.iterrows():
        sequence = seq['seq']
        #result[indexid] = []
        for i in range(len(sequence)):
            original_base = sequence[i]
            for base in bases:
                if base != original_base:
                    out = sequence[:i] + base + sequence[i+1:]
                    result["original:"+str(indexid)+":position:"+str(i)+":"+original_base+":"+base]=out

    df = pd.DataFrame.from_dict(result, orient='index')
    output = df.index.str.split(':', expand=True).to_frame(index=False)
    output = output[[1,3,4,5]]
    output.rename(columns={1: 'originalid', 3: 'positionid',4:'reference',5:'mutation'},inplace=True)
    output['seq'] = df[0].tolist()
    output.to_csv(outpath+'/'+outfile+'.fasta',sep="\t",header=False,index=False)
    del DNA,result,df,output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', '--inputpath', dest='inputpath',
                        required=True,
                        help='path of input file')
    parser.add_argument('-f', '--filename', dest='filename',
                        required=True,
                        help='name of input file')
    parser.add_argument('-O', '--outpath', dest='outpath',
                        required=True,
                        help='path of output file')
    parser.add_argument('-o', '--outfile', dest='outfile',
                        required=True,
                        help='name of output file')
    parser.add_argument("-V", "--version", action="version",version="MutSeq {}".format(__version__)\
                      ,help="Print version and exit")
    args = parser.parse_args()
    print('###Parameters:')
    print(args)
    print('###Parameters')
    MutSeq(args.inputpath,args.filename,args.outpath,args.outfile,args.version)

if __name__ == '__main__':
    main()



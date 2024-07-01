# MutSeq

This tutorial will introduce how to run MutSeq to generate/introduce genetic/point mutations in a given DNA sequence.

#### usage: 
```MutSeq [-h] [-b] -I INPUTPATH -f FILENAME -O OUTPATH -o OUTFILE``` 

input file has multiple DNA sequences with a column name.  
the output file show the DNA sequences with genetic mutations in each position. 

example:  
```MutSeq -I "the input path" -f "input file name" -o "output path" -O "the path of output"```


optional arguments:  
|  |   |    |   |   |
|:----:|:-----:|:----:|:------:|:------:|  
| -h |  |--help|| show this help message and exit |
| -I | INPUTPATH  | --inputpath | INPUTPATH |path of input file  |  
| -f | FILENAME   | --filename    | FILENAME |name of input file |
| -O | OUTPATH    | --outpath |  OUTPATH |path of output file  |  
| -o | OUTFILE    | --outfile |  OUTFILE |name of output file  |

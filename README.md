# getMappedRawReads

Reference sequence 에 "잘" 붙은 "raw reads" 를 얻기 위해 만듬.




## Environments

1. linux
2. python 3.6.7
3. samtools 1.9
4. htslib 1.9

## Usage

1. make input files (rawreadList.txt, inbamList.txt)

```
find <raw read path> -iname '*.fq.gz' | sort > rawreadList.txt
find <aligned bam path> -iname '*.bam' | sort > inbamList.txt
```

2.  modified *List.txt both

- rawreadList.txt example

```
rawdata/Sample_Set1_CM_I329T/Set1_CM_I329T_1.fq.gz                                   Set1_CM_I329T 1
rawdata/Sample_Set1_CM_I329T/Set1_CM_I329T_2.fq.gz                                   Set1_CM_I329T 2
rawdata/Sample_Set1_CM_I588T/Set1_CM_I588T_1.fq.gz                                   Set1_CM_I588T 1
rawdata/Sample_Set1_CM_I588T/Set1_CM_I588T_2.fq.gz                                   Set1_CM_I588T 2
rawdata/Sample_Set1_CM_R160Q/Set1_CM_R160Q_1.fq.gz                                   Set1_CM_R160Q 1
rawdata/Sample_Set1_CM_R160Q/Set1_CM_R160Q_2.fq.gz                                   Set1_CM_R160Q 2
rawdata/Sample_Set1_CM_WT/Set1_CM_WT_1.fq.gz                                         Set1_CM_WT 1
rawdata/Sample_Set1_CM_WT/Set1_CM_WT_2.fq.gz                                         Set1_CM_WT 2
rawdata/Sample_Set2_CM_I329T/Set2_CM_I329T_1.fq.gz                                   Set2_CM_I329T 1
rawdata/Sample_Set2_CM_I329T/Set2_CM_I329T_2.fq.gz                                   Set2_CM_I329T 2
rawdata/Sample_Set2_CM_I588T/Set2_CM_I588T_1.fq.gz                                   Set2_CM_I588T 1
rawdata/Sample_Set2_CM_I588T/Set2_CM_I588T_2.fq.gz                                   Set2_CM_I588T 2
rawdata/Sample_Set2_CM_R160Q/Set2_CM_R160Q_1.fq.gz                                   Set2_CM_R160Q 1
rawdata/Sample_Set2_CM_R160Q/Set2_CM_R160Q_2.fq.gz                                   Set2_CM_R160Q 2
rawdata/Sample_Set2_CM_WT/Set2_CM_WT_1.fq.gz                                         Set2_CM_WT 1
rawdata/Sample_Set2_CM_WT/Set2_CM_WT_2.fq.gz                                         Set2_CM_WT 2
rawdata/TBD200717_10759-10857_20201208/Sample_Set1_CM_I588T-1/Set1_CM_I588T-1_1.fq.gz      Set1_CM_I588T-1 1
rawdata/TBD200717_10759-10857_20201208/Sample_Set1_CM_I588T-1/Set1_CM_I588T-1_2.fq.gz      Set1_CM_I588T-1 2
rawdata/TBD200717_10759-10857_20201208/Sample_Set1_CM_R160Q-1/Set1_CM_R160Q-1_1.fq.gz      Set1_CM_R160Q-1 1
rawdata/TBD200717_10759-10857_20201208/Sample_Set1_CM_R160Q-1/Set1_CM_R160Q-1_2.fq.gz      Set1_CM_R160Q-1 2
rawdata/TBD200717_10759-10857_20201208/Sample_Set1_CM_WT-1/Set1_CM_WT-1_1.fq.gz            Set1_CM_WT-1 1
rawdata/TBD200717_10759-10857_20201208/Sample_Set1_CM_WT-1/Set1_CM_WT-1_2.fq.gz            Set1_CM_WT-1 2
rawdata/TBD200717_10759-10857_20201208/Sample_Set2_CM_I588T-1/Set2_CM_I588T-1_1.fq.gz      Set2_CM_I588T-1 1
rawdata/TBD200717_10759-10857_20201208/Sample_Set2_CM_I588T-1/Set2_CM_I588T-1_2.fq.gz      Set2_CM_I588T-1 2
rawdata/TBD200717_10759-10857_20201208/Sample_Set2_CM_R160Q-1/Set2_CM_R160Q-1_1.fq.gz      Set2_CM_R160Q-1 1
rawdata/TBD200717_10759-10857_20201208/Sample_Set2_CM_R160Q-1/Set2_CM_R160Q-1_2.fq.gz      Set2_CM_R160Q-1 2
```


- inbamList.txt example

```
star/Set1_CM_I329T/Aligned.sortedByCoord.out.bam     Set1_CM_I329T
star/Set1_CM_I588T-1/Aligned.sortedByCoord.out.bam   Set1_CM_I588T-1
star/Set1_CM_I588T/Aligned.sortedByCoord.out.bam     Set1_CM_I588T
star/Set1_CM_R160Q-1/Aligned.sortedByCoord.out.bam   Set1_CM_R160Q-1
star/Set1_CM_R160Q/Aligned.sortedByCoord.out.bam     Set1_CM_R160Q
star/Set1_CM_WT-1/Aligned.sortedByCoord.out.bam      Set1_CM_WT-1
star/Set1_CM_WT/Aligned.sortedByCoord.out.bam        Set1_CM_WT
star/Set2_CM_I329T/Aligned.sortedByCoord.out.bam     Set2_CM_I329T
star/Set2_CM_I588T-1/Aligned.sortedByCoord.out.bam   Set2_CM_I588T-1
star/Set2_CM_I588T/Aligned.sortedByCoord.out.bam     Set2_CM_I588T
star/Set2_CM_R160Q-1/Aligned.sortedByCoord.out.bam   Set2_CM_R160Q-1
star/Set2_CM_R160Q/Aligned.sortedByCoord.out.bam     Set2_CM_R160Q
star/Set2_CM_WT/Aligned.sortedByCoord.out.bam        Set2_CM_WT
```

3. create config file

- using get\_mappedRawReads.py create\_config

```
usage: get_mappedRawReads.py create_config [-h] [--outfn OUTFN]
                                           [--rawreadList RAWREADLIST]
                                           [--inbamList INBAMLIST]
                                           [--workdir WORKDIR]

optional arguments:
  -h, --help            show this help message and exit
  --outfn OUTFN
  --rawreadList RAWREADLIST
  --inbamList INBAMLIST
  --workdir WORKDIR
```

- command example

```
python get_mappedRawReads.py create_config --outfn config.yaml --rawreadList rawreadList.txt --inbamList inbamList.txt --workdir <working dir path>
```

1. run snakefile

```
snakemake --cores $(wc -l inbamList.txt | awk '{ print $1 *2 }') --snakefile get_mappedRawReads.snakefile
```

## output files

```
├── Set1_CM_I329T
│   ├── read_mapped_in_proper_pair.list
│   ├── Set1_CM_I329T_1.fq.gz
│   └── Set1_CM_I329T_2.fq.gz
├── Set1_CM_I588T
│   ├── read_mapped_in_proper_pair.list
│   ├── Set1_CM_I588T_1.fq.gz
│   └── Set1_CM_I588T_2.fq.gz
├── Set1_CM_I588T-1
│   ├── read_mapped_in_proper_pair.list
│   ├── Set1_CM_I588T-1_1.fq.gz
│   └── Set1_CM_I588T-1_2.fq.gz
├── Set1_CM_R160Q
│   ├── read_mapped_in_proper_pair.list
│   ├── Set1_CM_R160Q_1.fq.gz
│   └── Set1_CM_R160Q_2.fq.gz
├── Set1_CM_R160Q-1
│   ├── read_mapped_in_proper_pair.list
│   ├── Set1_CM_R160Q-1_1.fq.gz
│   └── Set1_CM_R160Q-1_2.fq.gz
├── Set1_CM_WT
│   ├── read_mapped_in_proper_pair.list
│   ├── Set1_CM_WT_1.fq.gz
│   └── Set1_CM_WT_2.fq.gz
├── Set1_CM_WT-1
│   ├── read_mapped_in_proper_pair.list
│   ├── Set1_CM_WT-1_1.fq.gz
│   └── Set1_CM_WT-1_2.fq.gz
├── Set2_CM_I329T
│   ├── read_mapped_in_proper_pair.list
│   ├── Set2_CM_I329T_1.fq.gz
│   └── Set2_CM_I329T_2.fq.gz
├── Set2_CM_I588T
│   ├── read_mapped_in_proper_pair.list
│   ├── Set2_CM_I588T_1.fq.gz
│   └── Set2_CM_I588T_2.fq.gz
├── Set2_CM_I588T-1
│   ├── read_mapped_in_proper_pair.list
│   ├── Set2_CM_I588T-1_1.fq.gz
│   └── Set2_CM_I588T-1_2.fq.gz
├── Set2_CM_R160Q
│   ├── read_mapped_in_proper_pair.list
│   ├── Set2_CM_R160Q_1.fq.gz
│   └── Set2_CM_R160Q_2.fq.gz
├── Set2_CM_R160Q-1
│   ├── read_mapped_in_proper_pair.list
│   ├── Set2_CM_R160Q-1_1.fq.gz
│   └── Set2_CM_R160Q-1_2.fq.gz
└── Set2_CM_WT
    ├── read_mapped_in_proper_pair.list
    ├── Set2_CM_WT_1.fq.gz
    └── Set2_CM_WT_2.fq.gz
```







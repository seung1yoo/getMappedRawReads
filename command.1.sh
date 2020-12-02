find /data06/project/TBD200717_10391_TBI_RNAref_20201027/rawdata -iname '*.fq.gz' | sort > rawreadList.txt
find /data06/project/TBD200717_10391_TBI_RNAref_20201027/analysis/star -iname Aligned.sortedByCoord.out.bam | sort > inbamList.txt
# modified two List.txt files
python get_mappedRawReads.py create_config --outfn config.yaml --rawreadList rawreadList.txt --inbamList inbamList.txt --workdir /data06/project/TBD200717_10391_TBI_RNAref_20201027/202012011311_mappedRawReads
snakemake --cores $(wc -l inbamList.txt | awk '{ print $1 *2 }') --snakefile get_mappedRawReads.snakefile

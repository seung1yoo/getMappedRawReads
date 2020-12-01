# snakemake 5.10.0
# seung1.yoo@gmail.com


configfile: "config.yaml"
print(config)


def get_all_target(config):
    ls = list()
    for sample in config['samples']:
        ls.append('analysis/{0}/read_mapped_in_proper_pair.list'.format(sample))
        ls.append('analysis/{0}/{0}_1.fq.gz'.format(sample))
        ls.append('analysis/{0}/{0}_2.fq.gz'.format(sample))
    return ls


rule target:
	input: get_all_target(config)
	message: "Compiling all output"

rule get_read_mapped_in_proper_pair:
	input:
		bam=lambda wildcards: config["samples"][wildcards.sample]["inbam"]
	output:
		readList="analysis/{sample}/read_mapped_in_proper_pair.list"
	shell:
		"samtools view -f 3 {input.bam} | "
		"cut -f 1 | "
		"sort -u "
		"> {output.readList}"

rule extract_rawread:
	input:
		fastq_1=lambda wildcards: config["samples"][wildcards.sample]["fastq_1"],
		fastq_2=lambda wildcards: config["samples"][wildcards.sample]["fastq_2"],
		readList="analysis/{sample}/read_mapped_in_proper_pair.list"
	output:
		fastq_1="analysis/{sample}/{sample}_1.fq.gz",
		fastq_2="analysis/{sample}/{sample}_2.fq.gz"
	shell:
		"python get_mappedRawReads.py extract_rawread "
		" --in-fq-1 {input.fastq_1}"
		" --in-fq-2 {input.fastq_2}"
		" --readList {input.readList}"
		" --out-fq-1 {output.fastq_1}"
		" --out-fq-2 {output.fastq_2}"

	






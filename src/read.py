from Bio import SeqIO

input_file = "data/gene_export/fasta.faa"

fasta_sequences = SeqIO.parse(open(input_file),'fasta')

for fasta in fasta_sequences:
    print(fasta.__dir__())  
    print(fasta.id)
    print(fasta.seq)
    print("----")
    print(fasta.description)
    print("----")
    print(fasta.name)
    print("----")
    print(fasta.features)
    print(fasta.dbxrefs)
    print(fasta.annotations)
    break  

# print(fasta_sequences.__dir__())

# for fasta in fasta_sequences:
#     name, sequence = fasta.id, str(fasta.seq)
#     print(name, sequence)

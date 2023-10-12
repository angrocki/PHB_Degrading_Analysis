import os
import pandas as pd


SEARCH_TERM = "nitrogenase"
DATA = "both"
FILE_NAME = "nitrogenase_scaffold_both"
# Create new data frame

# Get Scaffold ID Linage
scaffold_data = pd.read_csv(f"data/Search/{FILE_NAME}.csv")
scaffold_data = scaffold_data[scaffold_data['Scaffold Gene Count']>2]
gene_data = pd.read_csv(f"data/Search/{SEARCH_TERM}_scaffold_{DATA}.csv")
for index in scaffold_data.index:
    scaffold_id = scaffold_data['Scaffold ID'][index]
    scaffold_id = scaffold_id.split(" ")[-1]
    scaffold_gene_count = scaffold_data['Scaffold Gene Count'][index]
    scaffold_lineage = scaffold_data['Lineage'][index]
    # Find scaffold genes
    print(scaffold_id)
    scaffold_genes_file = f"data/gene_export/scaffold_genes/{FILE_NAME}/{scaffold_id}.csv"
    print(scaffold_genes_file)
    scaffold_genes = pd.read_csv(scaffold_genes_file)
    for gene in scaffold_genes.index:
        gene_id = scaffold_genes['Gene ID'][gene]
        print(gene)
        break
    break
#Scaffold Genes
#Search Term Genes 
#Add Key info to data frame 



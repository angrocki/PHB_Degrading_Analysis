import os
import pandas as pd


SEARCH_TERM = "nitrogenase"
DATA = "both"
FILE_NAME = "nitrogenase_scaffold_both"
# Create new data frame
matched_genes = pd.DataFrame()
missing_scaffolds = pd.DataFrame()

# Get Scaffold ID Linage
scaffold_data = pd.read_csv(f"data/Search/{FILE_NAME}.csv")
scaffold_data = scaffold_data[scaffold_data['Scaffold Gene Count']>2]
gene_data = pd.read_csv(f"data/Search/{SEARCH_TERM}_gene_{DATA}.csv")
gene_data_ids = [x["Gene ID"].split(" ")[-1] for _, x in gene_data.iloc[0:].iterrows()]
for index in scaffold_data.index:
    scaffold_id = scaffold_data['Scaffold ID'][index]
    scaffold_id = scaffold_id.split(" ")[-1]
    scaffold_gene_count = scaffold_data['Scaffold Gene Count'][index]
    scaffold_lineage = scaffold_data['Lineage'][index]
    # Find scaffold genes
    scaffold_genes_file = f"data/gene_export/scaffold_genes/{FILE_NAME}/{scaffold_id}.csv"
    print(scaffold_genes_file)
    if os.path.exists(scaffold_genes_file):
        scaffold_genes = pd.read_csv(scaffold_genes_file, delimiter="\t")
        #Search Scaffold Genes
        for index in scaffold_genes.index:
            #Shorten Gene ID
            gene_id = scaffold_genes['Gene ID'][index]
            gene_id = gene_id.split(" ")[-1]
            #Add Key info to data frame 
            if gene_id in gene_data_ids:
                gene_row = {'Gene ID': gene_id, 'Scaffold ID': scaffold_id, 'Scaffold Gene Count': scaffold_gene_count, 'Lineage': scaffold_lineage}
                matched_genes = pd.concat([matched_genes, pd.DataFrame([gene_row])], ignore_index=True)
    # Record missing scaffolds
    else: 
        missing_scaffolds = pd.concat([  missing_scaffolds, pd.DataFrame({'Scaffold ID Short': scaffold_id, 'Scaffold ID': scaffold_data['Scaffold ID']})], ignore_index=True)
# save data to csv
missing_scaffolds.to_csv(f'data/gene_export/scaffold_genes/{FILE_NAME}/missing_scaffolds_{FILE_NAME}.csv', index=False)
matched_genes.to_csv(f'data/gene_export/scaffold_genes/{FILE_NAME}/matched_genes_{FILE_NAME}.csv', index=False)
multiples = matched_genes.pivot_table(index = ['Gene ID'], aggfunc ='size') 
multiples.to_csv(f'data/gene_export/scaffold_genes/{FILE_NAME}/repeated_matched_genes_{FILE_NAME}.csv', index=False)

#Scaffold Genes
#Search Term Genes 
#Add Key info to data frame 



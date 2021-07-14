import pandas as pd
import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.width", 400)
pd.set_option("display.max_columns", 14)
# Change path before running
path = "/Users//markd/PycharmProjects/BGU_Internship//data/"

df = pd.read_csv(r"{0}rna_consensus.tsv".format(path), sep = '\t')
df.columns = df.columns.str.lower()

rna_tissue = df[['gene name', 'tissue']]
rna_tissue.columns = ['gene_name', 'tissue']
rna_tissue.tissue = rna_tissue.tissue.str.lower()
rna_tissue = rna_tissue.drop_duplicates()

rna_nx = df[['gene name', 'nx']]
rna_nx.columns = ['gene_name', 'nx']
rna_nx = rna_nx.drop_duplicates()

print(rna_tissue.groupby('tissue')['gene_name'].count().reset_index().head(15))
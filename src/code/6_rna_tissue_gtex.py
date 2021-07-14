import pandas as pd
import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.width", 400)
pd.set_option("display.max_columns", 14)
# Change path before running
path = "/Users//markd/PycharmProjects/BGU_Internship//data/"

df = pd.read_csv(r"{0}rna_tissue_gtex.tsv".format(path), sep = '\t')
df.columns = df.columns.str.lower()
print(df)

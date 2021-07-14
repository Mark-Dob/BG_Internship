import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.width", 400)
pd.set_option("display.max_columns", 11)
# Change path before running
path = "/Users//markd/PycharmProjects/BGU_Internship//data/"

df = pd.read_csv(r"{0}pathology.tsv".format(path), sep = '\t')
df.columns = df.columns.str.lower()

pathology_cancer = df[["gene name", "cancer"]]
pathology_cancer.columns = ["gene_name", "cancer_type"]
pathology_cancer = pathology_cancer.drop_duplicates()

cancer_g = (
    pathology_cancer.groupby("gene_name")["cancer_type"]
        .count()
        .reset_index()
        .sort_values(
        by="cancer_type", ascending=False)
)


print(df)
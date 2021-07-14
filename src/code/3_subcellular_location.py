import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

warnings.filterwarnings("ignore")


def missing_values(data):
    nan_list = []

    for x in data:
        if len(data[data[x].isnull()]) > 0:
            nan_list.append(x)
    nan_perc = []
    for x in nan_list:
        nan_perc.append([x, (len(data[data[x].isnull()]) / len(data))])
    nan_perc = pd.DataFrame(nan_perc, columns=["column", "percentage missing"])
    nan_perc["percentage missing"] = (100.0 * nan_perc["percentage missing"]).round(
        2
    ).astype(str) + "%"
    print(nan_perc.sort_values(by=["percentage missing"], ascending=False))


pd.set_option("display.width", 400)
pd.set_option("display.max_columns", 14)
# Change path before running
path = "/Users//markd/PycharmProjects/BGU_Internship//data/"

df = pd.read_csv(r"{0}subcellular_location.tsv".format(path), sep='\t')
df.columns = df.columns.str.lower()

subcellular_main_location = df[["gene name", "main location"]]
subcellular_main_location.columns = ["gene_name", "main_location"]
subcellular_main_location.main_location = (
    subcellular_main_location.main_location.str.lower()
)
subcellular_main_location = subcellular_main_location.drop_duplicates()

subcellular_reliability = df[["gene name", "reliability"]]
subcellular_reliability.columns = ["gene_name", "reliability"]
subcellular_reliability.reliability = subcellular_reliability.reliability.str.lower()
subcellular_reliability = subcellular_reliability.drop_duplicates()

subcellular_approved_location = df[["gene name", "approved"]]
subcellular_approved_location.columns = ["gene_name", "approved_location"]
subcellular_approved_location.approved_location = (
    subcellular_approved_location.approved_location.str.lower()
)
subcellular_approved_location = subcellular_approved_location.drop_duplicates()

subcellular_go_id = df[["gene name", "go id"]]
subcellular_go_id.columns = ["gene_name", "go_id"]
subcellular_go_id.go_id = subcellular_go_id.go_id.str.lower()
subcellular_go_id = subcellular_go_id.drop_duplicates()

main_location = pd.concat(
    [
        Series(row["gene_name"], row["main_location"].split(";"))
        for _, row in subcellular_main_location.iterrows()
    ]
).reset_index()
main_location.columns = ("main_location", "gene_name")

main_location_g = (
    main_location.groupby("main_location")["gene_name"]
        .count()
        .reset_index()
        .sort_values(by="gene_name", ascending=False)
)

reliability_g = (
    subcellular_reliability.groupby("reliability")["gene_name"].count().reset_index()
)

subcellular_go_id = pd.concat(
    [
        Series(row["gene_name"], row["go_id"].split(";"))
        for _, row in subcellular_go_id.iterrows()
    ]
).reset_index()

subcellular_go_id.columns = ["go_id", "gene_name"]
subcellular_go_id.go_id = subcellular_go_id.go_id.str.replace(
    r"[^\)]+(\(|$)", ""
).str.replace(r"\)", "")
go_id_g = subcellular_go_id.groupby("go_id")["gene_name"].count().reset_index()

subcellular_approved_location = pd.concat(
    [
        Series(row["gene_name"], row["approved_location"].split(";"))
        for _, row in subcellular_approved_location.dropna().iterrows()
    ]
).reset_index()
subcellular_approved_location.columns = ["approved_location", "gene_name"]

approved_location_g =(
    subcellular_approved_location.groupby('approved_location')['gene_name']
        .count()
        .reset_index()
        .sort_values(by="gene_name", ascending=False)
)

plt.title("Reliability distribution")
plt.pie(
    reliability_g["gene_name"],
    autopct="%.0f%%",
    labels=reliability_g["reliability"],
    pctdistance=0.8,
    counterclock=True,
)
sns.set_style("darkgrid", {"axes.facecolor": ".8"})

plt.title("Main location distribution")
sns.barplot(
    data=main_location_g,
    x="main_location",
    y="gene_name",
    edgecolor="black",
    palette="ch:.25_r",
)
sns.set_style("darkgrid", {"axes.facecolor": ".8"})
plt.xlabel("Location")
plt.ylabel("Number of genes")
plt.xticks(rotation=90)

plt.title("Approved location distribution")
sns.barplot(
    data=approved_location_g,
    x="approved_location",
    y="gene_name",
    edgecolor="black",
    palette="ch:.25_r",
)
sns.set_style("darkgrid", {"axes.facecolor": ".8"})
plt.xlabel("Location")
plt.ylabel("Number of genes")
plt.xticks(rotation=90)
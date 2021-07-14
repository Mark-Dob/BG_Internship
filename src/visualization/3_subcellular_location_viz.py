import seaborn as sns
import matplotlib.pyplot as plt

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
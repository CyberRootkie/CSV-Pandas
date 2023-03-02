import pandas as pd

# On charge le CSV
df = pd.read_csv('data.csv')

# On affiche les 5 premières lignes
print(df.head(n=5))

# On fait un group by gender
print(
    df.groupby("gender")["id"].count()
)

# On fait un group by et on affiche par nb décroissant
print(
    df.groupby("gender")["id"].count().sort_values(ascending=False)
)

# Compter les lignes correspondant à des femmes
print(
    df[df["gender"] == "Female"]["id"].count()
)

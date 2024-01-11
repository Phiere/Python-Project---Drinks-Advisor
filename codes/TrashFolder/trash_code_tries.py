import pandas as pd

# Créez un DataFrame de démonstration
data = {'colonne1': ['A', 'B', 'C', 'D'],
        'colonne2': ['1', '2', '3', '4']}

df = pd.DataFrame(data)

# Concaténez les valeurs de 'colonne1' et 'colonne2' dans une nouvelle colonne 'nouvelle_colonne'
df['nouvelle_colonne'] = df['colonne1'] + df['colonne2']

# Affichez le DataFrame mis à jour
print(df)

import pandas as pd

ds = pd.read_csv(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';')


#Exercicio 1
oceania = ds[ds["Region"].str.contains("OCEANIA")]
print("Paises da Oceania:")
print(oceania["Country"])
print()
print("Quantidade de paises da Oceania:", len(oceania))
print()


#Exercicio 2
populacao = ds.loc[ds['Population'].idxmax()]
print("Pais com maior populaçao:" , populacao['Country'])
print("Localizado na regiao:", populacao['Region'])
print()

#Exercicio 3
regioes = ds.groupby("Region")
print("Media de literatura por regiao:", regioes["Literacy (%)"].mean())
print()


#Exercicio 4
no_coast = ds[ds["Coastline (coast/area ratio)"] == 0]
no_coast["Country"].to_csv("noCoast.csv")


#Exercicio 5
def Mortalidade(deathrate):
    if deathrate < 9:
        return "Balanced"
    else:
        return "Urgent"
    
ds["Humanitarian Help"] = ds["Deathrate"].apply(Mortalidade)
print(ds[["Country", "Humanitarian Help"]])
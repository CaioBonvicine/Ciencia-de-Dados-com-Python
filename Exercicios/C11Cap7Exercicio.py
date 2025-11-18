import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

ds = pd.read_csv(r"C:\Users\Meu-PC\Documents\Python\DataSets\airtravel.csv", 
                delimiter=',', 
                parse_dates=True, 
                index_col='Date')

air_series = ds['Passengers']

plt.figure(figsize=(10,4))
air_series.plot(title='Numero de Passageiros Aéreos', ylabel='Passageiros')
plt.show()

decomp_air = seasonal_decompose(air_series, model='additive')

decomp_air.plot()
plt.show()


#Respostas para airtravel:
#a) A serie possui Tendência? Sim, ao longo dos anos o numero de passageiros aumentou, tambem pode se notar um grande aumento principalmente entre os meses de Junho, Julho e Agosto antes de cair novamente e establizar, acontecendo novamente nos proximos anos.
#b) A serie possui Sazonalidade? Sim, a serie tem sazonalidade mensal com periodo igual a 12, e possivel notar que em determinados meses do ano (Junho, Julho e Agosto) o numero de passageiros aumenta significativamente, abaixando em meses como fevereiro e novembro.
#c) A serie possui Ciclos? Sim, é possivel notar que a serie possui ciclos anuais, com picos de passageiros em meses especificos do ano.



ds2 = pd.read_csv(r"C:\Users\Meu-PC\Documents\Python\DataSets\co2_emissions.csv", 
                delimiter=',')

ds2['Year'] = pd.to_datetime(ds2['Year'], format='%Y')
ds2 = ds2.set_index('Year')

co2_series = ds2['CO2_Emissions']


plt.figure(figsize=(10,4))
co2_series.plot(title='Emissoes de CO2', xlabel='Ano', ylabel='Emissoes de CO2')
plt.show()


decomp_co2 = seasonal_decompose(co2_series, model='additive')

decomp_co2.plot()
plt.show()

#Respostas para co2_emissions:
#a) A serie possui Tendência? Sim, a serie apresenta uma tendencia decrescente ao longo dos anos.
#b) A serie possui Sazonalidade? Não, a serie nao apresenta sazonalidade.
#c) A serie possui Ciclos? Sim, e possivel notar oxilacoes, possivelmente relacionadas a fatores externos.



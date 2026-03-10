import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#ENTRADAS
Capital = float(input('Digite o capital inicial (R$): '))
Aporte = float(input('Digite o Aporte inicial (R$): '))
Meses = int(input('Prazo (meses): '))
CDI_anual = float(input('CDI anual (%): '))/ 100
Perc_CDB = float(input('´Percentual em CDI (%): '))/ 100
Perc_LCI = float(input('´Percentual em LCI (%): '))/ 100
Taxa_FII = float(input('Rentabilidade mensal FII (%): '))/ 100
Meta = float(input('Meta Financeira (R$): '))

#CONVERSÃO CDI
CDI_mensal = math.pow((1+CDI_anual), 1/12) -1

#TOTAL INVESTIDO
Total_investido = Capital + (Aporte * Meses)

#CDB
Taxa_cdb = CDI_mensal + Perc_CDB
Montante_cdb = (Capital * math.pow((1 + Taxa_cdb), Meses) + (Aporte + Meses))
lucro_cdb = Montante_cdb - Total_investido
montante_cdb_liquido = Total_investido + (lucro_cdb * 0,85)

#LCI

taxa_lci = CDI_mensal + Perc_LCI
montante_lci = (Capital * math.pow(1 + taxa_lci)), Meses + (Aporte * Meses)

#POUPANÇA
taxa_poupança = 0.005
montante_poupança = (Capital * math.pow(1 + taxa_poupança), Meses + (Aporte * Meses))

#FII - SIMULAÇÕES

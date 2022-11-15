import pandas as pd
import math

datahandle={}
dh={}
caminhões=[]
créditos=[]
modelos=[]
meses=['janeiro', 'Fevereiro','Março', 'Abril', 'Maio', 'junho', 'julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro' , 'Dezembro','Créditos']


print('Nome do arquivo excel dos caminhões ')
arquivo=input()
tabela_df=pd.read_excel(arquivo)
high=len(tabela_df)
for c in range(high):
  modelo=tabela_df["Caminhão"][c]
  placa=tabela_df["Placa"][c]
  capacidade=tabela_df["Capacidade de Carga"][c]
  tanque=tabela_df["Capacidade do Tanque"][c]
  consumo_v=tabela_df["Diesel/km (vazio)"][c]
  consumo_c=tabela_df["Diesel/km (cheio)"][c]

  modelos.append(modelo)
  #Perguntas obrigatórias
  print()
  print(f'Sobre o {modelo} de placa {placa} ')
  km=float(input('Digite a distância que será percorrida: '))
  carga=float(input('Qual o peso da carga à ser transportada (t):  '))
  print()
  
  
  distância_mv=tanque/consumo_v
  distância_mc= tanque/consumo_c
  carbono=3.2*(km*consumo_c)/1000 #kg/L
  carbono=round(carbono,2)
  créditos.append(carbono)
  
  
  if carga!=0:
    abastecimento=km/distância_mc
  else:
    abastecimento=km/distância_mv
  abastecimento=math.ceil(abastecimento)
  
  #Perguntas obrigatórias
  datahandle["Caminhão"]=modelo
  datahandle["Placa"]=placa
  datahandle["Capacidade de Carga"]=capacidade
  datahandle["Capacidade do Tanque"]=tanque
  datahandle["Diesel/km (vazio)"]=consumo_v
  datahandle["Diesel/km (cheio)"]=consumo_c
  datahandle["Será abastecido:"]=abastecimento
  datahandle["Emissão de Carbono"]=carbono
  caminhões.append(datahandle.copy())



arquivo2=input('Arquivo do consumo de carbono ')

mes=int(input('Mês Atual (Ex: 1,2,3,10,11,12) '))

if mes==1:
  for mês in meses:
    dh[mês]=0
  dh=pd.DataFrame(dh, index=modelos, dtype=float)
else:
  for mês in meses:
    dh[mês]=0
  dh0=pd.read_excel(arquivo2, index_col=[0])
  dh=pd.DataFrame(dh, index=modelos, dtype=float)
  
  for i in range(mes-1):
    mês=meses[i]
    l1=len(dh0[mês][:])
    l2=len(dh[mês][:])
    if l2>l1:
      dh[mês][:l1]=dh0[mês][:]
    elif l2<l1:
      dh[mês][:]=dh0[mês][:l2]
    else:
      dh[mês][:]=dh0[mês][:]

v=len(modelos)
mês=meses[mes-1]
amês=meses[mes-2]
for i in range(v):
    dh[mês][i]=créditos[i]
    if mes==1:
      dh["Créditos"]=0
    else:  
      dh["Créditos"][i]=dh[amês][i]-dh[mês][i]
  

dh.to_excel(arquivo2)
df=pd.DataFrame(caminhões)
df.to_excel(arquivo,index=False)
print()
print('------------------------------------------------------------------RESUMO---------------------------------------------------------------------')
print()
print(df)
print()
print(dh)
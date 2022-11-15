import pandas as pd

datahandle={}
caminhões=[]
multa="NULO"
carbono=0
abastecimento=0

r0=input('Você irá adicionar ou remover um caminhão? (a/r)')
if r0=='a':
  
  print('Nome do arquivo excel dos caminhões ( Não esqueça do sufixo .xlsx ) ')
  arquivo=input()
  tabela_df=pd.read_excel(arquivo)
  high=len(tabela_df)
  for c in range(high):
    datahandle["Caminhão"]=tabela_df["Caminhão"][c]
    datahandle["Placa"]=tabela_df["Placa"][c]
    datahandle["Capacidade de Carga"]=tabela_df["Capacidade de Carga"][c]
    datahandle["Capacidade do Tanque"]=tabela_df["Capacidade do Tanque"][c]
    datahandle["Diesel/km (vazio)"]=tabela_df["Diesel/km (vazio)"][c]
    datahandle["Diesel/km (cheio)"]=tabela_df["Diesel/km (cheio)"][c]
    datahandle["Será abastecido:"]=tabela_df["Será abastecido:"][c]
    datahandle["Emissão de Carbono"]=tabela_df["Emissão de Carbono"][c]
    caminhões.append(datahandle.copy())
    
    

  r1=int(input('Quantos caminhões serão adicionados? '))
  for i in range(r1):
    capacidade=float(input(f'Coloque a capacidade de carga do {i+1}° caminhão (t): '))
    placa=input('Placa do mesmo caminhão: ')
    r2=input('Quer usar os valores em média, de um veículo como o seu, ou fazer personalizado? (m/p) ')
    if r2=='m':
      if capacidade<=3:
        modelo='VUC'
        tanque=150#L
        consumo_v=6.2#km/L
        consumo_c=6.5#km/L
          
      elif capacidade>3 and capacidade <= 6:
        modelo ='Toco'
        tanque=180#L
        consumo_v=5.36#km/L
        consumo_c=6.2#km/L
        
      elif capacidade>6 and capacidade <= 14: 
        modelo ='Truck'
        tanque=450#L
        consumo_v=3.36#km/L
        consumo_c=6.2#km/L 
        
      elif capacidade>14 and capacidade <= 33: 
        modelo ='Carreta 2 eixos'
        tanque=950#L
        consumo_v=1.77#km/L
        consumo_c=3.09#km/L
        
      elif capacidade>33 and capacidade <= 41.5: 
        modelo ='Cavalo Mecânico'
        tanque=1000#L
        consumo_v=1.86#km/L
        consumo_c=4.2#km/L

      elif capacidade>41.5 and capacidade <= 57: 
        modelo ='Bitrem'
        tanque=1200#L
        consumo_v=1.5#km/L
        consumo_c=2#km/L
        
      else: 
        modelo ='Rodotrem'
        tanque=1300#L
        consumo_v=1.5#km/L
        consumo_c=1.7#km/L
    else:
        modelo =input('Modelo do Caminhão: ')
        tanque=float(input('Capacidade do Tanque de combustível: '))
        consumo_v=float(input('Consumo, em média, de diesel sem carga: '))
        consumo_c=float(input('Consumo, em média, de diesel cheio de carga: '))
      
    datahandle["Caminhão"]=modelo
    datahandle["Placa"]=placa
    datahandle["Capacidade de Carga"]=capacidade
    datahandle["Capacidade do Tanque"]=tanque
    datahandle["Diesel/km (vazio)"]=consumo_v
    datahandle["Diesel/km (cheio)"]=consumo_c
    datahandle["Será abastecido:"]=abastecimento
    datahandle["Emissão de Carbono"]=carbono
    caminhões.append(datahandle.copy())


  df=pd.DataFrame(caminhões)
  df.to_excel(arquivo, index=False)
  print(df)

elif r0=='r':

  datahandle={}
  caminhões=[]
  carbono=0
  abastecimento=0

  r1=int(input('Quantos caminhões serão removidos? '))
  for i in range(r1):   
    print('Nome do arquivo excel dos caminhões ( Não esqueça do sufixo .xlsx ) ')
    arquivo=input()
    tabela_df=pd.read_excel(arquivo)
    placa=input('Placa do caminhão que deseja remover: ' )
    df=tabela_df.loc[tabela_df["Placa"]!=placa]
    print(df)
    df.to_excel(arquivo, index=False)
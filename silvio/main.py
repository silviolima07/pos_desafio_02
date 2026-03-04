import pandas as pd
import glob
import os

def hex_to_float(valor):
    try:
        return float(int(str(valor), 16))
    except:
        return None

print('\n\nLendo os arquivos CSV...')

colunas = ["Time since reaction (ms)", "Filter (adc)"]
path = 'Desafio_2_2026_1'
lotes = ['Lote 062506', 'Lote 072501']
targets = ['Nivel 1', 'Nivel 3', 'Solucao 0', 'Solucao 1', 'Solucao 2']

lista_df = []
for lote in lotes:
    for target in targets:
        arquivos = glob.glob(os.path.join(path, lote, target, '*.csv'))
        
        for arquivo in arquivos:
            df = pd.read_csv(arquivo)
            df.columns = df.columns.str.strip() # Remove espaços extras dos nomes das colunas
            #print('Colunas disponíveis:', df.columns.tolist())
            #print(f'Arquivo: {arquivo}')
            lista_df.append(df[colunas])
            
            
            
df = pd.concat(lista_df, ignore_index=True)

for col in colunas:
    df[col] = df[col].apply(hex_to_float)
        
print('\n\nDataset lido:', df.shape)
print('\nDataset processado:\n', df.head())

x = df["Time since reaction (ms)"].values
y = df["Filter (adc)"].values

print('\nValores de X:', x[:5])
print('\nValores de y:', y[:5])
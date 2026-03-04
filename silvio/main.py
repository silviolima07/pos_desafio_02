import pandas as pd
import glob
import os

print('\n\nLendo os arquivos CSV...')

colunas = ["Time since reaction (ms)", "Filter (adc)"]

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, '..', 'Desafio_2_2026_1')
path = os.path.abspath(path)
print("Caminho final:", path)

lotes = ['Lote 062506', 'Lote 072501']
targets = ['Nivel I', 'Nivel III', 'Solucao 0', 'Solucao 1', 'Solucao 2']

lista_df = []
for lote in lotes:
    for target in targets:
        arquivos = glob.glob(os.path.join(path, lote, target, '*.csv'))
        #print('Diretório atual:', os.getcwd())
        #print('Lote:', lote)
        #print('Target:', target)
        #print('Arquivos encontrados:', arquivos)
        
        for arquivo in arquivos:
            df = pd.read_csv(arquivo)
            df.columns = df.columns.str.strip() # Remove espaços extras dos nomes das colunas
            #print('Total de linhas lidas:', len(df))
            #print('Colunas disponíveis:', df.columns.tolist())
            #print(f'Arquivo: {arquivo}')
            lista_df.append(df[colunas])
            
            
            
df = pd.concat(lista_df, ignore_index=True)

for col in colunas:
    df[col + '_hex'] = df[col]  # salva original
    df[col] = df[col].apply(lambda x: float(int(str(x), 16)))
        
print('\n\nDataset lido:', df.shape)
print('\nDataset processado:\n', df.head(20))

x = df["Time since reaction (ms)"].values
y = df["Filter (adc)"].values

print('\nValores de X:', x[:20])
print('\nValores de y:', y[:20])
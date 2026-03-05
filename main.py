import pandas as pd
import glob
import os

print('\n\nLendo os arquivos CSV...')

colunas = ["Time since reaction (ms)", "Filter (adc)"]

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, 'Desafio_2_2026_1')
path = os.path.abspath(path)

print("Caminho final:", path)

lotes = ['Lote 062506', 'Lote 072501']
solucoes = ['Nivel I', 'Nivel III', 'Solucao 0', 'Solucao 1', 'Solucao 2']

lista_df = []

for lote in lotes:
    for solucao in solucoes:

        arquivos = glob.glob(os.path.join(path, lote, solucao, '*.csv'))

        for arquivo in arquivos:

            df = pd.read_csv(arquivo)
            df.columns = df.columns.str.strip()

            df = df[colunas]

            # adiciona colunas corretamente
            df["Lote"] = lote
            df["Solucao"] = solucao

            lista_df.append(df)

df = pd.concat(lista_df, ignore_index=True)

# converter hexadecimal
for col in colunas:
    df[col] = df[col].apply(lambda x: float(int(str(x), 16)))

print('\nDataset lido:', df.shape)
print('\nDataset processado:\n', df.head())

# salvar dataset
output_path = os.path.join(base_dir, 'dataset_processado.csv')
df.to_csv(output_path, index=False)

print('\nDataset salvo em dataset_processado.csv')

print("\nValores nulos:\n", df.isna().sum())
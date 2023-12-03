import pandas as pd

# Lee los archivos CSV
df1 = pd.read_csv('contacts.csv')
df2 = pd.read_csv('contacts2.csv')

# Encuentra las diferencias utilizando merge
diferencias = pd.merge(df1, df2, how='outer', indicator=True).query(
    '_merge != "both"').drop('_merge', axis=1)

# Muestra las diferencias
if diferencias.empty:
    print("Los DataFrames son iguales.")
else:
    print("Hay diferencias:")
    print(diferencias)
    # Pregunta al usuario si desea exportar las diferencias
    respuesta = input(
        "¿Deseas exportar las diferencias a un archivo CSV? (s/n): ").lower()

    if respuesta == 's':
        # Exporta las diferencias a un archivo CSV
        diferencias.to_csv('diferencias.csv', index=False)
        print("Diferencias exportadas a 'diferencias.csv'.")
    else:
        print("No se exportaron las diferencias.")

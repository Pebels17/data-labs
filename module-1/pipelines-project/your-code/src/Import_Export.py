def import_csv(archivo):
    data = pd.read_csv(archivo +'.csv', encoding = 'ISO-8859-1')
    return data


def export_to_csv(df,nombre): 
    df.to_csv(nombre + '.csv')
    return print("El archivo " + nombre + " se ha exportado correctamente")
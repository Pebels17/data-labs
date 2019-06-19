
#Para elegir las columnas que quieres borrar
def choose_columns_to_erase():
    respuesta = input("Elige la columnas que quieras borrar, separadas por comas")
    respuesta = respuesta.split(',')
    respuesta = [x.strip() for x in respuesta]
    return respuesta

#función para borrar las filas
def delete_columns(data,lista):
    deleted_columns = data.drop(lista, axis=1)
    return deleted_columns

#Funcion para eliminar la filas que no contengan un item
def delete_rows(df,columna,item): 
    df = df.loc[df[columna] != item]
    return df

#para borrar un item del nombre de cualquier columna
def erase_letter_from_column(df,letra):
    df.columns = df.columns.str.replace(letra,'')
    return df 

#Filtrar por un valor de una columna
def filter_item(df,columna,item): 
    df = df[df[columna] == item]
    return df

#Agrupamos por columna y hacemos la media 
def group_by_item(df,columna): 
    df.groupby([columna]).mean()
    return df

#Crea columna total, suma de todas las anteriores
def add_column_sum_all(df):
    col_list= list(df)
    df['Suma'] = df[col_list].sum(axis=1)
    return df

#Nos quedamos con el top x de productos que más sumen basado en una columna
def top_num(df,num,column):
    df = df.nlargest(num, [column])
    return df

#Para crear una columna index nueva
def reset_index(df):
    df = df.reset_index()
    return df

#Grafica top x productos
def gráfico_barras(df, eje_x, eje_y):
    graff = df.plot(kind='bar', x = eje_x, y = eje_y)
    return graff

#Comparamos con el resto de paises
def filter_item(df,columna,item): 
    df = df[df[columna] == item]
    return df


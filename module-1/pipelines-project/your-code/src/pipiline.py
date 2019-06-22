from Import_Export import * 
from Limpiar_csv import *


def main(): 
    print('dentro de main main')

    df = import_csv('FAO')
    
    columnas_borrar = choose_columns_to_erase()
    "Area Abbreviation, Area Code, Item Code, Element Code"
    
    df = delete_columns(df,columnas_borrar)
    
    df = delete_rows(df,'Element','Feed')

    df = erase_letter_from_column(df, 'Y')

    spain = filter_item(df, 'Area','Spain')

    spain = group_by_item(spain, 'Item')

    columnas_borrar_2 = choose_columns_to_erase()
    "latitude, longitude"

    spain = delete_columns(spain,columnas_borrar_2)

    spain = add_column_sum_all(spain)

    spain = top_num(spain,10,'Suma')

    spain = reset_index(spain)

    gráfico_spain = gráfico_barras(spain,'Item','Suma')

    vegetables = filter_item(df,'Item','Vegetables')
    col_list_2 = list(vegetables)
    col_list_2.remove('latitude')
    col_list_2.remove('longitude')
    
    vegetables['suma'] = vegetables[col_list_2].sum(axis=1)
    print(vegetables.head()

    vegetables.to_csv('production_vegetables.csv')







"""
def test(): 
    print('dentro de main main')

    df = import_csv('FAO')

    df = erase_letter_from_column(df, 'Y')
    print(df.head())
"""
    
if __name__ == "__main__":
    # main()
    main()
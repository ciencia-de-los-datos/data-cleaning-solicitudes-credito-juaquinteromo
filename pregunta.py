"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    del dataframe['Unnamed: 0']
    dataframe = dataframe.dropna().drop_duplicates()
    dataframe['sexo']=dataframe['sexo'].apply(str.lower).str.capitalize()
    dataframe['tipo_de_emprendimiento']=dataframe['tipo_de_emprendimiento'].apply(str.lower).str.capitalize()
    dataframe['idea_negocio']=dataframe['idea_negocio'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ')).str.capitalize()
    dataframe['barrio']=dataframe['barrio'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ')).str.capitalize()
    dataframe['línea_credito'] = dataframe['línea_credito'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ')).str.capitalize()
    dataframe['monto_del_credito'] = dataframe['monto_del_credito'].str.replace(',', '').str.replace('$', '', regex=False).str.replace(' ', '').astype(float)
    dataframe['fecha_de_beneficio'] = pd.to_datetime(dataframe['fecha_de_beneficio'], dayfirst=True)
    dataframe = dataframe.drop_duplicates().dropna()
    dataframe.reset_index(drop = True)

    return dataframe

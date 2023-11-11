
#' Convertir un documento de excel a csv:

import pandas as pd

def excel_to_csv(excel_file, csv_file):
    # Cargar el archivo Excel
    xls = pd.ExcelFile(excel_file)

    #* Iterar sobre todas las hojas en el archivo Excel
    for sheet_name in xls.sheet_names:
        # Cargar la hoja en un DataFrame
        df = pd.read_excel(excel_file, sheet_name)

        # *Guardar como archivo CSV
        df.to_csv(f'{csv_file}_{sheet_name}.csv', index=False)

# *Reemplazar 'input.xlsx' con la ruta de tu archivo Excel y 'output' con el nombre base deseado para el archivo CSV
excel_to_csv("C:/Users/mar_amez/Desktop/gio/archivos_py/diabetes_dataset.xlsx", 'Arch_csv_creado')

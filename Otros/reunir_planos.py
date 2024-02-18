import os
import shutil
path = 'P:/REMICA/EDIFICIO TORRE DE VALORES/PLANOS S01'

# Nombre de las carpetas
folder_names = os.listdir(path)

# Ruta completa de las carpetas
folder_path = [path + '/' + folder for folder in folder_names]

# Nombre viejo y nuevo de los planos
old_sheet_names = []
new_sheet_names = []
for folder in folder_path:
    sheet = os.listdir(folder)[0]
    sheet_path = folder + '/' + sheet
    new_sheet_path = path + '/' + sheet
    old_sheet_names.append(sheet_path)
    new_sheet_names.append(new_sheet_path)

for file, new_file in zip(old_sheet_names, new_sheet_names):
    shutil.move(file, new_file)
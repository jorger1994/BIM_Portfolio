import os
import shutil
path = "P:/REMICA/EDIFICIO TORRE DE VALORES/PLANOS INTERFERENCIAS 3"
while True:
    formato = input('seleccione el formato, teclear 1 para pdf y 2 para dwg: ')
    if int(formato) == 1:
        ext = '.pdf'
        break
    elif int(formato) == 2:
        ext = '.dwg'
        break
    else:
        print('el formato no es válido')

# Nombre de los archivos
names = os.listdir(path)

# Nombre de los archivos sin la extensión
cleaned_names = [name.split(ext)[0] for name in names]

# Directorio para las carpetas
folder_names = [os.path.join(path, name) for name in cleaned_names]

# Crear carpetas
for folder in folder_names:
    os.mkdir(folder)

# Nombre de los archivos con la extensión    
files = [os.path.join(path, name) for name in names]

# Nuevo nombre de los archivos
new_files = []
for cleaned_name, name in zip(cleaned_names, names):
    new_file = path + '/' + cleaned_name + '/' + name
    new_files.append(new_file)

for file, new_file in zip(files, new_files):
    shutil.move(file, new_file)